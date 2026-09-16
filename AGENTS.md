# Research instructions

Read `manuscript/sequential_testing.tex`, `manuscript/RELATION_TO_PARALLEL_HYPOTHESIS.md`, `CURRENT_STATUS.md`, `docs/RESEARCH_LEDGER.md`, `docs/NOTATION.md`, `docs/RENYI_APPROXIMATION_PLAN.md`, and `docs/CLAIMS.md` before scientific work.

## Mandatory research ledger

`docs/RESEARCH_LEDGER.md` is compulsory reading before every scientific task, including derivations, literature searches, theorem drafting, numerical experiments, code changes motivated by research, and manuscript development.

Before doing new work, identify the ledger IDs that overlap the task. Do not rederive, recode, or relitigate an existing result or failed route unless the task explicitly calls for independent verification, correction, strengthening, or generalisation. If a listed counterexample already rules out the proposed route under the same assumptions, change the assumptions explicitly or choose another route.

Every substantive research task must update the ledger before it is declared complete. Results, failures, and counterexamples are never deleted merely because later work supersedes them; mark them `SUPERSEDED` and point to the replacement. The ledger is an index, so proofs and detailed evidence remain in their authoritative source files.

### Solved single-node base case

Ledger entry `SB001` is mandatory. The isolated iid single-node composite binary testing problem is already solved in Vera Sigüenza and Esposito, *Finite Sample Bounds for Composite Hypothesis Testing*. Do not treat its finite-sample achievability or converse theory as an open task, do not spend research time rederiving `beta_n^star`, and do not search for a particular test merely for its own sake. Use the prior theorem as nodewise input whenever its assumptions hold. Work on a local node is permitted only when a sequential, conditional, dependence, or model assumption genuinely changes the prior problem, and the task must state exactly what changed. The primary unresolved target is `UQ001`: how the local errors propagate through the action-selected sequential path.

## Preserve the model

Use lambda for Rényi order and D_lambda(Q||P), with q raised to lambda. Alpha_t and beta_t are local testing errors. A_t is the selected edge, not a Monte Carlo estimator. Keep the original notation and the observed history including actions.

The setting is new data whose future law can depend on decisions. Keep Parallel-Hypothesis separate. Do not replace the observed path law by a law including hidden states, model labels or unrevealed random seeds. The simulation label is not the correct edge.

Evaluate both models under the same specified policy. Common action kernels cancel in a path likelihood ratio but still affect future histories. A different policy comparison requires its own formula.

Use unnormalised masses at zero reach. Do not query conditional laws of an absent model as though they were intrinsic. Never smooth exact support, clip an invalid estimate into a success claim, or infer support equality from sampled paths.

Distinguish conditional kernels that can be chosen independently across histories from a shared parameter or latent environment. The truth map vartheta(v) is fixed across histories reaching the same node, even when kernels are rectangular. Do not move a supremum over that map inside each history update without justification.

Keep pairwise divergence, composite separation, local testing errors and probability of any wrong edge distinct. Do not multiply marginal correctness probabilities or identify a terminal testing error with path risk.

## Evidence and computation

Read the relevant prompt before implementation. Keep proofs, numerical checks, conjectures and literature results separate. No general dependent variance bound, linear horizon algorithm or globally optimal policy is currently established. Do not claim the elementary predictable identities are novel without a literature audit.

Count filtering, conditional evaluation, policy evaluation, sampling, state construction, branch integration and numerical precision costs. A full decision tree can be exponential in the horizon. Preserve the rare action counterexample and both uncertainty consistency examples.

Run `python -m unittest discover -s tests -v` after code changes and add a regression test for each confirmed defect. Record all model probabilities, policy, truth map restrictions, order, horizon, method, seed when relevant, sample count, runtime, error criterion, software version and commit for experiments. Separate statistical, numerical, model approximation and optimisation error.

## Publication and files

The recovery workspace was added to main at the owner's request. Use a descriptive research branch for subsequent substantive tasks, unless instructed otherwise. Do not force push, rewrite unrelated history or merge without instruction. Publish completed milestones with `CURRENT_STATUS.md` and `results/checkpoint.json`; do not leave the only copy in a temporary workspace.

The original scientific files remain authoritative. Put proposed corrections in a dated note before altering the manuscript's model or notation. Do not silently change assumptions to obtain a theorem. Update `docs/CLAIMS.md` when a claim changes status, and keep `docs/RESEARCH_LEDGER.md` consistent with it.

Use primary sources and record reading depth. The motivating article is linked, not mirrored. Do not upload third party full texts without appropriate permission, credentials, private correspondence or unrelated personal context. Do not choose a project licence without the owner's decision.
