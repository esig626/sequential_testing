# Research ledger

Date created: 16 September 2026.

This file is the persistent do-not-duplicate index for `esig626/sequential_testing`. Every scientific task must read it before derivation, literature search, coding, numerical work, theorem drafting, or manuscript changes.

## Mandatory use

1. Read this file in full before scientific work.
2. Identify overlapping IDs before starting.
3. Do not rederive an existing result unless the task explicitly requests verification, correction, strengthening, or generalisation.
4. Do not repeat a failed route under the same assumptions.
5. State which existing ID is being extended and what is genuinely new.
6. Update this ledger before a substantive research task is declared complete.
7. Never delete superseded or failed work. Mark it `SUPERSEDED` and point to the replacement.

### Permanent decision protocol for Codex

This ledger is the controlling research document, not a document to read once and forget. Codex must return to `docs/RESEARCH_LEDGER.md` before every material research decision, including before choosing a proof strategy, beginning a derivation, claiming a result is open, starting an experiment, adding a model class, changing the manuscript, or launching a literature search. The purpose is to prevent repeated reasoning, repeated code, repeated failed routes, and repeated searches.

Before any external literature search, Codex must first inspect the repository's existing source library. At minimum it must check:

* `sources/README.md`;
* `sources/references.bib`;
* relevant topic-specific bibliographies such as `sources/*/references.bib`;
* relevant `sources/*/SOURCE.md` records;
* literature-audit notes and authoritative locations cited by overlapping ledger entries;
* repository search results for the relevant author, theorem, concept, formula, and keywords.

If the source repository already contains the relevant result, Codex must use it rather than repeat the web search. A new external search is allowed only when a specific gap remains, when the recorded source needs verification or updating, when the task explicitly asks for a fresh search, or when the proposed work genuinely goes beyond what is already recorded. Before searching externally, Codex must state which ledger IDs and source records were checked and what unresolved gap justifies the search.

After any useful external search, the task is not complete until the new source and its contribution are recorded in `sources/` and in this ledger. Record bibliographic details, reading depth, relevant theorem/section, what the source actually solves, what it does not solve, and the exact relation to an existing ledger ID. Do not leave useful prior art only in chat, browser history, or a temporary research workspace.

The required research loop is therefore:

`LEDGER -> EXISTING SOURCES -> DECISION -> NEW WORK ONLY IF NEEDED -> RECORD RESULT/SOURCE -> LEDGER`.

If Codex cannot identify what is genuinely new after this loop, it must stop rather than manufacture a new task. Token saving is a research requirement, not merely a convenience.

## Ultimate research question

### UQ001 — How do the errors propagate?

At every reachable node, the primary object is the local composite testing error tradeoff. Under the user's approved zero based indexing, the root is V_0 and Z_t is the observed past BEFORE node t. Thus Z_0 is empty and Z_1=(X_0^n,A_0). Write the local optimal error as beta_t^star(epsilon_t | Z_t). The symbol h is reserved for the log likelihood ratio and must not be used for history. Composite classes retain C with node subscript and hypothesis superscript: C_t^(0) and C_t^(1). See the amendment in `docs/NOTATION.md`.

The ultimate goal is to understand how the nodewise Type I and Type II errors propagate through the action-selected path when an earlier reported decision changes the future statistical experiment.

We seek both:

* **Achievability:** attainable global sequential error guarantees from attainable nodewise guarantees.
* **Impossibility / converse:** lower bounds on achievable error, or necessary local error performance, valid for every admissible sequence of randomised tests.

A representative global event is making at least one wrong edge by horizon T. Its risk is the expectation of its indicator. Local errors and global path risk must remain distinct. Conditioning only on a selected branch is different from conditioning on the whole realised past; the R033 to R037 calculation uses branch selected joint laws with old data retained.

Rényi quantities, conditional divergences, information clocks, algorithms and policy constructions are tools towards UQ001, not the final objective.

## Solved base cases — do not re-solve

### SB001 — Isolated single-node finite-sample composite binary testing

For iid product data and composite classes `C_0` and `C_1`, the optimal worst-case Type II error under a Type I constraint,

\[
\beta_n^\star(\varepsilon;\mathcal C_0,\mathcal C_1),
\]

is already treated in Vera Sigüenza and Esposito, *Finite Sample Bounds for Composite Hypothesis Testing*. The paper supplies finite-sample achievability and converse bounds. Import this theory. Do not rederive it unless an assumption is explicitly changed or independent verification is requested.

The exact source version used for the current converse work is the user's uploaded arXiv:2608.28068v1, Theorem 1 equation (4), Appendix A-A, and equation (48). See `sources/2608.28068/SOURCE.md` and its bibliography. The arbitrary joint law converse follows by treating the full record as one observation; independence is required for the product simplification, not that reduction. Do not silently change source versions or mistake necessary sample counts for achievable ones.

## Status vocabulary

* `ESTABLISHED`: supported by external literature or an already established theorem under applicable hypotheses.
* `DERIVED — UNREVIEWED`: derived in this repository but not independently checked.
* `CHECKED NUMERICALLY`: finite reference verification only.
* `FAILED / COUNTEREXAMPLE`: false under the stated assumptions.
* `OPEN`: unresolved.
* `SUPERSEDED`: retained but replaced.
* `NO DIRECT MATCH LOCATED`: targeted search found no direct theorem for the stated combination; this is not a novelty claim.

## Results ledger

