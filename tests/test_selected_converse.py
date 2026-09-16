"""Finite consistency checks for the selected converse note.

No simulation or general performance claim. All laws are enumerated explicitly.
The reference NP calculation is used to check lower bounds, not to propose a
particular sequential test. These helpers are deliberately small model tools.
"""
import math
import unittest
from itertools import product


def power(q, p, lam):
    if lam <= 1 or not math.isfinite(lam):
        raise ValueError('This check requires finite lambda > 1')
    if len(p) != len(q):
        raise ValueError('Different alphabets')
    terms = []
    for qi, pi in zip(q, p):
        if qi == 0:
            continue
        if pi == 0:
            return math.inf
        terms.append(math.exp(lam*math.log(qi)+(1-lam)*math.log(pi)))
    return math.fsum(terms)


def renyi(q, p, lam):
    return math.log(power(q, p, lam))/(lam-1)


def np_test(p, q, epsilon):
    """Exact finite NP allocation, allowing a randomised boundary."""
    if not 0 <= epsilon <= 1:
        raise ValueError('Invalid Type I constraint')
    decision = [0.0]*len(p)
    remaining = epsilon
    order = sorted(range(len(p)),
                   key=lambda i: q[i]/p[i] if p[i] else math.inf,
                   reverse=True)
    for i in order:
        if p[i] == 0:
            decision[i] = float(q[i] > 0)
        elif remaining > 0:
            decision[i] = min(1.0, remaining/p[i])
            remaining = max(0.0, remaining-p[i]*decision[i])
    alpha = math.fsum(pi*f for pi, f in zip(p, decision))
    beta = math.fsum(qi*(1-f) for qi, f in zip(q, decision))
    return alpha, beta, decision


def dependent_rows(x):
    """Two new observations: the second depends on the first and old x."""
    p, q = [], []
    for y1, y2 in product((0, 1), repeat=2):
        pfirst, qfirst = .2+.2*x, .6-.1*x
        psecond, qsecond = .1+.3*x+.35*y1, .7-.2*x-.25*y1
        p.append((pfirst if y1 else 1-pfirst)
                 * (psecond if y2 else 1-psecond))
        q.append((qfirst if y1 else 1-qfirst)
                 * (qsecond if y2 else 1-qsecond))
    return p, q


def selected(phi):
    p0, q0 = [.7, .3], [.35, .65]
    a = math.fsum(pi*f for pi, f in zip(p0, phi))
    s = math.fsum(qi*f for qi, f in zip(q0, phi))
    if a == 0 or s == 0:
        raise ValueError('The selected branch must have positive reach')
    p, q = [], []
    for x, f in enumerate(phi):
        px, qx = dependent_rows(x)
        p.extend(f*p0[x]*v/a for v in px)
        q.extend(f*q0[x]*v/s for v in qx)
    return p0, q0, a, s, p, q


def terms(phi, lam, reverse=False):
    p0, q0, a, s, p, q = selected(phi)
    if reverse:
        p0, q0 = q0, p0
    H = power(q0, p0, lam)
    rho = math.fsum(f*qi**lam*pi**(1-lam)
                    for pi, qi, f in zip(p0, q0, phi))/H
    conditional = []
    for x in range(2):
        px, qx = dependent_rows(x)
        conditional.append(power(px, qx, lam) if reverse
                           else power(qx, px, lam))
    average = math.fsum(f*qi**lam*pi**(1-lam)*z
                        for pi, qi, f, z in zip(p0, q0, phi, conditional)) / (H*rho)
    return math.log(H)/(lam-1), rho, math.log(average)/(lam-1)


def ar_information(k, gamma):
    return (k*(1-gamma)+2*gamma)/(1+gamma)


def quadratic_inverse_sum(matrix):
    """Solve matrix*x=1 by elimination and return sum(x)."""
    size = len(matrix)
    a = [row[:] + [1.0] for row in matrix]
    for i in range(size):
        pivot = max(range(i, size), key=lambda j: abs(a[j][i]))
        a[i], a[pivot] = a[pivot], a[i]
        factor = a[i][i]
        if abs(factor) < 1e-15:
            raise ValueError('Singular matrix')
        a[i] = [v/factor for v in a[i]]
        for j in range(size):
            if j != i:
                factor = a[j][i]
                a[j] = [v-factor*w for v, w in zip(a[j], a[i])]
    return math.fsum(row[-1] for row in a)


