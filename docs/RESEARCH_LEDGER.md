# Research ledger

Date created: 16 September 2026.

This file is the persistent index of results, failures, counterexamples, attempted methods, literature boundaries, and open directions for `esig626/sequential_testing`.

Its purpose is to prevent duplicated research. Every scientific task must read this ledger before derivation, literature search, coding, numerical work, theorem drafting, or manuscript changes.

The ledger is an index, not a substitute for proofs. Each entry points to the authoritative source containing the derivation, counterexample, code, validation record, or literature audit.

## Mandatory use

Before starting scientific work:

1. Read this file in full.
2. Search the ledger for the topic, formula, method, obstruction, and model class involved in the proposed task.
3. Identify the existing entry IDs that overlap the task.
4. Do not rederive an existing result unless the task is explicitly an independent verification, correction, strengthening, or generalisation.
5. If an existing failure already rules out the proposed route under the same assumptions, do not repeat it. Either change the assumptions explicitly or pursue a different route.
6. When a task extends an existing item, state which ledger ID is being extended and what is genuinely new.
7. At the end of every substantive research task, update this ledger before declaring the task complete.

Never delete an old result or failure merely because it is superseded. Mark it `SUPERSEDED` and point to the replacement. A failed approach is research output and must remain visible.

## Ultimate research question

### UQ001 — How do the errors propagate?

At every reachable node, the primary object of interest is the local composite testing error tradeoff. For a local Type I budget `epsilon_t`, the fundamental quantity is

\[
\beta_t^\star(\varepsilon_t\mid h_{t-1}),
\]

the smallest worst case Type II error achievable at that node under the prescribed Type I constraint. Particular tests are secondary: they are used only as constructions for achievability, while converse results describe what no test can beat.

The ultimate goal of this project is to understand how these nodewise errors propagate through the sequential, action selected path when an earlier reported decision changes the node reached and therefore the future statistical problem.

The central target is therefore to obtain both:

1. **Achievability:** rigorous upper bounds showing how attainable local Type I and Type II error guarantees imply an attainable global sequential error guarantee, such as a bound on
   \[
   \mathbb P\!\left(\bigcup_{t=1}^T\{A_t\neq\Theta_t\}\right).
   \]
2. **Impossibility / converse:** rigorous lower bounds showing what global reliability cannot be achieved, or what local error performance is necessarily required, regardless of the tests used at the nodes.

The sequential dependence matters because an error at node `t` changes which node and which composite testing problem is encountered next. Therefore the local errors cannot in general be propagated by assuming independence, multiplying marginal correctness probabilities, or simply adding nominal node errors.

All Rényi quantities, path divergences, information clocks, controlled sensing analogies, numerical algorithms, and policy constructions are tools towards answering UQ001. They are not the ultimate objective of the project.

## Solved base cases — do not re-solve

### SB001 — Isolated single-node finite-sample composite binary testing

For a single isolated node with iid product data and composite classes `C_0` and `C_1`, the local object

\[
\beta_n^\star(\varepsilon;\mathcal C_0,\mathcal C_1)
=
\inf_{\phi_n:\,\alpha_n(\phi_n;\mathcal C_0)\leq\varepsilon}
\sup_{Q\in\mathcal C_1}\mathbb E_{Q^{\otimes n}}[1-\phi_n(X^n)]
\]

is already the subject of the prior paper **Finite Sample Bounds for Composite Hypothesis Testing** by Vera Sigüenza and Esposito. That work provides the finite-sample achievability and converse theory for the isolated iid composite binary problem. This is the solved base case from which the present project starts.

**Mandatory rule for Codex and future research:** do not treat the isolated single-node iid problem as open. Do not spend research time rederiving its achievability bounds, converse bounds, or the optimisation defining `beta_n^star`, and do not search for a particular test merely for its own sake. A particular test is relevant only when it is needed as an achievability construction or when a genuinely new assumption requires an extension.

When a node in the sequential tree satisfies the assumptions of the prior single-node theory, use that theory as an input. New work begins only where the sequential structure changes the question: conditioning on realised history, action-selected future experiments, dependence across stages, coherent uncertainty across the tree, or propagation of the nodewise Type I and Type II errors into a global path error.

