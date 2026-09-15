"""Small finite models, using H_lambda(Q,P) and D_lambda(Q||P).

Stages start at one. A history is ((x_1,a_1),...,(x_t,a_t)).
Full history enumeration is exponential. These routines use ordinary floating
point and do not provide a general approximation guarantee.
"""
from collections.abc import Callable, Mapping, Sequence
import math
import random
from typing import Hashable

History = tuple[tuple[int, int], ...]
Kernel = Callable[[int, History], Sequence[float]]
Policy = Callable[[int, History, int], float]
Masses = dict[History, tuple[float, float]]  # P mass, Q mass


def _order(lam: float, below_one: bool = False) -> None:
    if not math.isfinite(lam) or lam <= 0 or lam == 1 or (below_one and lam >= 1):
        raise ValueError("Require 0 < lambda < 1" if below_one else
                         "Require finite lambda > 0, lambda != 1")


def _horizon(value: int) -> None:
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise ValueError("Horizon must be a nonnegative integer")


def _vector(values: Sequence[float]) -> tuple[float, ...]:
    row = tuple(values)
    if not row or any(not math.isfinite(v) or v < 0 for v in row):
        raise ValueError("Probability vectors must be finite and nonnegative")
    if not math.isclose(math.fsum(row), 1.0, rel_tol=0, abs_tol=1e-12):
        raise ValueError("Probabilities must sum to one")
    return row


def _rows(p: Sequence[float], q: Sequence[float]):
    p, q = _vector(p), _vector(q)
    if len(p) != len(q):
        raise ValueError("Alphabet sizes differ")
    return p, q


def _decision(value: float) -> float:
    if not math.isfinite(value) or not 0 <= value <= 1:
        raise ValueError("Policy values must lie in [0,1]")
    return value


def _term(q: float, p: float, lam: float) -> float:
    if q == 0:
        return 0.0
    if p == 0:
        return math.inf if lam > 1 else 0.0
    value = math.exp(lam * math.log(q) + (1-lam) * math.log(p))
    if value == 0:
        raise ArithmeticError("Positive power term underflowed")
    return value


def power_integral(q: Sequence[float], p: Sequence[float], lam: float) -> float:
    """H_lambda(Q,P), with exact zero support conventions."""
    _order(lam)
    p, q = _rows(p, q)
    if p == q:
        return 1.0
    return math.fsum(_term(qi, pi, lam) for pi, qi in zip(p, q))


def divergence(q: Sequence[float], p: Sequence[float], lam: float) -> float:
    value = power_integral(q, p, lam)
    if value == 0 or math.isinf(value):
        return math.inf
    return math.log(value) / (lam-1)


def prefix_laws(p_kernel: Kernel, q_kernel: Kernel,
                policy: Policy, horizon: int) -> list[Masses]:
    """Enumerate unnormalised prefix masses; never query a zero reach model."""
    _horizon(horizon)
    levels: list[Masses] = [{(): (1.0, 1.0)}]
    for t in range(1, horizon+1):
        following: Masses = {}
        for h, (pm, qm) in levels[-1].items():
            p = _vector(p_kernel(t, h)) if pm > 0 else None
            q = _vector(q_kernel(t, h)) if qm > 0 else None
            if p is not None and q is not None and len(p) != len(q):
                raise ValueError("Alphabet sizes differ")
            size = len(p if p is not None else q)
            for x in range(size):
                px = pm*p[x] if p is not None else 0.0
                qx = qm*q[x] if q is not None else 0.0
                if px == 0 and qx == 0:
                    continue
                f = _decision(policy(t, h, x))
                for a, kappa in ((0, 1-f), (1, f)):
                    if kappa > 0:
                        following[h+((x, a),)] = (px*kappa, qx*kappa)
        levels.append(following)
    return levels


def path_power(masses: Mapping[History, tuple[float, float]], lam: float) -> float:
    return power_integral([v[1] for v in masses.values()],
                          [v[0] for v in masses.values()], lam)