class SelectedConverseTests(unittest.TestCase):
    orders = (1.125, 1.5, 2.0, 4.0)
    first_rules = ((.15, .85), (.2, .2), (0., 1.), (1., .2))

    def test_selected_joint_normalisation(self):
        for phi in self.first_rules:
            *_, p, q = selected(phi)
            self.assertAlmostEqual(math.fsum(p), 1.0)
            self.assertAlmostEqual(math.fsum(q), 1.0)

    def test_new_block_remains_dependent_given_old_data(self):
        for x in range(2):
            for row in dependent_rows(x):
                marginal_first = row[2]+row[3]
                marginal_second = row[1]+row[3]
                self.assertNotAlmostEqual(row[3], marginal_first*marginal_second)
        self.assertNotEqual(dependent_rows(0), dependent_rows(1))

    def test_selected_decomposition_both_directions(self):
        for phi, lam in product(self.first_rules, self.orders):
            _, _, a, s, p, q = selected(phi)
            I, rho, T = terms(phi, lam)
            S = (math.log(rho)-lam*math.log(s)-(1-lam)*math.log(a))/(lam-1)
            self.assertAlmostEqual(renyi(q, p, lam), I+S+T, places=11)
            I, rho, T = terms(phi, lam, reverse=True)
            S = (math.log(rho)-lam*math.log(a)-(1-lam)*math.log(s))/(lam-1)
            self.assertAlmostEqual(renyi(p, q, lam), I+S+T, places=11)

    def test_local_converse_substitution(self):
        for phi, lam, eps in product(self.first_rules, self.orders, (.01, .05, .2, .7)):
            _, _, a, s, p, q = selected(phi)
            c = (lam-1)/lam
            _, beta, _ = np_test(p, q, eps)
            I, rho, T = terms(phi, lam)
            substituted = max(0, 1-(a*eps)**c*rho**(1/lam)*math.exp(c*(I+T))/s)
            direct = max(0, 1-eps**c*math.exp(c*renyi(q, p, lam)))
            self.assertAlmostEqual(substituted, direct, places=11)
            self.assertLessEqual(substituted, beta+1e-11)

    def test_opposite_direction_converse_substitution(self):
        for phi, lam, eps in product(self.first_rules, self.orders, (.01, .05, .2, .7)):
            _, _, a, s, p, q = selected(phi)
            c = (lam-1)/lam
            _, beta, _ = np_test(p, q, eps)
            I, rho, T = terms(phi, lam, reverse=True)
            substituted = (a*(1-eps))**(1/c)*rho**(-1/(lam-1))*math.exp(-I-T)/s
            direct = (1-eps)**(1/c)*math.exp(-renyi(p, q, lam))
            self.assertAlmostEqual(substituted, direct, places=11)
            self.assertLessEqual(substituted, beta+1e-11)

    def test_two_node_survival_cancellation(self):
        for phi, lam, eps in product(self.first_rules, self.orders, (.01, .2, .7)):
            _, _, a, s, p, q = selected(phi)
            c = (lam-1)/lam
            _, beta, _ = np_test(p, q, eps)
            B = 1-s+s*beta
            I, rho, T = terms(phi, lam)
            factor = (a*eps)**c*rho**(1/lam)*math.exp(c*(I+T))
            local = max(0, 1-factor/s)
            global_lower = max(1-s, 1-factor)
            self.assertAlmostEqual(1-s+s*local, global_lower)
            self.assertLessEqual(global_lower, B+1e-11)

    def test_opposite_direction_path_bound(self):
        for phi, lam in product(self.first_rules, self.orders):
            _, _, a, s, p, q = selected(phi)
            eps, c = .2, (lam-1)/lam
            _, beta, _ = np_test(p, q, eps)
            I, rho, T = terms(phi, lam, reverse=True)
            lower = 1-s+(a*(1-eps))**(1/c)*rho**(-1/(lam-1))*math.exp(-I-T)
            self.assertLessEqual(lower, 1-s+s*beta+1e-11)

    def test_uniform_conditional_information_cap(self):
        for phi, lam in product(self.first_rules, self.orders):
            I, rho, T = terms(phi, lam)
            cap = max(renyi(*dependent_rows(x)[::-1], lam) for x in range(2))
            self.assertLessEqual(T, cap+1e-11)
            p0, q0, a, s, p, q = selected(phi)
            eps, c = .1, (lam-1)/lam
            _, beta, _ = np_test(p, q, eps)
            bound = max(0, 1-(a*eps)**c*math.exp(c*(I+cap)))
            self.assertLessEqual(bound, 1-s+s*beta+1e-11)

    def test_chain_caps_do_not_require_iid(self):
        for lam in self.orders:
            first_cap = max(renyi([.6-.1*x, .4+.1*x], [.2+.2*x, .8-.2*x], lam)
                            for x in range(2))
            second_cap = max(renyi([.7-.2*x-.25*y, .3+.2*x+.25*y],
                                   [.1+.3*x+.35*y, .9-.3*x-.35*y], lam)
                             for x, y in product(range(2), repeat=2))
            for x in range(2):
                p, q = dependent_rows(x)
                self.assertLessEqual(renyi(q, p, lam), first_cap+second_cap+1e-11)

    def test_multistage_all_ones_converse(self):
        for lam in self.orders:
            masses = {(): (1.0, 1.0)}
            caps, budgets = [], []
            for t in range(4):
                next_masses, conditional_d = {}, []
                old_p = math.fsum(v[0] for v in masses.values())
                for history, (pm, qm) in masses.items():
                    p1 = .15+.1*(sum(history) % 3)
                    q1 = .7-.1*(sum(history) % 3)
                    prow, qrow = [1-p1, p1], [1-q1, q1]
                    conditional_d.append(renyi(qrow, prow, lam))
                    for x in range(2):
                        f = .1+.65*x+.05*(t % 2)
                        next_masses[history+(x,)] = (pm*prow[x]*f, qm*qrow[x]*f)
                new_p = math.fsum(v[0] for v in next_masses.values())
                budgets.append(new_p/old_p)
                caps.append(max(conditional_d))
                masses = next_masses
            p_success = math.fsum(v[0] for v in masses.values())
            q_success = math.fsum(v[1] for v in masses.values())
            self.assertAlmostEqual(p_success, math.prod(budgets))
            c = (lam-1)/lam
            bound = max(0, 1-math.prod(budgets)**c*math.exp(c*math.fsum(caps)))
            self.assertLessEqual(bound, 1-q_success+1e-11)

    def test_zero_reach_is_not_normalised(self):
        with self.assertRaises(ValueError):
            selected((0., 0.))
        _, _, _, _, p, q = selected((0., 1.))
        self.assertTrue(all(v == 0 for v in p[:4]+q[:4]))
        self.assertTrue(math.isfinite(renyi(q, p, 2.0)))

    def test_repeated_fresh_observation_has_constant_information(self):
        p, q = [.8, .2], [.3, .7]
        for m in range(1, 6):
            pm, qm = [0.0]*(2**m), [0.0]*(2**m)
            pm[0], pm[-1] = p
            qm[0], qm[-1] = q
            self.assertAlmostEqual(renyi(qm, pm, 2.0), renyi(q, p, 2.0))

    def test_average_is_not_an_upper_information_bound(self):
        average = .001*10
        logarithmic_mean = math.log(.999+.001*math.exp(10))
        self.assertGreater(logarithmic_mean, 100*average)

    def test_upper_root_budget_cannot_enter_forward_lower_bound(self):
        a, eps0, eps1 = .1, .5, .05
        actual = 1-a*eps1
        valid = 1-a+(a*(1-eps1))**2/a
        invalid = 1-a+(eps0*(1-eps1))**2/a
        self.assertLessEqual(valid, actual)
        self.assertGreater(invalid, 1.0)

    def test_ar_information_matches_covariance_inverse(self):
        for k, gamma in product(range(1, 11), (.2, .6, .9)):
            covariance = [[gamma**abs(i-j) for j in range(k)] for i in range(k)]
            self.assertAlmostEqual(quadratic_inverse_sum(covariance),
                                   ar_information(k, gamma), places=10)

    def test_gaussian_order_optimisation(self):
        for L, J in product((.1, 1., 6.), (0., .2, 2., 9.)):
            best = max(0, math.sqrt(L)-math.sqrt(J))**2
            for lam in (1.0001, 1.1, 1.5, 2., 4., 10., 1000.):
                value = max(0, (lam-1)/lam*(L-lam*J))
                self.assertLessEqual(value, best+1e-11)
            if L > J > 0:
                lam = math.sqrt(L/J)
                self.assertAlmostEqual((lam-1)/lam*(L-lam*J), best, places=11)

    def test_gaussian_sample_size_inversion(self):
        L = math.log(1/(.05*.05))
        required = (math.sqrt(L)-math.sqrt(-math.log1p(-.1)))**2
        n = 20
        J0 = .5*ar_information(n, .6)
        minimum = max(1, math.ceil(((1+.6)*(required-J0)/.5-2*.6)/(1-.6)))
        self.assertEqual(minimum, 11)
        self.assertLess(J0+.5*ar_information(minimum-1, .6), required)
        self.assertGreaterEqual(J0+.5*ar_information(minimum, .6), required)
        for N, expected in ((30, .10107372125552405), (31, .08452053241686153)):
            J = N/8+3/4
            bound = -math.expm1(-max(0, math.sqrt(L)-math.sqrt(J))**2)
            self.assertAlmostEqual(bound, expected, places=12)


if __name__ == '__main__':
    unittest.main()