| ID | Result | Scope / limitation | Status | Authoritative location |
| --- | --- | --- | --- | --- |
| R001 | The controlled path law is generated by history-dependent observation kernels and a common decision policy; the backward quantity `G_t` computes the full path Hellinger integral. | Exact evaluation may still be exponential in history space. | DERIVED — UNREVIEWED | `manuscript/sequential_testing.tex`; controlled identities note |
| R002 | Independent nonidentical observations give additive Rényi divergence. | Genuine product laws only. | ESTABLISHED | van Erven and Harremoës, Theorem 28 |
| R003 | Under the same specified policy in both models, the action kernel cancels from the path likelihood ratio on common positive paths. | Policy still changes future histories and laws. | DERIVED — UNREVIEWED; CHECKED NUMERICALLY | controlled identities note, Section 1 |
| R004 | Prefix Hellinger accumulation is a tilted expectation of the next local Hellinger integral. | Requires positive prefix integral. | DERIVED — UNREVIEWED; CHECKED NUMERICALLY | controlled identities note, Section 2 |
| R005 | Conditioning the current observation on a selected randomised action gives the exact three-probability Rényi correction involving ordinary and tilted branch reaches. | Local selection identity; support conditions matter. | DERIVED — UNREVIEWED; CHECKED NUMERICALLY | controlled identities note, Section 3; Parallel-Hypothesis boundary work |
| R006 | For `0<lambda<1`, the predictable sum estimator has mean `1-H_lambda` under the equal-mixture construction. | Fixed pair and common policy. | DERIVED — UNREVIEWED; CHECKED NUMERICALLY | controlled identities note, Section 4 |
| R007 | Conditional expected remaining predictable gain equals the posterior weight times `1-G_t`. | Fixed pair and valid prefix. | DERIVED — UNREVIEWED; CHECKED NUMERICALLY | controlled identities note, Section 5 |
| R008 | A remaining-gain bound by `K Delta` implies second moment at most `2K Delta^2`. | Conditional lemma; no useful general model-specific `K` supplied. | DERIVED — UNREVIEWED | controlled identities note, Section 5 |
| R009 | A genuinely sufficient observed finite state can replace full histories in the exact backward recursion. | State must determine both models, policy and update. | DERIVED — UNREVIEWED; CHECKED NUMERICALLY | `src/controlled_renyi.py`; C14 |
| R010 | Same-data reuse adds no new full-transcript Rényi information under a common policy, although selection changes conditioned-law divergence. | Boundary case only. | DERIVED — UNREVIEWED; CHECKED NUMERICALLY | relation note; controlled identities note |
| R011 | For a fixed environment, probability of at least one future wrong edge obeys an absorbing backward recursion. | Does not justify moving coupled suprema inside. | DERIVED — UNREVIEWED; CHECKED NUMERICALLY | controlled identities note, Section 8 |
| R012 | Rectangular conditional-kernel uncertainty and globally coupled uncertainty are different optimisation problems. | Fixed truth map remains coupled across histories reaching the same node. | STRUCTURAL RESULT / COUNTEREXAMPLE CHECKED | relation note; research plan |
| R013 | Current finite reference code reproduces path enumeration, backward recursion, predictable identities, support cases and selected counterexamples. | Reference computation only. | CHECKED NUMERICALLY | `results/VALIDATION.md`; `src/`; `tests/` |
| R014 | Xing permits general increasing information functions rather than only `n` times a divergence. | Passive sequential multiple composite testing, not decision-selected future experiments. | ESTABLISHED | Xing SS-2025-0042; Xing audit note |
| R015 | Xing separates assumptions needed for validity from stronger assumptions needed for asymptotic expected-sample-size optimality. | Structural proof-design lesson only. | ESTABLISHED | Xing SS-2025-0042 |
| R016 | Temporal dependence and nonlinear information clocks are already treated in Gaussian, AR(1), and Markov examples. | Passive data mechanism. | ESTABLISHED | Xing supplement |
| R017 | Sequential actions that change future observation laws are classical controlled sensing / active hypothesis testing. | Does not reproduce the present local-decision tree. | ESTABLISHED | Chernoff 1959; Nitinawarat et al. 2013; Naghshvar and Javidi 2013 |
| R018 | Composite hypotheses plus controlled sequential sensing are established. | Sensing action is separate from final hypothesis decision; first-order asymptotics. | ESTABLISHED | Deshmukh, Veeravalli and Bhashyam 2021 |
| R019 | Controlled Markovian observations with causal sensing and sequential risk constraints are established. | Fixed underlying hypothesis; not the present nodewise decision semantics. | ESTABLISHED | Nitinawarat and Veeravalli 2015 |
| R020 | Sequential multiple testing with non-iid or dependent observations exists in several settings. | Earlier local reported decisions do not select the next composite experiment. | ESTABLISHED | Song and Fellouris 2019; Xing and Fellouris 2024; Chaudhuri and Fellouris 2024 |
| R021 | Rényi divergence rates for fixed hidden Markov models admit operator/eigenvalue characterisations. | Long-horizon fixed dependent models. | ESTABLISHED | Fuh et al. 2025 |
| R022 | Finite-sample active hypothesis-testing results exist in some models. | Not the present finite-sample composite pathwise problem. | ESTABLISHED | Kartik et al. 2022; Lin et al. 2026 |
| R023 | Xing gives universal simultaneous-stream misclassification bounds and thresholds. | Cannot be transplanted directly to selected path error. | ESTABLISHED | Xing SS-2025-0042 |
| R024 | Rare-event importance sampling towards closest wrong hypotheses is effective in Xing’s setting. | Controlled-tree adaptation must preserve coherent path law. | ESTABLISHED IN SOURCE SETTING; ADAPTATION OPEN | Xing SS-2025-0042 |
| R025 | The isolated iid single-node finite-sample composite error problem is solved prior work. | Import as nodewise input when assumptions apply. | ESTABLISHED BY PRIOR WORK | SB001 |
| R026 | For a two-node singleton problem conditioned on branch `A_0=1`, the selected joint-law Rényi divergence decomposes into the node-0 divergence, the branch-selection correction, and a logarithmic tilted expectation of the conditional new-data Rényi integral. | Positive ordinary and tilted branch reach; no iid assumption on new data. | CORRECT DERIVATION; now identified as R005 plus the established Rényi chain rule; finite checks added with R033 | `notes/2026-09-16_two_node_singleton_renyi_decomposition.md`; `tests/test_selected_converse.py` |
| R027 | The R026 future-data term is exactly the **common-input conditional Rényi divergence** of the two future kernels under the branch-selected tilted old-data law. | Several inequivalent notions are called conditional Rényi divergence; use the common-input/joint-law definition. | ESTABLISHED LITERATURE; exact mapping to R026 | Polyanskiy and Wu §7.12; Cai and Verdú 2019; conditional Rényi audit note |
| R028 | Rényi divergence has an exact chain rule for arbitrary joint laws: marginal Rényi divergence plus conditional Rényi divergence evaluated under the Rényi-tilted marginal. | Dependence changes the tilted conditioning law but does not destroy exact decomposition. | ESTABLISHED | Polyanskiy and Wu, Eq. (7.77)–(7.78) |
| R029 | Iterating R028 yields an exact full-chain decomposition for general dependent transition kernels using tilted prefix laws. | Finiteness/support conditions apply; no iid requirement. | ESTABLISHED by iteration; explicit preprint theorem available | Polyanskiy and Wu Eq. (7.77); Lei Yu, *The Entropy Method*, Theorem 8 |
| R030 | Adaptive simple channel discrimination already uses randomised tests and accumulation of Rényi/Hellinger-transform information under adaptively selected observations. | Simple fixed channel hypotheses, sensing action separate from final decision, asymptotic exponents. | ESTABLISHED | Hayashi 2009 |
| R031 | Composite adaptive channel discrimination is established, but the checked theory still assumes independence even when samples are non-identical; important adaptive composite exponent questions remain open. | One terminal composite decision; not arbitrary non-independent local decision tree. | ESTABLISHED BOUNDARY | Bergh, Datta and Salzmann, arXiv:2303.02016v2 |
| R032 | Arbitrary dependence in simple testing and filtered Hellinger-information frameworks are established separately. | Han is asymptotic simple testing; Jacod/Dzhaparidze et al. provide filtered experiment/Hellinger structure rather than UQ001 finite-sample error propagation. | ESTABLISHED BACKGROUND | Han 2000; Jacod 1989; Dzhaparidze, Spreij and Valkeila 2002 |
| R033 | Substituting R026 into the source converses gives explicit branch conditional Type II lower bounds in both Rényi directions, including the actual root errors and the appropriate tilted reach. | Fixed first rule; positive selected reaches and finite required moments. The two directions have different tilts. Actual root errors cannot be replaced by unrelated optimal or worst case errors. | DERIVED — UNREVIEWED; CHECKED NUMERICALLY | `notes/2026-09-16_selected_renyi_converse_sample_complexity.md`, Sections 2 to 4, equations (4) and (5); source equations (4), (48); `tests/test_selected_converse.py` |
| R034 | Under Q with correct path (1,1), converting the conditional error into B_Q=beta_0+(1-beta_0)beta_1 cancels the explicit factor 1-beta_0 in R033. The resulting converse bounds an actual two node path error. | A coherent P comparison has null label 0 at the root and the child on branch 1. The first rule still affects alpha_0, tilted reach and conditional information. No independence is used. | DERIVED — UNREVIEWED; CHECKED NUMERICALLY | selected converse note, Section 5, equations (6) and (7) |
| R035 | Uniform upper limits on conditional Rényi information give a converse for K successive all ones decisions, with the sum of logarithmic Type I budgets opposed to the sum of information limits. | Branch conditional Type I constraints and a coherent null comparison along that path are required. Proof uses surviving subprobability measures, not multiplication of marginal correctness rates. Arbitrary truth patterns are not characterised. | DERIVED — UNREVIEWED; CHECKED NUMERICALLY | selected converse note, Sections 6 and 7, equations (9) and (15); four stage finite check |
| R036 | Inverting R035 yields necessary sample size inequalities in n and m under explicit upper information growth bounds. Linear limits can follow from uniform conditional divergence limits without iid assumptions. Coherent pair selection also gives a composite lower bound when these limits are uniform over admissible policies. | Necessary only, not sufficient or an exact sample complexity. Do not independently minimise separate divergence terms. Both opposite direction local necessary conditions are retained. | DERIVED — UNREVIEWED; CHECKED NUMERICALLY | selected converse note, Sections 6 and 8, equations (10) to (14) |
| R037 | In the stated correlated Gaussian model, information equals lambda times J_0(n)+J_1(m), with J_t(k)=Delta_t^2[k(1-gamma_t)+2gamma_t]/[2 sigma_t^2(1+gamma_t)]. Optimising the converse order yields a closed form necessary count relationship. | Both blocks are dependent and the new block remains dependent given the old. Constancy of its conditional divergence follows from a common mean shift, not independence. The example yields a necessary total of 31, not a sufficient count; root reliability remains a separate requirement. | DERIVED — UNREVIEWED; CHECKED NUMERICALLY | selected converse note, Section 9, equations (16) to (19); `results/2026-09-16_selected_converse_checks.json` |
| R038 | Generalised Holder applied to the product of conditional observation likelihood ratios gives a constructed nonuniform upper bound on the selected conditional contribution from averaged higher order conditional Renyi moments. | Fixed coherent pair and first test. Optimise positive weights summing to one. No uniform cap over histories or iid assumption is required. Finite higher moments are sufficient, not necessary; computation can still be costly. | DERIVED — UNREVIEWED; CHECKED NUMERICALLY; no novelty claim | `notes/2026-09-23_nonuniform_selected_information_bounds.md`, Sections 2 and 3, equations (2) to (5) |
| R039 | Local integral comparison functions dominate the exact backward conditional moment and give an upper bound after averaging their initial value under the selected root tilt. | Reuses R001 at orders above one with finite moments. Comparison functions may be unbounded. Their integral inequalities must actually be proved from the kernels. No general fast recursion is claimed. | DERIVED — UNREVIEWED; finite recursion checks; no novelty claim | nonuniform information note, Section 4, equations (6) to (9) |
| R040 | A Gaussian feedback model with distinct autoregression coefficients has an exact scalar quadratic moment recursion and an explicit bound containing both n and m. Its pointwise conditional divergences are unbounded over histories but the selected bound can be finite. | New illustrative model, not a universal assumption. Gaussian integrability thresholds and actual first test reach are retained. Distinct from R037's constant conditional divergence model. | DERIVED — UNREVIEWED; CHECKED against full joint Gaussian integration | nonuniform information note, Section 5, equations (10) to (13); `results/2026-09-23_nonuniform_information_verification.json` |
| R041 | For fixed kernels and root laws, the supremum of the selected conditional contribution over all positive reach first tests satisfying only a Type I upper budget equals the least bound on the pointwise conditional divergence outside a set of total root tilted measure zero. | Proof selects a high divergence set with an appropriately scaled randomised indicator. Unbounded conditional divergence therefore prevents a finite bound uniform over all such first tests. It does not prevent a finite fixed test bound. | DERIVED — UNREVIEWED; finite alphabet check | nonuniform information note, Section 7 |
| R042 | The exact selected prefix chain rule makes the contribution nondecreasing with m for a coherent prefix process and fixed n and first test. No general monotonicity in n follows when the first test or future kernels change with n. | Existing R004/R028/R029 applied with the full updated prefix tilt. Do not freeze the tilt or replace it by local tilted transitions. | ESTABLISHED by the imported chain rule; CHECKED NUMERICALLY | nonuniform information note, Section 6, equation (14); F009 |
| R043 | Actual root power bounds below the tilted branch reach through the root Holder inequality, yielding a positive lower tilted reach when power is uniformly bounded below and the root moment is finite. | An elementary consequence of the existing converse machinery, not a new testing theorem. A Type I upper budget alone does not provide a positive lower reach. | DERIVED CONSEQUENCE; CHECKED NUMERICALLY | nonuniform information note, Section 7 |
| R044 | A standard minimising Renyi projection does not upper bound the selected singleton contribution; however, Holder change of measure through any reference old-history law mu gives an upper bound equal to a Renyi mismatch penalty plus an exponential future-information moment under mu. Taking mu as the unselected root tilt gives an explicit penalty bounded by minus log tilted branch reach. | Fixed singleton pair and first test. The reference-law moment still has to be controlled; minimising only the mismatch term need not minimise the total bound. No triangle inequality is assumed. | DERIVED — UNREVIEWED | `notes/2026-09-23_projection_assisted_selected_bound.md` |