Any task that proposes to revisit single-node composite testing must first cite `SB001` and state exactly which assumption of the prior result is being changed. If no assumption is changed and no independent verification has been explicitly requested, the task is duplicate work and must stop.

## Status vocabulary

* `ESTABLISHED`: supported by an external source or a previously established theorem with applicable hypotheses.
* `DERIVED — UNREVIEWED`: derived in this repository, but not yet independently checked.
* `CHECKED NUMERICALLY`: verified on finite reference examples or regression tests only.
* `FAILED / COUNTEREXAMPLE`: a proposed statement or method is false under the stated assumptions.
* `OPEN`: no result has been established.
* `SUPERSEDED`: retained for history but replaced by a later entry.
* `NO DIRECT MATCH LOCATED`: a targeted literature search found no direct theorem matching the stated combination; this is not a novelty claim.

## Results ledger

| ID | Result | Scope and limitations | Status | Authoritative location |
| --- | --- | --- | --- | --- |
| R001 | The controlled path law is generated by history dependent observation kernels and a common decision policy; the backward quantity `G_t` computes the full path Hellinger integral. | General formulation in the manuscript. No efficient evaluation claim follows because the history tree can be exponential. | DERIVED — UNREVIEWED for the broader programme; backward recursion is part of the original manuscript | `manuscript/sequential_testing.tex`; `notes/2026-09-16_controlled_renyi_identities.md`, Sections 1 and 5 |
| R002 | Independent observations need not be identically distributed for Rényi additivity. | Applies to genuine product laws. It does not apply to the action dependent path law merely because kernels are written as a product of conditionals. | ESTABLISHED | `docs/RENYI_APPROXIMATION_PLAN.md`, R2; van Erven and Harremoës, Theorem 28 |
| R003 | Under the same specified policy in both models, the action kernel cancels from the path likelihood ratio on common positive paths. | The policy still changes the distribution of future histories and therefore the future observation kernels. Comparing two different policies requires a separate formula. | DERIVED — UNREVIEWED; CHECKED NUMERICALLY | `notes/2026-09-16_controlled_renyi_identities.md`, Section 1; `docs/CLAIMS.md`, C03 |
| R004 | Prefix Hellinger accumulation satisfies `H_t = H_{t-1} E_{nu_{lambda,t-1}}[z_{lambda,t}(H_{t-1})]`. | Requires a positive prefix integral before normalisation. The increment is a logarithm of a tilted average, not the ordinary average of local divergences. | DERIVED — UNREVIEWED; CHECKED NUMERICALLY | `notes/2026-09-16_controlled_renyi_identities.md`, Section 2; `docs/CLAIMS.md`, C04 |
| R005 | Conditioning the current observation on a selected action gives an exact three probability Rényi correction involving `rho_P`, `rho_Q`, and `rho_lambda`. | Local current observation identity only. It is not automatically a recursion for the entire future process. Ordinary branch probabilities must be positive; tilted zero cases require the stated support convention. | DERIVED — UNREVIEWED; CHECKED NUMERICALLY | `notes/2026-09-16_controlled_renyi_identities.md`, Section 3; `docs/CLAIMS.md`, C05 |
| R006 | For `0 < lambda < 1`, the predictable sum `A_lambda = sum_t C_{lambda,t}` is an unbiased estimator of the path Hellinger gap `1-H_lambda` under the equal mixture construction. | Fixed pair and fixed common policy. The estimator targets the Hellinger gap, not the divergence directly. The simulation label is not a truth label. | DERIVED — UNREVIEWED; CHECKED NUMERICALLY | `notes/2026-09-16_controlled_renyi_identities.md`, Section 4; `docs/CLAIMS.md`, C06 |
| R007 | The conditional expected remaining predictable gain equals `w_lambda(omega_{t-1}) [1-G_t(H_{t-1})]`. | Fixed pair, fixed common policy, and valid conditional histories. This links the estimator directly to the original backward continuation quantity. | DERIVED — UNREVIEWED; CHECKED NUMERICALLY | `notes/2026-09-16_controlled_renyi_identities.md`, Section 5; `docs/CLAIMS.md`, C07 |
| R008 | If the remaining gain is uniformly bounded by `K Delta`, then the predictable estimator has second moment at most `2 K Delta^2`. | Conditional lemma only. It does not provide a useful model specific `K`. Computing `K` from exact `G_t` can be circular. | DERIVED — UNREVIEWED | `notes/2026-09-16_controlled_renyi_identities.md`, Section 5; `docs/CLAIMS.md`, C08 |
| R009 | A genuinely sufficient observed finite state can replace full histories in the exact backward recursion. | The state must determine both conditional models, the policy, and the state update. A hidden state is not automatically an observed sufficient state. | DERIVED — UNREVIEWED; CHECKED NUMERICALLY | `src/controlled_renyi.py`, `finite_state_power`; `docs/CLAIMS.md`, C14 |
| R010 | Same data reuse is a boundary case with no additional full transcript Rényi information when later observations merely reproduce stored information under a common policy, although conditioning on reported actions can change selected law divergence. | This is the precise bridge to `Parallel-Hypothesis`; do not import same data formulas as though new observations were absent. | DERIVED — UNREVIEWED; CHECKED NUMERICALLY | `notes/2026-09-16_controlled_renyi_identities.md`, Section 3; `manuscript/RELATION_TO_PARALLEL_HYPOTHESIS.md` |
| R011 | For a fixed environment, the probability of at least one future wrong edge obeys a direct absorbing backward recursion. | Fixed environment identity only. It is not a robust Bellman theorem and does not justify moving environment or truth suprema inside the recursion. | DERIVED — UNREVIEWED; CHECKED NUMERICALLY in reference examples | `notes/2026-09-16_controlled_renyi_identities.md`, Section 8 |
| R012 | Rectangular conditional kernel uncertainty and globally coupled environment uncertainty are distinct optimisation problems. | Local pasting is valid only for a genuinely rectangular class. A fixed truth map remains coupled across histories reaching the same node. | STRUCTURAL RESULT / MODEL RULE; CHECKED BY COUNTEREXAMPLES | `manuscript/RELATION_TO_PARALLEL_HYPOTHESIS.md`, Section 4; `docs/RENYI_APPROXIMATION_PLAN.md`, Section 8 |
| R013 | The current finite reference implementation reproduces path enumeration, backward recursion, predictable identities, support cases, and selected counterexamples on the included test suite. | Reference computation only. Ordinary floating point and full path enumeration are not a scalable or general guarantee. | CHECKED NUMERICALLY | `results/VALIDATION.md`; `src/controlled_renyi.py`; `tests/test_controlled_renyi.py` |
| R014 | Xing's sequential multiple composite testing theory permits general increasing information functions rather than only linear `n` times a divergence. The optimal expected stopping scale is obtained by inverting the relevant cumulative information function at logarithmic error thresholds. | Xing studies independent streams with possible temporal dependence inside each stream, a common stopping time, and one terminal decision vector. It does not include action controlled future experiments. | ESTABLISHED | Xing, SS-2025-0042, Sections 2 to 4; `notes/2026-09-16_xing_2025_and_controlled_testing_literature_audit.md`, Sections 3 and 6 |
| R015 | Xing separates assumptions for validity from assumptions for asymptotic optimality: almost sure divergence of adaptive evidence from every wrong composite class is enough for almost sure termination and error control, while stronger information growth and complete convergence assumptions are used for matching sample size bounds. | This is a structural proof design principle, not a theorem for the present controlled model. | ESTABLISHED | Xing, Assumptions 1 to 3 and Theorems 1 to 3; literature audit, Section 4 |
| R016 | Temporal dependence and nonlinear information clocks are already handled in sequential composite testing examples, including unequal variance Gaussian data, AR(1), and finite Markov chains. | These are passive data mechanisms. The policy does not change their future laws. | ESTABLISHED | Xing supplement, Section S1; literature audit, Section 9 |
| R017 | Sequential hypothesis testing in which an action or experiment selection changes the distribution of later observations is classical controlled sensing / active hypothesis testing. | Covers fixed and sequential settings under various simple hypothesis models; it does not by itself reproduce the repository's tree of local composite decisions. | ESTABLISHED | Chernoff 1959; Nitinawarat, Atia and Veeravalli 2013; Naghshvar and Javidi 2013; literature audit, Section 10 |
| R018 | Composite hypotheses together with controlled sequential sensing are established: Deshmukh, Veeravalli and Bhashyam give an error controlled, first order asymptotically optimal policy for composite multihypothesis testing in single parameter exponential families. | Sensing controls are distinct from the final hypothesis decision; the objective is expected delay subject to terminal error. | ESTABLISHED | Deshmukh, Veeravalli and Bhashyam 2021; literature audit, Sections 10 and 11 |
| R019 | Controlled Markovian observation models with causal control, memory, nonuniform control cost, and sequential multihypothesis decisions are established. A procedure meeting separate decision risk constraints nonasymptotically while retaining asymptotic optimality is available in that model. | Fixed underlying hypothesis and sensing control framework; not a sequence of history indexed composite binary decisions with pathwise error. | ESTABLISHED | Nitinawarat and Veeravalli 2015; literature audit, Sections 10 and 11 |
| R020 | Sequential multiple testing with non iid or dependent observations is established in several settings. Song and Fellouris use strong laws for local likelihood ratios; Xing and Fellouris treat non iid multistage tests; Chaudhuri and Fellouris allow dependence across streams. | These works do not make an earlier reported local hypothesis decision the control that selects the next composite experiment. | ESTABLISHED | Song and Fellouris 2019; Xing and Fellouris 2024; Chaudhuri and Fellouris 2024; literature audit, Section 10 |
| R021 | Rényi divergence rates for fixed hidden Markov models can be characterised using a Markov representation and eigenvalues of an associated operator. | Long horizon dependent model result. It does not provide a finite horizon controlled composite testing theorem or policy result. | ESTABLISHED | Fuh, Fuh, Liu and Wang 2025; literature audit, Section 10 |
| R022 | Finite sample active hypothesis testing results exist, including fixed horizon active testing bounds and a 2026 nonasymptotic expected stopping time bound for an elimination based active testing method. | The available results checked here are not the repository's finite sample composite controlled pathwise problem. | ESTABLISHED | Kartik, Nayyar and Mitra 2022; Lin, Nguyen, Xu and Ruchkin 2026; literature audit, Section 10 |
| R023 | Xing gives a universal global misclassification bound `binom(K,s)(M-1)^s exp(-a_s)` and corresponding thresholds, while recommending importance sampling for sharper finite sample calibration. | Relies on the simultaneous stream error structure. It cannot be substituted directly for selected path error. | ESTABLISHED | Xing, Theorem 2 and Section 5; literature audit, Sections 7 and 8 |
| R024 | Importance sampling that changes selected components towards their closest wrong alternatives is effective for calibrating rare sequential misclassification events. | The controlled tree analogue must use a coherent controlled change of measure and preserve policy and environment coupling. | ESTABLISHED as a method in Xing's setting; adaptation here is OPEN | Xing, Section 5; literature audit, Section 8 |
| R025 | The isolated iid single-node finite-sample composite binary testing problem, including achievability and converse bounds for the optimal Type II error under a Type I constraint, is prior solved work and is not an open problem in this repository. | Applies to the assumptions of the prior single-node theory. The sequential project must import this result rather than rederive it. | ESTABLISHED BY PRIOR WORK | `SB001`; Vera Sigüenza and Esposito, *Finite Sample Bounds for Composite Hypothesis Testing* |
| R026 | For a two-node singleton problem conditioned on reaching branch `A_0=1`, the Rényi divergence between the selected joint laws of old and new data decomposes exactly into: the original node-0 Rényi divergence; a branch-selection correction involving `alpha_0`, `beta_0`, and the tilted reach `rho_{lambda,0}`; and a dependent new-data term equal to a logarithm of a branch-selected tilted expectation of the conditional Rényi integral. | Requires positive branch reach under both laws and positive tilted reach. No iid or independence assumption is used for the new block. The branch-selection factor overlaps R005; the explicit dependent new-data contribution is the key additional two-node term. | DERIVED — UNREVIEWED; no numerical check yet | `notes/2026-09-16_two_node_singleton_renyi_decomposition.md`; overlaps R004 and R005 |

