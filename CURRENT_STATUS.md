# Current research status

Date: 16 September 2026.
Current branch: `research/selected-renyi-converse-sample-complexity`.
Branch base: `f7e6dab50b296b1a0f9faf21b6cb1a18911e2c92` on `research/xing-2025-literature-audit`.

The repository studies how local Type I and Type II errors propagate when each reported randomised decision selects the next dependent experiment. The governing question remains UQ001. The original `manuscript/sequential_testing.tex` and `manuscript/RELATION_TO_PARALLEL_HYPOTHESIS.md` have not been changed by this task.

## Current milestone: converse substitution and necessary sample counts

The exact uploaded source was read: Vera-Sigüenza and Esposito, *Finite Sample Bounds for Composite Hypothesis Testing*, arXiv:2608.28068v1. Theorem 1 equation (4), Appendix A-A, and equation (48) provide the two converse directions used here. A dedicated versioned source record and bibliography now live in `sources/2608.28068/`. The online version record was checked, but the later version was not silently substituted for the upload.

The new derivation is `notes/2026-09-16_selected_renyi_converse_sample_complexity.md`. It records:

* R033: explicit substitution of the selected joint Rényi expression into both source converses, with the first rule fixed and the correct tilt in each direction;
* R034: conversion to the (1,1) path error and cancellation of the explicit alternative branch survival factor;
* R035: a converse for successive all ones decisions under a coherent null comparison and uniform conditional information limits;
* R036: necessary sample size inversions in n and m, including the limited coherent pair implication for composite risk;
* R037: an explicit correlated Gaussian model with dependence within both blocks and across them, a closed form order optimisation, and a necessary sample count example.

These are derived results with finite checks, NOT independently reviewed theorems or novelty claims. The sample counts are necessary conditions, not sufficient counts. This is converse work only. General truth maps, exact composite minimax tradeoffs, optimal policy design and matching achievability remain unresolved here.

The main useful cancellation is that beta_0+(1-beta_0)beta_1 removes the explicit division by 1-beta_0 in the selected local converse. The first decision still affects its actual alpha_0, the tilted branch reach, and the conditional information. Uniform upper information limits allow a bound independent of the particular first test; ordinary average divergence does not provide such an upper limit when lambda>1.

The root is indexed zero in this calculation. Z_t denotes the past before node t; h remains reserved for the log likelihood ratio. The composite class notation is C_t^(0), C_t^(1). The amendment in `docs/NOTATION.md` records the user approved changes while retaining the old manuscript conventions for historical reference.

## Validation

`python -m unittest discover -s tests -v` passed all 47 methods locally under Python 3.13.5: the 30 existing methods plus 17 new ones. Existing source and test files were verified against their Git blob hashes before running. No production source file was changed.

The new checks cover selected normalisation, genuine conditional dependence, both divergence orientations, source converse substitution against exact finite NP errors, survival cancellation, uniform information limits, a four stage path bound, zero reach, the repeated observation obstruction, invalid average information substitution, the opposite direction budget error, covariance inversion, and the Gaussian count calculation.

Validation record and file hashes: `results/2026-09-16_selected_converse_checks.json`.
No independent mathematical review, remote CI run or broad stochastic performance study is claimed.

## What was already available and remains an input

SB001/R025 record the original isolated iid composite testing theory as solved prior work. R026 is the two node selected Rényi decomposition. R027 to R029 identify its conditional term and chain rule as established literature. None was presented as a new theorem in this task.

The earlier Xing audit and conditional Rényi audit remain in their dated notes and in `sources/SS-2025-0042/` and `sources/conditional_renyi_chain_rule/`. Controlled sensing, composite controlled testing, temporal dependence, Markov memory and nonlinear information accumulation remain established neighbouring literature. The previous targeted searches found no exact match to the complete project formulation; that is not a novelty proof for the present results.

## Research protocol and next decision

`docs/RESEARCH_LEDGER.md` remains the controlling document before every material research decision. Inspect its entries and the existing source library before any new search. Newly useful references and failures must be recorded immediately rather than retained only in chat.

The ledger now extends through R037, F021, M014 and O019. O016 and O017 are partially answered within the precise scopes above. Next: independently review the new derivation and sharpen the necessary counts by retaining the selected tilted reach, checking root reliability, and comparing with exact selected experiment errors. Start from R033 to R037 and O019; do not redo the source converse, the chain rule or the initial substitution. A matching achievability analysis has not been requested in this task.
