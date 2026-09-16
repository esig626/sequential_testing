# Current research status

Date: 16 September 2026.

The repository has been prepared as a research workspace without changing `manuscript/sequential_testing.tex` or `manuscript/RELATION_TO_PARALLEL_HYPOTHESIS.md`. The starting scientific commit was `a7765a057b1879dc12a3fc66359e5f2b9a52ebd8`.

Completed so far: repository and article reading; an adapted Rényi approximation plan; a notation register; working controlled identities; a claims register; a mandatory research ledger; finite reference code; 30 previously passing local test methods; source records; and a first executable research task.

A new literature audit has now been completed on branch `research/xing-2025-literature-audit`. Yiming Xing's newly accepted Statistica Sinica paper SS-2025-0042 and its supplement were read directly. The audit then searched the neighbouring literatures on active sequential hypothesis testing, controlled sensing, composite controlled sensing, controlled Markov observations, non iid and dependent sequential testing, finite sample active testing, and Rényi divergence for hidden Markov models.

The main literature consequence is a sharper novelty boundary. Action dependent future observations, adaptive sensing, composite controlled sensing, temporal dependence, and controlled Markov memory are all established ingredients. They must not be claimed as novel in isolation. The targeted search did not locate a theorem matching the complete combination in this repository: successive local composite binary decisions where each reported edge decision is also the action selecting the next experiment, with history dependent future classes, fixed node truth semantics, coherent uncertainty across the tree, pathwise wrong edge risk, and finite sample Rényi analysis. This is recorded only as `NO DIRECT MATCH LOCATED`, not as a novelty claim.

The most useful import from Xing is the general information function viewpoint: asymptotic information need not grow linearly in sample count. A future controlled theory should define the relevant policy and environment dependent information clock before specialising to a linear rate. A second important import is the separation between assumptions needed for validity and stronger assumptions needed for expected stopping time optimality. A third is the use of coherent rare event importance sampling for calibrating very small sequential error probabilities.

Detailed synthesis: `notes/2026-09-16_xing_2025_and_controlled_testing_literature_audit.md`.

Source record: `sources/SS-2025-0042/SOURCE.md`.

The research ledger has been expanded through R024, F016, M011 and O015. Any subsequent research must use these entries rather than rediscover the controlled sensing literature or repeat novelty claims ruled out by the audit.

The repository's own new derivations have still not received independent mathematical review. The useful model specific variance bound, a general approximation algorithm, uniform composite guarantees, policy optimisation, the connection from pairwise Rényi quantities to path risk, and a theorem level novelty audit remain research tasks.

The next executable technical task remains `prompts/01_controlled_renyi_foundations.md`, but its literature stage must now start from R014 to R024 and F011 to F016. In particular, future policy work must distinguish the repository's reported decision as control from the separate sensing actions used in standard active hypothesis testing.

Validation details remain in `results/VALIDATION.md`. No code was changed in this literature audit, so the earlier 30 passing local tests were not rerun as evidence for this task. No remote CI execution or stochastic performance study is claimed.