## Failure and counterexample ledger

| ID | Failed statement or route | What is known | Consequence: do not repeat this route without changing assumptions | Authoritative location |
| --- | --- | --- | --- | --- |
| F001 | Positive probabilities, bounded likelihood ratios, and a short horizon should uniformly bound the direct predictable estimator's relative variance. | False. In the two stage rare action example the relative variance is `1/tau - 1` while likelihood ratios remain bounded. | Any variance theorem needs additional control of rare informative branches or a different estimator. | `docs/RENYI_APPROXIMATION_PLAN.md`, Section 6; `docs/CLAIMS.md`, C09 |
| F002 | F001 implies that no efficient algorithm can exist. | Not established. Exact action integration removes the variance in the rare action example. | Do not turn the rare action counterexample into an algorithmic impossibility claim. Study branch integration and count its cost. | `docs/CLAIMS.md`, C10; `docs/RENYI_APPROXIMATION_PLAN.md`, Route B |
| F003 | A fixed node truth map can be maximised independently at every history reaching that node. | False. A two history example changes the legitimate worst case error from `1/2` to the invalid value `1` if the truth label is allowed to vary by history. | Keep `vartheta(v)` fixed at the node unless the model itself is changed. Do not move this supremum inside history updates. | `notes/2026-09-16_controlled_renyi_identities.md`, Section 8; `docs/CLAIMS.md`, C11 |
| F004 | A coupled environment parameter can be replaced by independent local worst case choices. | False in general. Rectangular enlargement can change, and in examples destroy, the separation present in every coherent model. | Preserve global parameter or latent model consistency. Local minimisation is valid only after proving rectangularity. | `docs/RENYI_APPROXIMATION_PLAN.md`, Section 8; `docs/CLAIMS.md`, C12 |
| F005 | Same data reuse by itself increases full transcript Rényi divergence under a common policy. | False. If no new information is generated, the full transcript divergence remains that of the original data, although selected conditional laws may change. | Treat `Parallel-Hypothesis` as a boundary case, not as evidence of new information accumulation. | `docs/CLAIMS.md`, C13; `notes/2026-09-16_controlled_renyi_identities.md`, Section 3 |
| F006 | A relative estimate of the Hellinger gap below order one automatically yields a uniform relative estimate of Rényi divergence. | False without overlap control. The logarithmic map becomes badly conditioned as the Hellinger integral approaches zero. | State an overlap promise or use a different accuracy target. | `docs/RENYI_APPROXIMATION_PLAN.md`, Section 9; `docs/CLAIMS.md`, C15 |
| F007 | Pairwise controlled path Rényi divergence is already the minimax probability of any wrong edge. | Not established. These are different objects and require a separate testing theorem. | Do not relabel a pairwise divergence approximation as a composite path risk bound. | `docs/CLAIMS.md`, C19; `docs/RENYI_APPROXIMATION_PLAN.md`, Section 8 |
| F008 | Local Type I and Type II guarantees alone determine the complete sequential path law. | False in the same data predecessor project and structurally unsafe here; the new data version remains a candidate early theorem rather than an established current theorem. | Do not propagate global path risk by multiplying or otherwise using only nominal local errors. | `manuscript/RELATION_TO_PARALLEL_HYPOTHESIS.md`, Section 3 |
| F009 | Locally tilted simulation is the same as simulation from the globally tilted controlled path law. | False. The global tilted transition contains the continuation factor `G_{t+1}/G_t` and generally reweights actions. | Do not claim exact global tilted sampling from locally normalised kernels. Using exact `G_t` in a fast algorithm is circular unless its cost is counted. | `notes/2026-09-16_controlled_renyi_identities.md`, Section 6 |
| F010 | Because the model is a finite decision tree, a backward pass is automatically linear in the horizon. | False as a complexity statement. The number of histories or nodes can itself grow exponentially with horizon. | State complexity in number of states, histories, branches, or oracle calls. Never hide tree size in `O(T)`. | `docs/RENYI_APPROXIMATION_PLAN.md`, Sections 3 and 7 |
| F011 | Action dependent future observation laws are themselves a novel feature of sequential hypothesis testing. | False as a novelty claim. Controlled sensing and active sequential hypothesis testing study exactly the ability to choose actions or experiments that alter future observation laws. | Any novelty argument must concern the repository's more specific decision tree, composite, pathwise, or finite sample Rényi structure. | R017; literature audit, Section 10 |
| F012 | Composite hypotheses combined with controlled sequential sensing are absent from the literature. | False. Deshmukh, Veeravalli and Bhashyam 2021 treat sequential controlled sensing for composite multihypothesis testing. | Do not claim novelty from the combination of composite hypotheses and observation control alone. | R018; literature audit, Section 10 |
| F013 | Temporal dependence or controlled Markov memory is absent from sequential hypothesis testing theory. | False. Passive temporal dependence and controlled Markovian observations are both established. | Novelty must not be based on removing iid assumptions or adding Markov memory alone. | R016, R019, R020 |
| F014 | Xing's simultaneous stream threshold and sum of smallest information functions can be used directly for the repository's path error. | Not justified. Xing has independent parallel streams and one terminal decision vector; our procedure follows one action selected path and earlier errors alter later experiments. | Any imported threshold or information sum requires a new pathwise derivation. | R014, R023; literature audit, Sections 5 to 7 |
| F015 | A sensing control policy from active hypothesis testing can be identified without qualification with the repository's edge decision. | Not generally. Standard active testing usually separates the experiment selection action from the final hypothesis decision, whereas here `A_t` is both a reported binary conclusion and the action selecting the next node. | Preserve the semantic distinction and prove any reduction explicitly. | literature audit, Sections 10 to 13 |
| F016 | A hidden Markov Rényi divergence rate result supplies a finite sample controlled path theorem. | False as an implication. The HMM result characterises long horizon divergence for fixed dependent models. | Use it only as dependent Rényi background or for model specific asymptotics after control is fixed. | R021 |
| F017 | Treat the isolated iid single-node composite error problem as an unsolved task and derive it again. | Duplicate work. The finite-sample local achievability and converse problem is already solved in the prior paper recorded as `SB001` and `R025`. | Stop immediately unless the task explicitly changes an assumption, seeks a strengthening, or requests independent verification. The sequential research starts from propagation of these local errors. | `SB001`; `R025` |

