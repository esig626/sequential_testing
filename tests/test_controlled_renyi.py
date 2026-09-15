import math
import random
import unittest
from collections import defaultdict
from src.controlled_renyi import (power_integral, divergence, prefix_laws,
    path_power, backward_power, predictable_values, mixture_moments,
    sample_gap, finite_state_power)


def controlled():
    def p(t, h):
        b = .3 if not h else .2+.15*h[-1][1]+.1*(sum(x for x, _ in h) % 2)
        return [b, 1-b]
    def q(t, h):
        b = .6 if not h else .65-.2*h[-1][1]+.05*(sum(x for x, _ in h) % 2)
        return [b, 1-b]
    def phi(t, h, x):
        return .15+.55*x+(.1*h[-1][1] if h else 0)
    return p, q, phi


def rare_action(tau):
    def p(t, h):
        return [.75, .25] if t == 2 and h[-1][1] else [.5, .5]
    def q(t, h):
        return [.25, .75] if t == 2 and h[-1][1] else [.5, .5]
    return p, q, lambda t, h, x: tau if t == 1 else .5


def increment(p, q, levels, h, lam):
    pm, qm = levels[len(h)][h]
    if pm == 0 or qm == 0:
        return 0.0
    omega = qm/(pm+qm)
    return 2*omega**lam*(1-omega)**(1-lam)*(1-power_integral(q(len(h)+1, h), p(len(h)+1, h), lam))