## Failure and counterexample ledger

| ID | Failed statement / route | What is known | Consequence | Location |
| --- | --- | --- | --- | --- |
| F001 | Bounded likelihood ratios plus positivity and short horizon uniformly bound direct-estimator relative variance. | False; rare-action example gives relative variance `1/tau-1`. | Need branch reach control or different estimator. | research plan; C09 |
| F002 | F001 proves every efficient algorithm impossible. | Not established; exact branch integration removes the variance in the example. | Do not infer an algorithmic impossibility. | C10 |
| F003 | Fixed node truth can be maximised independently at each history. | False. | Keep truth map fixed at the node. | controlled identities note |
| F004 | Coupled environment parameter can be replaced by independent local worst cases. | False. | Prove rectangularity before local pasting. | research plan; C12 |
| F005 | Same-data reuse itself increases full-transcript Rényi divergence. | False under common policy. | Treat same-data project as boundary case. | C13 |
| F006 | Relative gap error below order one always gives uniform relative divergence error. | False without overlap control. | State overlap promise or different target. | research plan; C15 |
| F007 | Pairwise path Rényi divergence already equals minimax path risk. | Not established. | Separate information and testing objects. | C19 |
| F008 | Local Type I/II guarantees alone determine complete sequential path law. | False in predecessor project; unsafe here. | Do not multiply local correctness probabilities. | relation note |
| F009 | Locally tilted simulation equals globally tilted path simulation. | False; global tilt contains continuation factors. | Do not use local normalisation as exact global sampler. | controlled identities note |
| F010 | Finite-tree backward pass is automatically linear in horizon. | False; history count may be exponential. | Count states/histories/oracle calls. | controlled identities note |
| F011 | Action-dependent future observations are themselves novel. | False. | Novelty cannot rest on controlled sensing alone. | R017 |
| F012 | Composite hypotheses plus controlled sequential sensing are absent from literature. | False. | Do not claim this combination alone. | R018 |
| F013 | Temporal dependence or controlled Markov memory is absent from sequential testing theory. | False. | Removing iid alone is not the novelty. | R016, R019, R020 |
| F014 | Xing’s simultaneous-stream threshold applies directly to selected path error. | Not justified. | Derive pathwise threshold separately. | R014, R023 |
| F015 | Active-sensing control can be silently identified with the reported edge decision. | False in general. | Preserve decision-as-control semantics. | Xing literature audit |
| F016 | Hidden-Markov Rényi rate result supplies finite-sample controlled path theorem. | False implication. | Use only as dependent Rényi background. | R021 |
| F017 | Re-solve isolated iid single-node composite testing. | Duplicate work. | Stop unless assumptions change or verification is explicitly requested. | SB001; R025 |
| F018 | The R026 dependent future-data term is itself a new unsolved divergence object, or dependence destroys the exact Rényi chain rule. | False. It is the standard common-input conditional Rényi divergence, and the exact tilted-marginal chain rule is known. | Do not spend research effort rediscovering the algebra. The new work begins at decision-selected testing/minimax error propagation. | R027–R029; conditional Rényi audit note |
| F019 | Raw observation count alone forces information to increase under arbitrary dependence. | False. Repeating one freshly drawn Bernoulli observation m times leaves its Rényi information constant in m. | State an information growth assumption before claiming a universal count relationship. | selected converse note, Section 10; repeated observation regression check |
| F020 | An upper bound on the ordinary mean conditional divergence upper bounds T for lambda>1. | False. T is a logarithmic exponential mean; rare large conditional divergences can dominate it. | Use a uniform bound or a justified exponential moment bound, not an arithmetic mean. | selected converse note, Section 6; two point regression example |
| F021 | The actual alpha_0 may be replaced by its upper budget in either direction of the selected converse. | False. That replacement weakens equation (6) safely but can make equation (7) invalid and even larger than one. | Check monotonicity separately in each direction and retain quantities from the same first test. | selected converse note, Section 5; explicit regression check |
| F022 | Absolute continuity and finite conditional divergence at every realised history guarantee a finite selected exponential average. | False. A Gaussian conditional divergence equal to S squared is finite pointwise but its exponential average diverges when the old Gaussian variance is large enough. | Verify integrability under the selected tilt, not merely pointwise finiteness. | nonuniform information note, Section 7 |
| F023 | Finiteness of the target order selected contribution implies finiteness of the positive weight higher moment bound R038. | False. A discrete likelihood ratio can have a finite moment exactly at lambda and no moment above lambda; adding a copied observation preserves finite target divergence but the displayed higher order bound is infinite. | Treat R038 as sufficient, not a necessary characterisation. Remove identically one factors or use the original order recursion when useful. | nonuniform information note, Section 3 |
| F024 | A Type I upper budget alone supplies a finite bound uniform over all first tests whenever some fixed first test has a finite contribution. | False when the pointwise conditional divergence is unbounded under the root tilt. R041 gives an exact supremum argument using selection on high divergence histories. | Retain the first test dependence or state additional root power/reach restrictions; do not silently claim uniformity. | R041; nonuniform information note, Section 7 |
| F025 | A minimising Renyi projection can be substituted directly as an upper bound on d_{lambda,1}. | False in general. A projection minimises divergence and therefore points toward a lower information value; in singleton classes it is trivial. | For an upper bound, use a proved comparison inequality or projection-assisted change of measure with an explicit mismatch penalty. | R044; projection-assisted note |

