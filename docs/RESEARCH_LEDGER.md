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

At every reachable node, the primary object is the local composite testing error tradeoff. For a local Type I budget `epsilon_t`, write

\[
\beta_t^\star(\varepsilon_t\mid Z_{t-1}),
\]

where `Z_{t-1}` denotes the observed past before node `t`. The symbol `h` is reserved for the log likelihood ratio from the prior article and must not be used for history.

The ultimate goal is to understand how the nodewise Type I and Type II errors propagate through the action-selected path when an earlier reported decision changes the future statistical experiment.

We seek both:

* **Achievability:** attainable global sequential error guarantees from attainable nodewise guarantees.
* **Impossibility / converse:** lower bounds on global reliability, or necessary local error performance, valid for every admissible sequence of randomised tests.

A representative global event is making at least one wrong edge by horizon `T`. Local errors and global path risk must remain distinct.

Rényi quantities, conditional divergences, information clocks, algorithms and policy constructions are tools towards UQ001, not the final objective.

## Solved base cases — do not re-solve

### SB001 — Isolated single-node finite-sample composite binary testing

For iid product data and composite classes `C_0` and `C_1`, the optimal worst-case Type II error under a Type I constraint,

\[
\beta_n^\star(\varepsilon;\mathcal C_0,\mathcal C_1),
\]

is already treated in Vera Sigüenza and Esposito, *Finite Sample Bounds for Composite Hypothesis Testing*. The paper supplies finite-sample achievability and converse bounds. Import this theory. Do not rederive it unless an assumption is explicitly changed or independent verification is requested.

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
| R026 | For a two-node singleton problem conditioned on branch `A_0=1`, the selected joint-law Rényi divergence decomposes into the node-0 divergence, the branch-selection correction, and a logarithmic tilted expectation of the conditional new-data Rényi integral. | Positive ordinary and tilted branch reach; no iid assumption on new data. | CORRECT DERIVATION; now identified as R005 plus the established Rényi chain rule | `notes/2026-09-16_two_node_singleton_renyi_decomposition.md` |
| R027 | The R026 future-data term is exactly the **common-input conditional Rényi divergence** of the two future kernels under the branch-selected tilted old-data law. | Several inequivalent notions are called conditional Rényi divergence; use the common-input/joint-law definition. | ESTABLISHED LITERATURE; exact mapping to R026 | Polyanskiy and Wu §7.12; Cai and Verdú 2019; conditional Rényi audit note |
| R028 | Rényi divergence has an exact chain rule for arbitrary joint laws: marginal Rényi divergence plus conditional Rényi divergence evaluated under the Rényi-tilted marginal. | Dependence changes the tilted conditioning law but does not destroy exact decomposition. | ESTABLISHED | Polyanskiy and Wu, Eq. (7.77)–(7.78) |
| R029 | Iterating R028 yields an exact full-chain decomposition for general dependent transition kernels using tilted prefix laws. | Finiteness/support conditions apply; no iid requirement. | ESTABLISHED by iteration; explicit preprint theorem available | Polyanskiy and Wu Eq. (7.77); Lei Yu, *The Entropy Method*, Theorem 8 |
| R030 | Adaptive simple channel discrimination already uses randomised tests and accumulation of Rényi/Hellinger-transform information under adaptively selected observations. | Simple fixed channel hypotheses, sensing action separate from final decision, asymptotic exponents. | ESTABLISHED | Hayashi 2009 |
| R031 | Composite adaptive channel discrimination is established, but the checked theory still assumes independence even when samples are non-identical; important adaptive composite exponent questions remain open. | One terminal composite decision; not arbitrary non-independent local decision tree. | ESTABLISHED BOUNDARY | Bergh, Datta and Salzmann, arXiv:2303.02016v2 |
| R032 | Arbitrary dependence in simple testing and filtered Hellinger-information frameworks are established separately. | Han is asymptotic simple testing; Jacod/Dzhaparidze et al. provide filtered experiment/Hellinger structure rather than UQ001 finite-sample error propagation. | ESTABLISHED BACKGROUND | Han 2000; Jacod 1989; Dzhaparidze, Spreij and Valkeila 2002 |

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
| F010 | Finite-tree backward pass is automatically linear in horizon. | False; history count may be exponential. | Count states/histories/oracle calls. | research plan |
| F011 | Action-dependent future observations are themselves novel. | False. | Novelty cannot rest on controlled sensing alone. | R017 |
| F012 | Composite hypotheses plus controlled sequential sensing are absent from literature. | False. | Do not claim this combination alone. | R018 |
| F013 | Temporal dependence or controlled Markov memory is absent from sequential testing theory. | False. | Removing iid alone is not the novelty. | R016, R019, R020 |
| F014 | Xing’s simultaneous-stream threshold applies directly to selected path error. | Not justified. | Derive pathwise threshold separately. | R014, R023 |
| F015 | Active-sensing control can be silently identified with the reported edge decision. | False in general. | Preserve decision-as-control semantics. | Xing literature audit |
| F016 | Hidden-Markov Rényi rate result supplies finite-sample controlled path theorem. | False implication. | Use only as dependent Rényi background. | R021 |
| F017 | Re-solve isolated iid single-node composite testing. | Duplicate work. | Stop unless assumptions change or verification is explicitly requested. | SB001; R025 |
| F018 | The R026 dependent future-data term is itself a new unsolved divergence object, or dependence destroys the exact Rényi chain rule. | False. It is the standard common-input conditional Rényi divergence, and the exact tilted-marginal chain rule is known. | Do not spend research effort rediscovering the algebra. The new work begins at decision-selected testing/minimax error propagation. | R027–R029; conditional Rényi audit note |

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

