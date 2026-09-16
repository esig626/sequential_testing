# Current research status

Date: 16 September 2026.

The repository is a research workspace for finite-sample sequential composite testing when reported local decisions select future experiments. The authoritative starting scientific files remain `manuscript/sequential_testing.tex` and `manuscript/RELATION_TO_PARALLEL_HYPOTHESIS.md`.

The mandatory research ledger is `docs/RESEARCH_LEDGER.md`. Its ultimate question `UQ001` is how nodewise Type I and Type II error tradeoffs propagate into global sequential error. `SB001` records the isolated iid single-node finite-sample composite problem as solved prior work that must not be rederived.

## Literature status

The Xing SS-2025-0042 audit established that controlled sensing, adaptive observations, composite controlled sensing, non-iid sequential testing, controlled Markov observations and nonlinear information clocks are all established neighbouring areas. No direct theorem was located for the complete model in this repository; this remains `NO DIRECT MATCH LOCATED`, not a novelty claim.

A second targeted audit has now been completed for the exact two-node singleton bottleneck exposed by `R026`. The result materially changes the research plan:

* the logarithmic branch-selected tilted expectation in `R026` is exactly the established **common-input conditional Rényi divergence**;
* Polyanskiy and Wu give the exact Rényi chain rule for arbitrary joint laws, with the conditional term evaluated under a Rényi-tilted marginal;
* iterating that identity gives an exact dependent-path chain decomposition using tilted prefix laws;
* therefore non-iid dependence does **not** create an unsolved divergence algebra problem, although ordinary tensorisation is lost.

Detailed audit: `notes/2026-09-16_conditional_renyi_chain_rule_literature_audit.md`.

Source record: `sources/conditional_renyi_chain_rule/SOURCE.md`.

The earlier two-node derivation remains useful as the explicit mapping from this project’s branch-selection notation to the standard chain rule: `notes/2026-09-16_two_node_singleton_renyi_decomposition.md`.

## Revised bottleneck

The previous wording of `O016` treated the dependent future-data term itself as the main unknown. That is now superseded.

The actual next problem is to combine the established conditional Rényi chain rule with the project-specific branch-selection correction and the finite-sample testing converse. In the singleton case, the immediate goal is a recursive finite-sample converse expressed through previous-node error quantities and future conditional Rényi information.

After that, the difficult composite step is to take the pairwise converse over history-dependent composite classes while preserving coherent environment coupling. This is `O017` and directly serves `UQ001`.

The closest checked testing neighbours are informative but do not close this gap:

* Hayashi 2009 treats adaptive discrimination of two simple channels, allows randomised tests, and accumulates Rényi/Hellinger-transform information along adaptive observations, but has one final decision and asymptotic error exponents.
* Bergh, Datta and Salzmann treat composite adaptive channel discrimination, but still require independence even when samples are non-identical, and leave important adaptive composite exponent questions open.
* Han 2000 treats arbitrary dependent general sources in simple asymptotic testing.
* Jacod and Dzhaparidze–Spreij–Valkeila provide filtered Hellinger/information-process frameworks, including randomized filtered experiments, but not the finite-sample nodewise composite error-propagation theorem sought here.

The ledger now records these boundaries through `R032`, `F018`, `M013`, and `O018`.

## Validation

No code was changed in this literature audit, so the earlier 30 local regression tests were not rerun as evidence for this task. No remote CI execution or stochastic performance study is claimed.

The next mathematical focus is `O016`: derive the singleton finite-sample converse recursion using the established conditional Rényi chain rule, without rediscovering that chain rule or the branch-selection correction.