## Attempted and reusable method ledger

| ID | Method | Current outcome | Next permissible use | Location |
| --- | --- | --- | --- | --- |
| M001 | Full path enumeration | Exact small-model reference; exponential. | Validation and counterexamples only. | `src/controlled_renyi.py` |
| M002 | Exact backward `G_t` on full histories | Exact but potentially exponential. | Baseline; compress only with proved sufficient state. | `src/controlled_renyi.py` |
| M003 | Predictable Monte Carlo gap estimator | Unbiased; rare branches can explode relative variance. | Baseline under explicit variance condition. | R006–R008; F001 |
| M004 | Explicit integration over selected action branches | Removes two-stage rare-action sampling variance; branch cost can grow exponentially. | Short-horizon controlled examples with full cost accounting. | research plan |
| M005 | Local tilted path sampling | Valid importance identity, not global tilted path sampling. | Benchmark only. | controlled identities note |
| M006 | Exact finite-state recursion | Exact with genuinely sufficient observed state. | Main tractable exact class. | R009 |
| M007 | General information-function / information-clock asymptotics | Established in passive non-iid composite testing. | Controlled analogue only after finite-sample object is clear. | R014–R016 |
| M008 | Adaptive likelihood versus generalised wrong-class likelihood | Useful in Xing’s setting. | Candidate local statistic; requires new pathwise proof. | Xing audit |
| M009 | Rare-event importance sampling towards wrong hypotheses | Effective in Xing’s setting. | Build coherent wrong-path change of measure. | R024 |
| M010 | Chernoff-style controlled sensing | Mature policy-design baseline. | Compare only after separating sensing action from reported decision. | R017–R019 |
| M011 | Markov operator / spectral Rényi rates | Useful for fixed HMMs. | Long-horizon controlled finite-state work after policy fixed. | R021 |
| M012 | Common-input conditional Rényi divergence plus tilted-marginal chain rule | Exactly resolves the R026 non-iid divergence algebra and iterates over dependent paths. | Use as the primary information identity for singleton converse propagation; do not reinvent it. | R027–R029 |
| M013 | Uniform conditional Rényi bound / adaptive composition | Replacing the exact tilted average by an essential supremum gives additive coarse control; mature analogue in Rényi differential privacy. | Use only when a uniform conditional bound is acceptable; record loss of exact branch-selected structure. | Mironov 2017; conditional Rényi audit note |
| M014 | Substitute the source converses, retain actual branch reaches, cancel survival when converting to path risk, then invert uniform upper information limits. | Gives R033 to R037, with finite checks in both divergence directions. | Refine the retained selection term or specified information model; do not repeat the initial substitution as a new task. | selected converse note; source record `sources/2608.28068/SOURCE.md` |
| M015 | Generalised Holder with optimised weights on conditional likelihood ratio factors | R038 bounds the selected contribution using averaged higher order conditional moments, rather than uniform history caps. | Check higher moment finiteness; compare conditional/grouped variants and original order recursion. Do not claim a fast algorithm or necessary integrability criterion. | R038; F023 |
| M016 | Local integral comparison functions and Gaussian quadratic moment recursion | R039/R040 give nonuniform original order bounds, including an example with no finite uniform conditional divergence cap. | Extend to specified kernel structures or review the stated recursion; preserve support and integrability thresholds. | R039/R040 |
| M017 | Projection-assisted change of measure for selected history laws | Holder through a tractable reference law yields R044; the unselected root tilt has an explicit selection mismatch penalty. | Use only when the reference-law exponential future-information moment is tractable; a pure projection is not enough. | R044; projection-assisted note |