## Attempted and reusable method ledger

| ID | Method | Current outcome | Next permissible use | Location |
| --- | --- | --- | --- | --- |
| M001 | Full path enumeration | Exact small model reference; exponential in horizon. | Validation, counterexamples, and tiny benchmark models only. | `src/controlled_renyi.py`, `prefix_laws` and `path_power` |
| M002 | Exact backward `G_t` recursion on full histories | Exact but can still be exponential in the history space. | Baseline and reference computation; exploit only a proved sufficient state for compression. | `src/controlled_renyi.py`, `backward_power` |
| M003 | Predictable Monte Carlo gap estimator | Unbiased, but can have arbitrarily large relative variance because of rare informative actions. | Reuse only with an explicit variance condition or as a baseline against branch integration. | R006, R007, F001 |
| M004 | Explicit integration over selected action branches | Removes the two stage rare action sampling variance; general cost can grow as `2^b` for `b` integrated binary stages. | Immediate next research route on two to four stage examples, with complete cost accounting. | `docs/RENYI_APPROXIMATION_PLAN.md`, Route B; `prompts/01_controlled_renyi_foundations.md` |
| M005 | Local tilted path sampling | Gives a valid importance identity but not samples from the globally tilted law. Weight variance can remain large. | Compare against M003 and M004 on explicit controlled model classes. | `notes/2026-09-16_controlled_renyi_identities.md`, Section 6 |
| M006 | Exact finite state recursion | Effective when a genuinely sufficient observed state exists. | Use as the main tractable exact control class and as a benchmark for approximation methods. | R009 |
| M007 | General information function / information clock asymptotics | Established and powerful in passive non iid sequential composite testing. | Develop a controlled analogue only after defining the coherent pair or composite object whose evidence growth is measured. Do not assume linear growth. | R014 to R016; literature audit, Sections 3, 4 and 13 |
| M008 | Adaptive log likelihood versus generalised wrong class likelihood | Gives sequential evidence that supports error control and first order optimality in Xing's composite setting. | Candidate local statistic at a node when conditional models admit likelihood optimisation. Requires a new controlled and pathwise proof. | Xing 2025; literature audit, Sections 4 and 12 |
| M009 | Rare event importance sampling towards closest wrong hypotheses | Effective in Xing's finite sample calibration. | Construct a coherent change of measure for wrong paths or adverse environments while preserving the policy. Compare against M003 to M005. | R024; literature audit, Section 8 |
| M010 | Chernoff style controlled sensing / active testing policy design | Large established literature with asymptotic lower bounds and dynamic programming viewpoints. | Use as the baseline for global policy design after distinguishing sensing control from reported edge decisions. | R017 to R019; literature audit, Sections 10 to 13 |
| M011 | Markov operator / spectral Rényi rate analysis | Established for fixed HMMs. | Candidate tool for long horizon controlled finite state models after a policy is fixed or an augmented state is justified. Not a finite sample replacement for `G_t`. | R021 |