## Open problem ledger

| ID | Open problem | Dependency / warning | Current next location |
| --- | --- | --- | --- |
| O001 | Useful variance bound for action-integrated estimation on an explicit controlled class. | Must survive F001 and count branch integration. | Task 01 |
| O002 | Explicit model-based bound for remaining-gain constant `K`. | Exact `G_t` everywhere would be circular computationally. | research plan |
| O003 | General finite-horizon approximation algorithm with explicit work and accuracy. | No linear-horizon theorem established. | research plan |
| O004 | Extend SB001 only where conditional/history dependence actually prevents direct use of the prior local theorem. | Do not rederive isolated iid theory. | later theorem work |
| O005 | Connect local testing guarantees to minimax path risk. | F007/F008 block naive propagation. | UQ001 |
| O006 | Characterise minimax recursion separately for rectangular and coupled environment classes. | Respect F003/F004. | relation note |
| O007 | Determine whether globally optimal testing policy has useful dynamic characterisation. | Compare with active testing; local optimality need not be global. | future work |
| O008 | Complete novelty audit for predictable Hellinger-process identities. | R027–R032 are now mandatory prior art. | literature work |
| O009 | Formalise positive reach and rectangular/coupled environments in manuscript. | Proposed but not yet authoritative manuscript text. | relation note |
| O010 | Define useful controlled information process for history-dependent composite experiments. | Exact conditional Rényi chain rule is known; the question is which derived information quantity controls testing errors. | R027–R029 |
| O011 | Theorem-level novelty audit against controlled sensing and composite adaptive testing. | `NO DIRECT MATCH LOCATED` is not novelty. | literature notes |
| O012 | Determine the mathematical effect of making the reported local hypothesis decision itself the control selecting the next experiment. | Do not silently reduce to ordinary sensing control. | future examples/theorems |
| O013 | Construct coherent importance-sampling law for rare wrong paths. | Rectangular and coupled cases differ. | M009 |
| O014 | Develop finite-sample pathwise error-propagation theorem for UQ001. | Local iid problem is solved; exact dependent Rényi algebra is also known. | O004/O005; R027–R029 |
| O015 | Controlled finite-state Markov model as first tractable comparison class. | Preserve observed-state sufficiency and truth map. | R009/R019/R021 |
| O016 | Use the **established** conditional Rényi chain rule under branch-selected tilted prefix laws to derive a finite-sample singleton converse recursion in terms of previous-node error quantities and future conditional information. | Supersedes the earlier wording that treated the R026 future-data term itself as the unknown object. Do not rederive R027–R029. | `notes/2026-09-16_conditional_renyi_chain_rule_literature_audit.md`; R026–R030 |
| O017 | Lift the singleton converse recursion to history-dependent composite classes by taking the pairwise converse over a coherent environment class without illegal rectangularisation. | Hardest-pair reduction is available locally; global coupling must be preserved. | UQ001; F003/F004; R031 |
| O018 | Determine whether decision-as-control plus repeated local error constraints yields finite-sample phenomena not captured by standard adaptive channel discrimination. | Hayashi solves a close simple asymptotic neighbour; Bergh et al. solve parts of a composite independent neighbour. | R030/R031; O012 |

## Literature boundary: conditional Rényi bottleneck audit, 16 September 2026

Detailed note: `notes/2026-09-16_conditional_renyi_chain_rule_literature_audit.md`.

The audit establishes that the divergence algebra behind R026 is known. The project must not claim novelty for conditional Rényi divergence, the tilted-marginal Rényi chain rule, or its iteration to general dependent kernels.

The targeted search did **not** locate a theorem for the complete combination sought here: repeated randomised local composite hypothesis decisions, where each reported decision selects the next dependent experiment, with coherent history-dependent uncertainty and finite-sample propagation of nodewise Type I/II tradeoffs into path error. Record this only as `NO DIRECT MATCH LOCATED`.

## Earlier literature boundary: controlled sequential testing

The following broad ingredients are already established and are not novelty claims by themselves: action-controlled future observations, adaptive sensing, composite controlled sensing, controlled Markov observations, temporal dependence, non-iid sequential testing, nonlinear information clocks, finite-sample active testing in some models, and Rényi divergence rates for HMMs.

## Cross-project boundary

`Parallel-Hypothesis` remains separate. Its same-data path representation, local-error insufficiency, rectangular propagation, selected Rényi corrections and fixed-path converse/achievability recursions may be used as boundary checks but should not be rederived here.

## End-of-task update rule

Each substantive task must record stable IDs, exact hypotheses/scope, status, authoritative location, review/numerical status, and any obstruction or supersession. `docs/RESEARCH_LEDGER.md`, `CURRENT_STATUS.md`, and `docs/CLAIMS.md` must remain consistent.
