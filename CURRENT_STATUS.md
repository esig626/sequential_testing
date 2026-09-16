# Current research status

Date: 16 September 2026.

The repository has been prepared as a research workspace without changing `manuscript/sequential_testing.tex` or `manuscript/RELATION_TO_PARALLEL_HYPOTHESIS.md`. The starting scientific commit was `a7765a057b1879dc12a3fc66359e5f2b9a52ebd8`.

Completed so far: repository and article reading; an adapted Rényi approximation plan; a notation register; working controlled identities; a claims register; a mandatory research ledger; finite reference code; 30 previously passing local test methods; source records; and a first executable research task.

A new literature audit has now been completed on branch `research/xing-2025-literature-audit`. Yiming Xing's newly accepted Statistica Sinica paper SS-2025-0042 and its supplement were read directly. The audit then searched the neighbouring literatures on active sequential hypothesis testing, controlled sensing, composite controlled sensing, controlled Markov observations, non iid and dependent sequential testing, finite sample active testing, and Rényi divergence for hidden Markov models.

The main literature consequence is a sharper novelty boundary. Action dependent future observations, adaptive sensing, composite controlled sensing, temporal dependence, and controlled Markov memory are all established ingredients. They must not be claimed as novel in isolation. The targeted search did not locate a theorem matching the complete combination in this repository: successive local composite binary decisions where each reported edge decision is also the action selecting the next experiment, with history dependent future classes, fixed node truth semantics, coherent uncertainty across the tree, pathwise wrong edge risk, and finite sample Rényi analysis. This is recorded only as `NO DIRECT MATCH LOCATED`, not as a novelty claim.

The most useful import from Xing is the general information function viewpoint: asymptotic information need not grow linearly in sample count. A future controlled theory should define the relevant policy and environment dependent information clock before specialising to a linear rate. A second important import is the separation between assumptions needed for validity and stronger assumptions needed for expected stopping time optimality. A third is the use of coherent rare event importance sampling for calibrating very small sequential error probabilities.

Detailed synthesis: `notes/2026-09-16_xing_2025_and_controlled_testing_literature_audit.md`.

Source record: `sources/SS-2025-0042/SOURCE.md`.

The ledger also records `SB001`: the isolated iid single-node finite-sample composite binary testing problem is a solved base case from the prior Vera Sigüenza and Esposito paper *Finite Sample Bounds for Composite Hypothesis Testing*. Its local achievability and converse theory must be imported rather than rederived. The new project begins with what changes once those local error guarantees live on an action-selected, history-dependent sequential path, and ultimately with how the local errors propagate.

A first explicit two-node singleton calculation has now been recorded as `R026`. Conditional on reaching branch `A_0=1`, the Rényi divergence between the selected joint laws of the old and new data decomposes exactly into three pieces: the original node-0 Rényi divergence; the already familiar branch-selection correction involving `alpha_0`, `beta_0`, and the tilted branch reach; and a genuinely dependent new-data contribution given by the logarithm of a branch-selected tilted expectation of the conditional Rényi integral. No iid or independence assumption is used for the new block. The derivation is in `notes/2026-09-16_two_node_singleton_renyi_decomposition.md` and is currently unreviewed and not numerically checked.

The main bottleneck exposed by `R026` is now `O016`: characterise or bound the dependent new-data term, understand how it iterates across further nodes, and then lift the singleton identity to composite converse bounds. The branch-selection correction itself is already covered by `R005` and must not be rediscovered.

The research ledger has therefore been expanded through R026, F017, M011 and O016, in addition to `SB001`. Any subsequent research must use these entries rather than rediscover the single-node composite theory, the controlled sensing literature, the branch-selection correction, or novelty claims ruled out by the audit.

The repository's own new derivations have still not received independent mathematical review. The useful model specific variance bound, a general approximation algorithm, uniform sequential composite guarantees, policy optimisation, the connection from nodewise guarantees to path risk, the dependent new-data bottleneck, and a theorem level novelty audit remain research tasks.

The next mathematical focus should start from `R026` and `O016`: analyse the branch-selected tilted conditional Rényi term before returning to broader approximation machinery. Any work on local iid error bounds must first check `SB001`, and future policy work must distinguish the repository's reported decision as control from the separate sensing actions used in standard active hypothesis testing.

Validation details remain in `results/VALIDATION.md`. No code was changed in the literature audit, the `SB001` clarification, or the `R026` algebraic derivation, so the earlier 30 passing local tests were not rerun as evidence for these tasks. No remote CI execution or stochastic performance study is claimed.