## Open problem ledger

| ID | Open problem | Dependency / warning | Current next location |
| --- | --- | --- | --- |
| O001 | Prove or refute a useful variance bound for action integrated estimation on an explicit controlled class. | Must survive F001 and include branch integration cost. | `prompts/01_controlled_renyi_foundations.md` |
| O002 | Obtain an explicit model based bound for the remaining gain constant `K`. | An expression requiring exact `G_t` everywhere is not an efficient theorem. | `docs/RENYI_APPROXIMATION_PLAN.md`, Sections 5 and 7 |
| O003 | Develop a general finite horizon approximation algorithm with an explicit accuracy and work guarantee. | No linear horizon result is currently established; tree size and conditional oracle cost must be counted. | `docs/RENYI_APPROXIMATION_PLAN.md` |
| O004 | Extend the already solved single-node theory `SB001` only as needed to a conditional or history-dependent node, and connect the resulting nodewise Rényi quantities to the local composite Type I and Type II errors. | The isolated iid node is solved and must not be rederived. Any new theorem must identify precisely which sequential or dependence assumption prevents direct use of `SB001`. | Later Stage 6 work; `SB001` |
| O005 | Connect local testing guarantees to the minimax path risk `R_T`. | F007 and F008 block naive substitutions. This is part of UQ001. | Later Stage 6 work |
| O006 | Characterise minimax recursion separately for rectangular and coupled environment classes. | F003 and F004 must remain enforced. | `manuscript/RELATION_TO_PARALLEL_HYPOTHESIS.md`; future manuscript development |
| O007 | Determine whether a globally optimal testing policy admits a useful dynamic characterisation. | Local testing optimality need not imply global optimality. Compare explicitly with active sequential hypothesis testing before claiming novelty. | R017 to R019; future work after fixed policy evaluation |
| O008 | Complete a novelty audit for predictable Hellinger process identities and controlled path formulations. | Do not label R003 to R008 novel before this audit. The active testing literature in R017 to R022 is now mandatory background. | Literature stage in `prompts/01_controlled_renyi_foundations.md` |
| O009 | Formalise positive reach, rectangular environments, and coupled environments directly in the manuscript. | Proposed in the relation note, not yet merged into the scientific formulation. | `manuscript/RELATION_TO_PARALLEL_HYPOTHESIS.md`, Section 9 |
| O010 | Define the correct controlled information function or information process for history dependent composite experiments. | Must reduce to Xing's information clock in passive cases and respect coherent environment coupling. Do not assume `nD`. | R014 to R016; M007 |
| O011 | Perform a theorem level novelty audit against controlled sensing, active sequential hypothesis testing, controlled Markov observations, and composite controlled sensing. | The present search establishes strong neighbouring results but not exhaustive absence of a direct theorem. | `notes/2026-09-16_xing_2025_and_controlled_testing_literature_audit.md` |
| O012 | Determine the mathematical effect of requiring the reported local decision itself to be the control selecting the next experiment, rather than introducing a separate sensing action. | F015 blocks silent identification with classical active testing. This distinction may be central to the project. | Future formulation and controlled examples |
| O013 | Construct an importance sampling law for rare wrong path events under action dependent observations. | Proposal must be a coherent controlled path law; rectangular and coupled cases differ. | M009; F004 |
| O014 | Develop a finite-sample pathwise error propagation theorem for UQ001, using the already solved local theory `SB001` as nodewise input wherever its assumptions apply and the exact Hellinger / Rényi recursion where sequential dependence requires it. | The local iid achievability and converse problem is not the missing theorem. The missing bridge is from nodewise guarantees to global sequential error when decisions alter future problems. | O004, O005; `SB001`; future theorem work |
| O015 | Use a controlled finite state Markov model as the first model class where exact `G_t`, active control literature, and possible asymptotic information clocks can all be compared. | Must preserve observed state sufficiency and the truth map. | R009, R019, R021 |
| O016 | Characterise or bound the dependent new-data bottleneck in R026: the branch-selected tilted expectation of the conditional Rényi integral, determine how it iterates over further nodes, and then lift the identity from singleton pairs to composite converse bounds. | Do not rederive the branch-selection correction R005. The genuinely new difficulty is the non-tensorising future-data term and its interaction with the selected tilted law. | `notes/2026-09-16_two_node_singleton_renyi_decomposition.md`; R026 |

