# Current research status

Date: 24 September 2026.
Branch: `research/non-iid-renyi-literature-audit`.
Audit base: `adc0b7784f61569308f70244bb4e639c1f396415` on `research/selected-renyi-converse-sample-complexity`.

The governing question remains UQ001: how local Type I and Type II errors propagate when reported randomised decisions select future dependent experiments. The controlling document before every material research decision is `docs/RESEARCH_LEDGER.md`. Check its entries and the existing source library before any new search.

## Current milestone: literature on computing and controlling dependent Rényi divergence

The source checked repository review is `sources/non_iid_renyi/REVIEW.md`. Its compiled bibliography is `sources/non_iid_renyi/references.bib`. There are 30 reference records; each records the primary source, relevant result, scope and inspection depth. S29 and S30 are explicitly limited leads. A longer Markdown review, annotated bibliography and structured source record are also supplied as conversation attachments. The repository edition is shorter, not a byte identical copy of that report.

The most directly relevant findings are:

* R045: Watanabe and Hayashi's finite length Markov moment and testing bounds, retaining spectral and initial boundary terms. The report includes an algebraic translation to the selected future moment as a finite matrix product when an observed sufficient state exists.
* R046: Feldman and Zrnic's adaptive Rényi composition under a cumulative conditional budget along paths, including a fixed pair and suitable stopping. This is not a budget only in expectation.
* R047: Kontoyiannis and Meyn's positive operator and multiplicative regularity methods for dependent exponential functionals. Transform domains, drift assumptions and initial integrability must be checked.
* R048: Atar, Chowdhary and Dupuis's exact variational reference infimum for exponential functionals. This is established background for the reference comparison method in R044, not a new general inequality.
* R049 to R052: hidden Markov filtering and rate restrictions; endpoint versus full transcript comparison; finite particle error bounds; and Esposito and Mondelli's finite sample dependence concentration and Hellinger moment methods.

The ledger now extends through R052, F028 and O022. Source results have not been promoted to new project theorem claims. The detailed limitations are in the review and ledger. In particular, an expectation over histories is compatible with finite sample analysis. Finiteness, evaluability, numerical accuracy and uniformity over root tests are separate questions.

The original manuscript, user working notes, production code and previous branch are unchanged by this audit. No branches were merged. This task did not rerun regression tests or perform new numerical experiments. Selected primary theorem statements and assumptions were inspected, not all proofs independently verified. No exhaustive novelty claim is made.

## Current notation

Use `d_{lambda,1}(n,m;phi_0)` for the scalar logarithmic selected tilted average that the 16 September note called `T_{lambda,1}`. Do not also use `d_{lambda,1}(x)` for the pointwise conditional divergence. Write the pointwise divergence explicitly. Root laws are P_0^(tensor n), Q_0^(tensor n) in the current calculation. Every new symbol must be defined before use. Preserve the user's uploaded working notes.

## Preserved earlier milestones

SB001/R025 record the prior isolated iid composite testing theory. R026 to R029 give the selected decomposition and its identification with the established conditional Rényi chain rule. R033 to R037 contain the source converse substitution, survival cancellation, restricted path converse and necessary sample size relationships under stated information assumptions. The earlier note remains `notes/2026-09-16_selected_renyi_converse_sample_complexity.md`, with source records under `sources/2608.28068/` and historical validation under `results/2026-09-16_selected_converse_checks.json`.

The 23 September note `notes/2026-09-23_nonuniform_selected_information_bounds.md` records R038 to R043. R038 is the higher moment Hölder bound, R039 the local integral comparison construction, R040 the Gaussian feedback example, R041 the obstruction to uniformity over all root tests with only a Type I budget, R042 the coherent prefix monotonicity statement, and R043 the root power lower bound on tilted reach. These remain derived and not independently reviewed. Fifteen standalone methods were previously checked, not a rerun of the older 47 method suite. That historical record is `results/2026-09-23_nonuniform_information_verification.json`.

R044 and `notes/2026-09-23_projection_assisted_selected_bound.md` record a reference law Hölder comparison. R048 identifies the established risk sensitive variational literature behind this method. A useful reference family and its full objective still require model analysis. No pure projection upper bound is asserted.

The Xing and earlier conditional Rényi audits remain in their existing dated notes and source folders. The old Lei Yu monograph Theorem 8 reference was not freshly verified because the monograph could not be reopened; use the checked Polyanskiy and Wu equations as the present exact chain rule foundation.

## Next permissible work

O022: apply the finite length Markov spectral bounds or the fixed pair adaptive Rényi filter to the selected future experiment. Prove the sufficient observed state or cumulative conditional budget, keep the selected initial law and finite length correction, and only then insert the resulting upper information bound into the existing converse.

For unbounded state models, continue O020/O021 using R047/R048 and their explicit assumptions. Do not replace these tasks with another broad search, rederive SB001, or claim a limiting rate or endpoint bound controls the full finite retained record without proof. A sample size excluded by a converse is impossible; the first size not excluded is not thereby sufficient. Exact composite minimax sample complexity and matching achievability remain separate objectives.