def backward_power(p_kernel: Kernel, q_kernel: Kernel, policy: Policy,
                   horizon: int, lam: float, history: History = ()) -> float:
    """The manuscript's G_t recursion, on common reachable histories only."""
    _order(lam, below_one=True)
    _horizon(horizon)
    if horizon < len(history):
        raise ValueError("History extends beyond horizon")

    def visit(h: History) -> float:
        if len(h) == horizon:
            return 1.0
        t = len(h)+1
        p, q = _rows(p_kernel(t, h), q_kernel(t, h))
        terms = []
        for x, (px, qx) in enumerate(zip(p, q)):
            mass = _term(qx, px, lam)
            if mass == 0:
                continue
            f = _decision(policy(t, h, x))
            future = math.fsum(k*visit(h+((x, a),))
                               for a, k in ((0, 1-f), (1, f)) if k > 0)
            terms.append(mass*future)
        return math.fsum(terms)
    return visit(history)


def predictable_values(p_kernel: Kernel, q_kernel: Kernel, policy: Policy,
                       horizon: int, lam: float) -> tuple[Masses, dict[History, float]]:
    """Enumerate the predictable estimator of 1-H_lambda on all paths."""
    _order(lam, below_one=True)
    levels = prefix_laws(p_kernel, q_kernel, policy, horizon)
    increments: dict[History, float] = {}
    for t, level in enumerate(levels[:-1], start=1):
        for h, (pm, qm) in level.items():
            if pm == 0 or qm == 0:
                increments[h] = 0.0
                continue
            p, q = _rows(p_kernel(t, h), q_kernel(t, h))
            omega = qm/(pm+qm)
            w = 2*_term(omega, 1-omega, lam)
            increments[h] = w*(1-power_integral(q, p, lam))
    values = {h: math.fsum(increments[h[:i]] for i in range(horizon))
              for h in levels[-1]}
    return levels[-1], values


def mixture_moments(masses: Masses, values: Mapping[History, float]):
    if set(masses) != set(values):
        raise ValueError("Path sets differ")
    mean = math.fsum((pm+qm)*values[h]/2 for h, (pm, qm) in masses.items())
    second = math.fsum((pm+qm)*values[h]**2/2 for h, (pm, qm) in masses.items())
    return mean, second


def sample_gap(p_kernel: Kernel, q_kernel: Kernel, policy: Policy,
               horizon: int, lam: float, rng: random.Random) -> tuple[float, History]:
    """One mixture trajectory. Requires matching conditional supports.

    Draw the simulation label once, exclude it from the posterior, and use the
    same policy under both models. No accuracy claim accompanies one draw.
    """
    _order(lam, below_one=True)
    _horizon(horizon)
    use_q = rng.random() < 0.5
    omega, total, history = 0.5, 0.0, ()
    for t in range(1, horizon+1):
        p, q = _rows(p_kernel(t, history), q_kernel(t, history))
        if any((pi == 0) != (qi == 0) for pi, qi in zip(p, q)):
            raise ValueError("Sampler requires matching conditional supports")
        total += 2*_term(omega, 1-omega, lam)*(1-power_integral(q, p, lam))
        row = q if use_q else p
        u, cumulative = rng.random(), 0.0
        x = max(i for i, mass in enumerate(row) if mass > 0)
        for i, mass in enumerate(row):
            cumulative += mass
            if u < cumulative:
                x = i
                break
        denominator = omega*q[x]+(1-omega)*p[x]
        omega = omega*q[x]/denominator
        f = _decision(policy(t, history, x))
        a = int(rng.random() < f)
        history += ((x, a),)
    return total, history


def finite_state_power(states: Sequence[Sequence[Hashable]], initial: Hashable,
                       p_kernel: Callable, q_kernel: Callable, policy: Callable,
                       update: Callable, lam: float) -> float:
    """Exact recursion when the declared state is genuinely sufficient.

    states[t-1] is the state set before stage t; the last set is terminal.
    The caller must establish sufficiency for both kernels AND the policy.
    """
    _order(lam, below_one=True)
    if not states or initial not in states[0]:
        raise ValueError("Initial state missing")
    values = {s: 1.0 for s in states[-1]}
    for t in range(len(states)-1, 0, -1):
        current = {}
        for s in states[t-1]:
            p, q = _rows(p_kernel(t, s), q_kernel(t, s))
            terms = []
            for x, (px, qx) in enumerate(zip(p, q)):
                mass = _term(qx, px, lam)
                if mass == 0:
                    continue
                f = _decision(policy(t, s, x))
                future = math.fsum(k*values[update(t, s, x, a)]
                                   for a, k in ((0, 1-f), (1, f)) if k > 0)
                terms.append(mass*future)
            current[s] = math.fsum(terms)
        values = current
    return values[initial]