## Literature boundary established on 16 September 2026

The detailed audit is `notes/2026-09-16_xing_2025_and_controlled_testing_literature_audit.md` and the source record for Xing is `sources/SS-2025-0042/SOURCE.md`.

The search establishes that the following broad ingredients are already in the literature and must not be presented as new on their own:

* action controlled future observation laws in sequential testing;
* adaptive and causal sensing policies;
* controlled Markovian observations;
* composite hypotheses with controlled sensing;
* temporal dependence and non iid sequential testing;
* general nonlinear information growth functions;
* dependent stream sequential multiple testing;
* finite sample active testing bounds in some models;
* Rényi divergence rates for hidden Markov models.

No direct match was located in this search for the complete combination used by this repository: a tree of local composite binary tests in which each reported edge decision is also the control selecting the next experiment, with history dependent future composite classes, fixed node truth semantics, coherent uncertainty across the path, pathwise wrong edge risk, and finite sample Rényi analysis. Record this as `NO DIRECT MATCH LOCATED`, not `NOVEL`.

## Cross project results that must not be rediscovered here

`Parallel-Hypothesis` remains a separate repository. Its same data results may be used as boundary checks but should not be rederived inside this project unless needed for an explicit reduction theorem.

The following ideas are already available there:

* exact same data path representation and selected law formulas;
* local nominal error insufficiency for global path response;
* rectangular path event propagation;
* same data Rényi selection corrections involving `rho_P`, `rho_Q`, and `rho_lambda`;
* fixed realised simple path converse and achievability recursions.

The current project must only derive what changes when genuinely new, action dependent observations are introduced.

See `manuscript/RELATION_TO_PARALLEL_HYPOTHESIS.md` for the import boundary.

## End of task update rule

Every completed scientific task must append or revise ledger entries with:

* a stable ID;
* the exact statement or failed statement;
* hypotheses and scope;
* status;
* authoritative file or commit;
* whether independent review was performed;
* whether numerical checks exist;
* if failed, the smallest known counterexample or obstruction;
* if superseded, the replacement ID.

The task is not complete until `docs/RESEARCH_LEDGER.md`, `CURRENT_STATUS.md`, and, when claim status changes, `docs/CLAIMS.md` are consistent.