## Open problem ledger

| ID | Open problem | Dependency / warning | Current next location |
| --- | --- | --- | --- |
| O001 | Useful variance bound for action-integrated estimation on an explicit controlled class. | Must survive F001 and count branch integration. | Task 01 |
| O002 | Explicit model-based bound for remaining-gain constant `K`. | Exact `G_t` everywhere would be circular computationally. | research plan |
| O003 | General finite-horizon approximation algorithm with explicit work and accuracy. | No linear-horizon theorem established. | research plan |
| O004 | Extend SB001 only where conditional/history dependence actually prevents direct use of the prior local theorem. | Do not rederive isolated iid theory. R033 now supplies the branch selected converse substitution. | later theorem work; R033 |
| O005 | Connect local testing guarantees to minimax path risk. | R034 to R036 give a restricted converse connection, not a full characterisation. F007/F008 still block naive propagation. | UQ001 |
| O006 | Characterise minimax recursion separately for rectangular and coupled environment classes. | Respect F003/F004. | relation note |
| O007 | Determine whether globally optimal testing policy has useful dynamic characterisation. | Compare with active testing; local optimality need not be global. | future work |
| O008 | Complete novelty audit for predictable Hellinger-process identities. | R027–R032 are now mandatory prior art. | literature work |
| O009 | Formalise positive reach and rectangular/coupled environments in manuscript. | Proposed but not yet authoritative manuscript text. The approved zero based notation amendment is in the register; original manuscript retained. | relation note; `docs/NOTATION.md` |
| O010 | Define useful controlled information process for history-dependent composite experiments. | Exact conditional Rényi chain rule is known; R033 to R036 now give one restricted converse use. | R027–R029; selected converse note |
| O011 | Theorem-level novelty audit against controlled sensing and composite adaptive testing. | `NO DIRECT MATCH LOCATED` is not novelty. New applications have not received an independent novelty review. | literature notes |
| O012 | Determine the mathematical effect of making the reported local hypothesis decision itself the control selecting the next experiment. | Do not silently reduce to ordinary sensing control. | future examples/theorems |
| O013 | Construct coherent importance-sampling law for rare wrong paths. | Rectangular and coupled cases differ. | M009 |
| O014 | Develop finite-sample pathwise error-propagation theorem for UQ001. | PARTIALLY ANSWERED on the converse side by R034 to R036 for the stated target path and coherent comparison; general truth patterns and matching achievability remain open. | O004/O005; R033 to R037 |
| O015 | Controlled finite-state Markov model as first tractable comparison class. | Preserve observed-state sufficiency and truth map. A distinct correlated Gaussian illustration is now recorded in R037. | R009/R019/R021 |
| O016 | Use the established conditional Rényi chain rule to obtain a singleton converse recursion in previous errors and future information. | PARTIALLY ANSWERED by R033 to R035: exact substitution in both directions, two node survival cancellation, and an all ones path converse with uniform information limits. Do not repeat this calculation. General sharp recursion remains open. Earlier unknown divergence algebra interpretation remains superseded by R027 to R029. | selected converse note, Sections 4 to 7; O019 |
| O017 | Lift the singleton converse to coherent history dependent composite classes. | PARTIALLY ANSWERED by the coherent pair lower bound in R036/Section 8. This requires a suitable pair and policy uniform information limits, and is not an exact minimax recursion for arbitrary classes. | UQ001; F003/F004; R036 |
| O018 | Determine whether repeated local decision constraints yield effects not captured by standard adaptive channel discrimination. | Hayashi and Bergh et al. remain required comparisons. A new novelty conclusion is not claimed from the present substitution. | R030/R031; O012 |
| O019 | Review and sharpen the sample size converses while retaining the selected tilted reach and testing them against exact selected experiment error. | Start from R033 to R037. Necessary counts are not sufficient; root reliability and coherent pairs remain constraints. Independent proof review remains required. R038 to R043 now add nonuniform information bounds and explain the obstruction to uniformity over all first tests. | selected converse note, Sections 6, 9 and 10; nonuniform information note |
| O020 | Sharpen and apply the nonuniform information bounds to the error propagation problem while preserving first test dependence or justified root power restrictions. | R038 can require unnecessarily high moments; R039 requires verified comparison functions; R041 blocks unsupported uniformity. Do not repeat the uniform cap argument as a new solution. Independent review remains required. | R038 to R044; `notes/2026-09-23_nonuniform_selected_information_bounds.md`; projection-assisted note |
| O021 | Determine whether a tractable reference family for the old-history law makes the R044 projection-assisted bound useful for explicit finite-sample singleton counts. | The total bound includes both a Renyi mismatch penalty and a reference-law exponential future-information moment; optimising the projection term alone is insufficient. | R044; M017 |

