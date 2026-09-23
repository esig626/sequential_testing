# Current research status

Date: 23 September 2026.
Branch: `research/selected-renyi-converse-sample-complexity`.
This task started from `1409d7af0c4b33d98fcec73bb54eb53fec54e910`.

The governing question remains UQ001: how local Type I and Type II errors propagate when reported randomised decisions select future dependent experiments. The controlling document before every material research decision is `docs/RESEARCH_LEDGER.md`. Check its entries and the existing source library before any new search.

## Current milestone: bounds without a uniform cap over histories

New note: `notes/2026-09-23_nonuniform_selected_information_bounds.md`.

R038 constructs a general upper bound using generalised Holder and averaged higher order moments of each conditional observation likelihood ratio. These averages preserve dependence on the old data and the new prefix. No iid assumption or uniform history cap is imposed. Finiteness of the specified higher moments is sufficient, not necessary; the bound is not automatically efficient to evaluate.

R039 gives a local integral comparison form of the existing backward moment recursion, at the original order above one. Functions that satisfy the stated one observation integral inequalities dominate the remaining moment. They may be unbounded if their initial selected average is finite. This is a constructive condition to verify from the kernels, not an assertion that suitable finite functions exist in every model.

R040 solves the conditional moment recursion in an illustrative Gaussian feedback model with distinct autoregression coefficients. Its conditional divergences are unbounded over histories, unlike the constant conditional divergence example R037. Yet the selected contribution and an explicit bound containing n and m can be finite. The scalar quadratic recursion, Gaussian integrability thresholds, and first test dependence are retained.

R041 proves a limitation on uniformity over first tests: for fixed kernels, taking the supremum over every positive reach first test satisfying only the Type I upper budget recovers the least bound on the pointwise conditional divergence outside a null set for the root tilt. A finite bound for one first test need not be uniform over all of them.

R042 records monotonicity in the number of new observations only for a coherent prefix process with n and the first rule fixed. R043 gives the elementary lower tilted reach bound from actual root power, which can be used when a lower power requirement is imposed.

The ledger now extends through R043, F024, M016 and O020. New claims are derived and not independently reviewed. Standard Holder inequalities, Gaussian integration, the chain rule and the original backward recursion are not claimed as novel.

## Current notation

The user now writes `d_{lambda,1}(n,m;phi_0)` for the scalar logarithmic selected tilted average that the 16 September note called `T_{lambda,1}`. Do not also use `d_{lambda,1}(x)` for pointwise conditional divergence. Write the pointwise divergence explicitly. Root laws are P_0^(tensor n), Q_0^(tensor n) in the current calculation. Every new symbol must be defined before use. The uploaded working notes were deliberately left unchanged.

## Validation and source reading

Fifteen standalone local deterministic methods passed under Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. They check finite dependent enumeration, Holder weights, exact forward and backward recursions, the Gaussian recursion against full joint Gaussian integration, selected Gaussian bounds and the stated obstructions. They do not constitute a rerun of the old 47 method suite. No production code, original manuscript or user note was changed.

Record: `results/2026-09-23_nonuniform_information_verification.json`. A complete standalone verification script and an extended derivation were also supplied as a conversation attachment. No remote CI, independent mathematical review or stochastic performance claim is made.

The existing Polyanskiy and Wu reference was checked directly at equations (7.77) and (7.78), using parsed primary source text. Screenshot fetches failed. This was a targeted verification after reading the source library, not a new broad literature survey. See `sources/conditional_renyi_chain_rule/VERIFICATION_2026-09-23.md`. No third party full text was mirrored.

## Preserved earlier milestones

SB001/R025 record the prior isolated iid composite testing theory. R026 to R029 give the selected decomposition and its identification with the established conditional Renyi chain rule. R033 to R037 contain the source converse substitution, survival cancellation, restricted path converse and necessary sample size relationships under stated information assumptions. The full earlier note remains `notes/2026-09-16_selected_renyi_converse_sample_complexity.md`, with source records under `sources/2608.28068/` and the historical validation under `results/2026-09-16_selected_converse_checks.json`.

The Xing and conditional Renyi literature audits remain in their existing dated notes and source folders. No new claim that the complete project problem is absent from the literature is made.

## Next permissible work

Start from O020 and the new note. Review the moment construction, choose a specified model or integrability condition, and connect the nonuniform bound back to the existing converse while preserving the actual first test or justified root power restrictions. Do not replace this task by rederiving the uniform cap implication, the chain rule, or SB001.

A universal finite bound depending on counts alone is ruled out by the stated examples. Exact composite minimax sample complexity, arbitrary optimal policies and matching achievability are not established by this task.