class ControlledRenyiTests(unittest.TestCase):
    def test_orientation_is_q_then_p(self):
        q, p, lam = [.1, .9], [.4, .6], .3
        expected = sum(qi**lam*pi**(1-lam) for qi, pi in zip(q, p))
        self.assertAlmostEqual(power_integral(q, p, lam), expected)
        self.assertNotAlmostEqual(divergence(q, p, lam), divergence(p, q, lam))

    def test_nonidentical_products_with_common_policy(self):
        p = [[.2, .8], [.6, .4], [.35, .65]]
        q = [[.55, .45], [.25, .75], [.65, .35]]
        pk, qk = lambda t, h: p[t-1], lambda t, h: q[t-1]
        phi = controlled()[2]
        for lam in (.25, .5, .75):
            with self.subTest(lam=lam):
                h = backward_power(pk, qk, phi, 3, lam)
                self.assertAlmostEqual(h, math.prod(power_integral(qi, pi, lam) for pi, qi in zip(p, q)))
                self.assertAlmostEqual(math.log(h)/(lam-1), sum(divergence(qi, pi, lam) for pi, qi in zip(p, q)))

    def test_backward_matches_path_enumeration(self):
        p, q, phi = controlled()
        masses = prefix_laws(p, q, phi, 3)[-1]
        for lam in (.25, .5, .75):
            self.assertAlmostEqual(backward_power(p, q, phi, 3, lam), path_power(masses, lam), places=12)

    def test_path_masses_are_normalised(self):
        for level in prefix_laws(*controlled(), 3):
            self.assertAlmostEqual(sum(pm for pm, _ in level.values()), 1)
            self.assertAlmostEqual(sum(qm for _, qm in level.values()), 1)

    def test_common_policy_cancels_likelihood_ratio(self):
        p, q, phi = controlled()
        for h, (pm, qm) in prefix_laws(p, q, phi, 3)[-1].items():
            ratio = math.prod(q(i+1, h[:i])[x]/p(i+1, h[:i])[x] for i, (x, _) in enumerate(h))
            self.assertAlmostEqual(qm/pm, ratio, places=11)

    def test_policy_still_changes_future_divergence(self):
        p, q, phi0 = rare_action(0)
        _, _, phi1 = rare_action(1)
        self.assertAlmostEqual(backward_power(p, q, phi0, 2, .5), 1)
        self.assertLess(backward_power(p, q, phi1, 2, .5), .9)

    def test_final_action_does_not_change_full_transcript_power(self):
        p, q, phi = controlled()
        other = lambda t, h, x: 1-phi(t, h, x) if t == 3 else phi(t, h, x)
        self.assertAlmostEqual(backward_power(p, q, phi, 3, .3), backward_power(p, q, other, 3, .3))

    def test_deterministic_policy_support(self):
        p, q, _ = controlled()
        phi = lambda t, h, x: float(x)
        masses = prefix_laws(p, q, phi, 3)[-1]
        self.assertEqual(len(masses), 8)
        self.assertTrue(all(all(a == x for x, a in h) for h in masses))
        self.assertAlmostEqual(backward_power(p, q, phi, 3, .5), path_power(masses, .5))

    def test_predictable_unbiasedness(self):
        for lam in (.25, .5, .75):
            masses, values = predictable_values(*controlled(), 3, lam)
            mean, _ = mixture_moments(masses, values)
            self.assertAlmostEqual(mean, 1-path_power(masses, lam), places=12)
            self.assertGreaterEqual(min(values.values()), -1e-12)

    def test_conditional_remaining_gain(self):
        p, q, phi = controlled()
        lam, horizon = .4, 3
        levels = prefix_laws(p, q, phi, horizon)
        for level in levels[:-1]:
            for h, (pm, qm) in level.items():
                omega = qm/(pm+qm)
                theoretical = 2*omega**lam*(1-omega)**(1-lam)*(1-backward_power(p, q, phi, horizon, lam, h))
                direct = 0.0
                for full, (pfull, qfull) in levels[-1].items():
                    if full[:len(h)] == h:
                        tail = sum(increment(p, q, levels, full[:i], lam) for i in range(len(h), horizon))
                        direct += (pfull+qfull)/(pm+qm)*tail
                self.assertAlmostEqual(direct, theoretical, places=12)

    def test_conditional_second_moment_bound(self):
        p, q, phi = controlled()
        lam = .5
        levels = prefix_laws(p, q, phi, 3)
        masses, values = predictable_values(p, q, phi, 3, lam)
        mean, second = mixture_moments(masses, values)
        gains = []
        for level in levels[:-1]:
            for h, (pm, qm) in level.items():
                omega = qm/(pm+qm)
                gains.append(2*math.sqrt(omega*(1-omega))*(1-backward_power(p, q, phi, 3, lam, h)))
        k = max(gains)/mean
        self.assertLessEqual(second, 2*k*mean**2+1e-12)

    def test_rare_action_second_moment(self):
        for tau in (.1, .01, .001):
            for lam in (.25, .5, .75):
                with self.subTest(tau=tau, lam=lam):
                    masses, values = predictable_values(*rare_action(tau), 2, lam)
                    mean, second = mixture_moments(masses, values)
                    d = 1-power_integral([.25, .75], [.75, .25], lam)
                    self.assertAlmostEqual(mean, tau*d, places=12)
                    self.assertAlmostEqual(second/mean**2, 1/tau, places=7)
                    self.assertTrue(all(1/3-1e-12 <= qm/pm <= 3+1e-12 for pm, qm in masses.values()))

    def test_rare_action_integration_is_exact(self):
        tau = .001
        p, q, phi = rare_action(tau)
        d = 1-power_integral([.25, .75], [.75, .25], .5)
        integrated = tau*d
        self.assertAlmostEqual(integrated, 1-backward_power(p, q, phi, 2, .5), places=12)

    def test_prefix_tilt_identity(self):
        p, q, phi = controlled()
        levels = prefix_laws(p, q, phi, 3)
        lam = .35
        for t in range(1, 4):
            before = path_power(levels[t-1], lam)
            average = sum(qm**lam*pm**(1-lam)/before*power_integral(q(t, h), p(t, h), lam)
                          for h, (pm, qm) in levels[t-1].items())
            self.assertAlmostEqual(path_power(levels[t], lam), before*average, places=12)

    def test_randomised_branch_selection_identity(self):
        p, q, kappa = [.2, .3, .5], [.5, .2, .3], [.1, .7, .9]
        rp, rq = sum(pi*k for pi, k in zip(p, kappa)), sum(qi*k for qi, k in zip(q, kappa))
        for lam in (.3, .5, .7):
            z = power_integral(q, p, lam)
            rt = sum(qi**lam*pi**(1-lam)*k for pi, qi, k in zip(p, q, kappa))/z
            selected = power_integral([qi*k/rq for qi, k in zip(q, kappa)], [pi*k/rp for pi, k in zip(p, kappa)], lam)
            self.assertAlmostEqual(selected, z*rt/(rq**lam*rp**(1-lam)), places=12)

    def test_same_data_reuse_has_no_new_transcript_divergence(self):
        def p(t, h):
            return [.2, .8] if t == 1 else [float(h[0][0] == 0), float(h[0][0] == 1)]
        def q(t, h):
            return [.6, .4] if t == 1 else p(t, h)
        phi = controlled()[2]
        self.assertAlmostEqual(backward_power(p, q, phi, 3, .4), power_integral([.6, .4], [.2, .8], .4))

    def test_action_projection_is_not_transcript_divergence(self):
        p, q, _ = controlled()
        masses = prefix_laws(p, q, lambda t, h, x: .5, 2)[-1]
        grouped = defaultdict(lambda: [0.0, 0.0])
        for h, (pm, qm) in masses.items():
            key = tuple(a for _, a in h)
            grouped[key][0] += pm
            grouped[key][1] += qm
        projected = power_integral([v[1] for v in grouped.values()], [v[0] for v in grouped.values()], .5)
        self.assertAlmostEqual(projected, 1)
        self.assertLess(path_power(masses, .5), projected)

    def test_zero_reach_is_not_queried(self):
        def kernel(t, h):
            if any(x != 1 or a != 0 for x, a in h):
                raise AssertionError("An unreachable history was queried")
            return [0., 1.]
        phi = lambda t, h, x: 0.
        self.assertEqual(len(prefix_laws(kernel, kernel, phi, 3)[-1]), 1)
        self.assertEqual(backward_power(kernel, kernel, phi, 3, .5), 1)

    def test_one_model_zero_reach_is_not_queried(self):
        def p(t, h):
            if h and h[0][0] != 0:
                raise AssertionError("P queried off support")
            return [1., 0.]
        def q(t, h):
            if h and h[0][0] != 1:
                raise AssertionError("Q queried off support")
            return [0., 1.]
        phi = lambda t, h, x: 0.
        masses, values = predictable_values(p, q, phi, 2, .5)
        self.assertEqual(path_power(masses, .5), 0)
        self.assertEqual(mixture_moments(masses, values), (1., 1.))
        self.assertEqual(backward_power(p, q, phi, 2, .5), 0)

    def test_finite_state_recursion(self):
        p = lambda t, s: [.3+.1*s, .7-.1*s]
        q = lambda t, s: [.6-.1*s, .4+.1*s]
        phi = lambda t, s, x: .2+.5*x
        state = lambda h: h[-1][1] if h else 0
        direct = backward_power(lambda t, h: p(t, state(h)), lambda t, h: q(t, state(h)),
                                lambda t, h, x: phi(t, state(h), x), 4, .4)
        compressed = finite_state_power([[0]]+[[0, 1]]*4, 0, p, q, phi, lambda t, s, x, a: a, .4)
        self.assertAlmostEqual(compressed, direct, places=12)

    def test_equal_models_give_zero_estimator(self):
        p, _, phi = controlled()
        masses, values = predictable_values(p, p, phi, 3, .5)
        self.assertEqual(mixture_moments(masses, values), (0., 0.))

    def test_sample_value_matches_enumerated_path(self):
        model = controlled()
        masses, values = predictable_values(*model, 3, .5)
        for seed in range(12):
            value, h = sample_gap(*model, 3, .5, random.Random(seed))
            self.assertIn(h, masses)
            self.assertAlmostEqual(value, values[h], places=12)

    def test_sampler_rejects_mismatched_support(self):
        with self.assertRaises(ValueError):
            sample_gap(lambda t, h: [1., 0.], lambda t, h: [0., 1.], lambda t, h, x: 0., 1, .5, random.Random(0))

    def test_support_above_one_has_correct_orientation(self):
        self.assertTrue(math.isinf(divergence([1., 0.], [0., 1.], 2)))
        self.assertAlmostEqual(divergence([1., 0.], [.5, .5], 2), math.log(2))
        self.assertTrue(math.isinf(divergence([.5, .5], [1., 0.], 2)))

    def test_invalid_inputs(self):
        for lam in (0, 1, -1, math.inf, math.nan):
            with self.assertRaises(ValueError):
                power_integral([.5, .5], [.5, .5], lam)
        with self.assertRaises(ValueError):
            power_integral([.2, .2], [.5, .5], .5)
        with self.assertRaises(ValueError):
            prefix_laws(*controlled()[:2], lambda t, h, x: 1.1, 1)
        with self.assertRaises(ValueError):
            backward_power(*controlled(), 2, 2)

    def test_coupled_parameter_cannot_be_optimised_locally(self):
        fair, biased, lam = [.5, .5], [.9, .1], .5
        z = power_integral(fair, biased, lam)
        coupled_h = max(1*z, z*1)
        rectangular_h = max(1, z)*max(1, z)
        self.assertGreater(math.log(coupled_h)/(lam-1), 0)
        self.assertEqual(math.log(rectangular_h)/(lam-1), 0)

    def test_truth_map_is_fixed_across_histories_at_same_node(self):
        # A_1=0 reaches one node; X_1 is fair, and A_2=X_1.
        fixed = max(sum(.5*(x != truth) for x in (0, 1)) for truth in (0, 1))
        history_dependent = sum(.5*max(x != truth for truth in (0, 1)) for x in (0, 1))
        self.assertEqual(fixed, .5)
        self.assertEqual(history_dependent, 1)

    def test_invalid_horizons(self):
        for horizon in (-1, 1.5, True):
            for operation in (
                lambda: prefix_laws(*controlled(), horizon),
                lambda: backward_power(*controlled(), horizon, .5),
                lambda: sample_gap(*controlled(), horizon, .5, random.Random(0)),
            ):
                with self.assertRaises(ValueError):
                    operation()

    def test_relative_gap_conversion_above_one(self):
        for gap in (1e-6, .1, 1, 100):
            for factor in (.9, 1.1):
                self.assertLessEqual(abs(math.log1p(factor*gap)/math.log1p(gap)-1), .1+1e-12)

    def test_below_one_gap_promise_conversion(self):
        gamma, eps = .8, .1
        eta = eps*(1-gamma)/2
        for gap in (1e-6, .1, .5, gamma):
            for factor in (1-eta, 1+eta):
                self.assertLessEqual(abs(math.log1p(-factor*gap)/math.log1p(-gap)-1), eps)


if __name__ == '__main__':
    unittest.main()