## Literature boundary: conditional Rényi bottleneck audit, 16 September 2026

Detailed note: `notes/2026-09-16_conditional_renyi_chain_rule_literature_audit.md`.

The audit establishes that the divergence algebra behind R026 is known. The project must not claim novelty for conditional Rényi divergence, the tilted-marginal Rényi chain rule, or its iteration to general dependent kernels.

The targeted search did **not** locate a theorem for the complete combination sought here: repeated randomised local composite hypothesis decisions, where each reported decision selects the next dependent experiment, with coherent history-dependent uncertainty and finite-sample propagation of nodewise Type I/II tradeoffs into path error. Record this only as `NO DIRECT MATCH LOCATED`.

## Earlier literature boundary: controlled sequential testing

The following broad ingredients are already established and are not novelty claims by themselves: action-controlled future observations, adaptive sensing, composite controlled sensing, controlled Markov observations, temporal dependence, non-iid sequential testing, nonlinear information clocks, finite-sample active testing in some models, and Rényi divergence rates for HMMs.

## Cross-project boundary

`Parallel-Hypothesis` remains separate. Its same-data path representation, local-error insufficiency, rectangular propagation, selected Rényi corrections and fixed-path converse/achievability recursions may be used as boundary checks but should not be rederived here.

## Task record: selected converse and sample counts, 16 September 2026

Work on `research/selected-renyi-converse-sample-complexity` began from `f7e6dab50b296b1a0f9faf21b6cb1a18911e2c92`. Overlapping inputs checked: SB001, R025 to R029, M013, O016/O017, and F003/F004/F007. Existing source records and topic bibliographies were checked first. The supplied paper was read for the exact two converses; the only new online check was its version record, not a repeated literature survey.

The new calculation and its limitations are recorded in R033 to R037 and F019 to F021. Seventeen new finite test methods were added; all 47 methods, including the 30 existing methods, passed locally under Python 3.13.5. Existing source and test files were checked against their Git blob hashes before execution. No independent mathematical review or remote CI run is claimed. Details and hashes: `results/2026-09-16_selected_converse_checks.json`.

## Task record: nonuniform selected information bounds, 23 September 2026

This extension starts from the verified branch head `1409d7af0c4b33d98fcec73bb54eb53fec54e910`. It addresses the user's request not to replace the dependent contribution by an assumed constant. It imports the exact chain rule and backward recursion rather than claiming them as new. The main new-to-this-repository content is R038 to R043, with failures F022 to F024, methods M015/M016 and open task O020.

Current user notation takes priority for new work: `d_{lambda,1}(n,m;phi_0)` is the logarithmic selected tilted average formerly called `T_{lambda,1}`. Do not use `d_{lambda,1}(x)` for the pointwise conditional divergence. The root in this calculation is iid with single observation laws P_0,Q_0. Retain the full pointwise conditional divergence when explaining it. Do not introduce new placeholders without definition. Keep the user's working notes unchanged.

The existing Polyanskiy and Wu source was rechecked at equations (7.77) and (7.78) after checking the ledger and source library. The primary source check used parsed text; screenshots failed. No new broad literature survey, exhaustive novelty claim or independent review was performed. Source verification depth and scope are recorded in the new note and in `sources/conditional_renyi_chain_rule/VERIFICATION_2026-09-23.md`.

Fifteen standalone local deterministic methods passed. They do not constitute a rerun of the older 47 method repository suite. No production code or original manuscript was modified. The numerical record is `results/2026-09-23_nonuniform_information_verification.json`; the complete standalone script and extended derivation are also provided as a conversation attachment. Proofs and counterexamples are preserved in `notes/2026-09-23_nonuniform_selected_information_bounds.md`.

## End-of-task update rule

Each substantive task must record stable IDs, exact hypotheses/scope, status, authoritative location, review/numerical status, and any obstruction or supersession. `docs/RESEARCH_LEDGER.md`, `CURRENT_STATUS.md`, and `docs/CLAIMS.md` must remain consistent.

## Literature audit: computing and controlling dependent Rényi divergence, 24 September 2026

Mandatory source record before another search: `sources/non_iid_renyi/REVIEW.md` and `sources/non_iid_renyi/references.bib`. They contain 30 records with primary links and reading depths. S29 and S30 are explicitly limited leads. The extended conversation report supplies a method table and further explanation. The audit branch starts from `adc0b7784f61569308f70244bb4e639c1f396415` and does not change the original manuscript, user notes or production code.

The following IDs add source results and boundaries, not new project theorem claims.

| ID | Source result | Scope and limitation | Status | Source location |
| --- | --- | --- | --- | --- |
| R045 | Finite length Markov cumulant bounds with spectral and boundary terms lead to finite length simple testing bounds. The selected finite state moment also has an exact weighted matrix product representation. | Finite observed sufficient state, appropriate support and source ergodicity conditions. The report's selected initial law formula is an algebraic translation, not a new source theorem. Sequence length complexity does not ignore state size or precision. | ESTABLISHED SOURCE RESULT; explicit translation supplied | Watanabe and Hayashi 2017, Lemma 6.1 and Theorem 9.1; S05/S06 in the new source record |
| R046 | Adaptive Rényi composition can use cumulative history dependent conditional costs, including a fixed pair and suitable stopping. | Requires the cumulative budget along paths, not only its expectation or one realised path. Source assumptions must be checked for the auxiliary common initial law experiment. | ESTABLISHED SOURCE RESULT; project budget not yet proved | Feldman and Zrnic 2021, Theorem 3.1, Remark 3.2 and Theorem 4.3; S12 |
| R047 | Positive operator spectral and multiplicative drift methods control exponential functionals of dependent Markov paths. | Transform domain, boundedness or multiplicative drift, domination and initial integrability conditions are substantive. Ordinary geometric ergodicity is not an all orders Rényi guarantee. | ESTABLISHED SOURCE METHODS; constants require model work | Kontoyiannis and Meyn 2003/2005; S08/S09 |
| R048 | Exponential functionals admit an exact variational reference infimum involving a Rényi penalty and a reference exponential moment. | Atar et al. use R_alpha=D_alpha/alpha. Their bounded function theorem and any unbounded extension must be distinguished. This is prior art for the method behind R044, not a solved reference optimisation for our model. | ESTABLISHED SOURCE RESULT | Atar, Chowdhary and Dupuis 2015, Theorem 2.1; Anantharam 2018; S15/S16 |
| R049 | The hidden Markov rate result R021 uses an observed likelihood/filter construction and explicit C1 to C4 conditions; orders above one retain additional positivity requirements. | A hidden transition matrix cannot generally be powered entrywise to obtain the observed Rényi moment. A rate needs finite length evaluation or remainder before use as a finite sample upper bound. | VERIFIED SCOPE REFINEMENT of R021 | Fuh et al. 2025, Theorem 3.1; S10 |
| R050 | Shifted composition gives finite time Rényi comparisons for endpoint laws, and recent discrete channel work develops order greater than one contraction. | Endpoint bounds do not upper bound full retained path divergence. Rényi contraction factors cannot be inherited from KL or total variation without proof. | ESTABLISHED SOURCE METHODS; observation scope restriction | Altschuler and Chewi I/III, S18/S19; Vandenbroucque et al. 2026 preprint S20 |
| R051 | Feynman–Kac particle normalising constants have nonasymptotic numerical error bounds under explicit potential and transition comparisons. | Particle count controls computation error, not statistical n or m. Conditions may fail for unbounded likelihood ratio weights. No new simulation was run in this audit. | ESTABLISHED SOURCE RESULT | Cérou, Del Moral and Guyader 2011, Theorems 1.5 and 5.1; S21 |
| R052 | Finite sample information based concentration and Hellinger moment bounds for dependent laws are established, including Hölder and Markov constructions. | Esposito–Mondelli principally compare a joint law to a product of marginals. Arbitrary testing pairs require a proved reference comparison. Related base methods in R038 are not novelty claims. | ESTABLISHED SOURCE RESULT; target pair distinction | Esposito and Mondelli 2024, Theorem 1, equations 23 to 25; S14 |

| ID | Invalid inference | Consequence | Location |
| --- | --- | --- | --- |
| F026 | A limiting Rényi divergence rate can be substituted as an upper bound at an arbitrary finite sample size. | Retain a proved finite length remainder or evaluate the finite horizon moment. | R045/R049; source record S05/S10 |
| F027 | An upper bound for the final observation's divergence is an upper bound for the complete retained block. | Data processing gives the reverse comparison between these objects; require sufficiency or keep the path. | R050; source record S02/S18/S19 |
| F028 | A restricted variational supremum or a trained numerical divergence estimate is automatically an upper information bound for a converse. | Population restriction gives a lower value; sampling and optimisation errors need separate control. | Birrell et al. 2021, Theorem 3.1; S27 |

| ID | Next research task | Boundary |
| --- | --- | --- |
| O022 | Apply the finite length Markov spectral bounds and/or the fixed pair adaptive Rényi filter to the selected future experiment, retaining its initial tilt and finite length terms. | Begin with R045/R046 and existing source records. Prove the sufficient observed state or cumulative budget. Do not assert a new general n,m law or repeat the chain rule derivation. |

An expectation over histories is compatible with finite sample analysis. Finiteness, evaluability, numerical error and uniformity over first tests are distinct requirements. The audit does not establish exact or sufficient sample complexity. The older Lei Yu Theorem 8 reference in R029 was not freshly verified because the monograph could not be reopened; the exact chain rule remains supported by the inspected Polyanskiy–Wu source. No complete proof review, regression rerun or independent novelty claim is made.
