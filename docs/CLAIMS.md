# Claims register

Date: 16 September 2026. Updated: 23 September 2026. Local derivations are supported by working proofs and finite numerical checks where stated, not by default by independent review or a novelty determination.

The mandatory historical do-not-duplicate index is `docs/RESEARCH_LEDGER.md`.

| ID | Claim | Status |
| --- | --- | --- |
| C01 | Independent nonidentical laws give additive Rényi divergence | Established literature, van Erven and Harremoës Theorem 28 |
| C02 | `G_t` computes the full controlled path integral | Original manuscript; checked against enumeration |
| C03 | A common policy cancels from path likelihood ratios | Derived on common positive paths; policy still changes future histories |
| C04 | Prefix accumulation uses a tilted expectation of the local integral | Derived; tested |
| C05 | A selected current observation has the three-probability Rényi correction | Derived with support conditions; tested |
| C06 | The controlled predictable estimator has mean `1-H` for orders below one | Derived; tested |
| C07 | Remaining gain equals posterior weight times `1-G_t` | Derived; tested |
| C08 | Remaining gain bounded by `K Delta` implies second moment at most `2K Delta^2` | Conditional lemma only |
| C09 | Positivity and bounded likelihood ratios uniformly bound direct-estimator relative variance | False; rare-action example |
| C10 | Rare-action example prevents every efficient algorithm | Not established; explicit branch integration defeats that example |
| C11 | A fixed truth map can be maximised separately at each history | False |
| C12 | Coupled environment parameters can be replaced by independent local choices | False |
| C13 | Same-data reuse increases full-transcript Rényi divergence under common policy | False when no new information is generated |
| C14 | A small sufficient observed state gives an exact smaller recursion | Derived finite reference, conditional on genuine sufficiency |
| C15 | Relative gap error always transfers uniformly to relative `D` below order one | False without overlap control |
| C16 | Relative gap error transfers to relative `D` above order one under the stated logarithmic conversion | Elementary; says nothing about estimator variance |
| C17 | Useful explicit `K` for general controlled dependent laws | Open |
| C18 | General linear-horizon approximation or optimal-policy theorem | Not established |
| C19 | Pairwise path divergence determines minimax any-error risk | Not established |
| C20 | Predictable identities are novel | Not asserted |
| C21 | Sequential testing with actions changing future observation laws is established literature | Controlled sensing / active testing; not a novelty claim |
| C22 | Composite hypotheses with controlled sequential sensing are established | Deshmukh, Veeravalli and Bhashyam 2021 |
| C23 | Controlled Markovian observations with causal sensing and sequential risk constraints are established | Nitinawarat and Veeravalli 2015 |
| C24 | General nonlinear information functions can replace linear `n`-times-divergence scales in sequential composite testing | Xing SS-2025-0042 |
| C25 | Temporal dependence, non-iid observations and dependence across streams already occur in sequential testing theory | Established neighbouring literature |
| C26 | The complete combination in this repository has no direct theorem match in the targeted searches | NO DIRECT MATCH LOCATED, not a novelty claim |
| C27 | Requiring the reported local hypothesis decision itself to select the next experiment may distinguish this model from standard active testing | Open structural question |
| C28 | In the two-node singleton branch `A_0=1`, the selected joint-law Rényi divergence decomposes into node-0 divergence, branch-selection correction, and dependent future-data term | Correct mapping to R005 plus the established chain rule; now also checked on finite dependent examples in both directions |
| C29 | The R026 future-data term is exactly the common-input conditional Rényi divergence of the future kernels under the branch-selected tilted old-data law | ESTABLISHED LITERATURE mapping; Polyanskiy and Wu §7.12; Cai and Verdú 2019 |
| C30 | Rényi divergence has an exact chain rule for arbitrary joint dependent laws using a Rényi-tilted marginal as the conditioning law | ESTABLISHED; Polyanskiy and Wu Eq. (7.77)–(7.78) |
| C31 | The exact Rényi chain rule iterates across general dependent transition kernels using tilted prefix laws; ordinary tensorisation is only a special product case | ESTABLISHED by iteration; explicit full-chain theorem also appears in Lei Yu’s preprint monograph |
| C32 | Adaptive simple channel discrimination already accumulates Rényi/Hellinger-transform information under adaptive observation laws | ESTABLISHED; Hayashi 2009; simple hypotheses and asymptotic error exponents |
| C33 | Composite adaptive channel discrimination does not settle this project: the checked Bergh–Datta–Salzmann theory still requires independence and leaves important classical non-convex adaptive exponent questions open | ESTABLISHED BOUNDARY; arXiv:2303.02016v2 |
| C34 | Convert the exact selected Rényi chain into finite sample converse recursion and global error propagation | PARTIALLY ANSWERED by C35 to C38 for the stated singleton path and coherent comparison. General minimax tradeoffs and matching achievability remain open. |
| C35 | The source equations (4) and (48), after substitution of R026, give explicit local selected converses in both Rényi directions | DERIVED, NOT INDEPENDENTLY REVIEWED; finite checks against exact NP errors; fixed first rule, correct separate tilts and actual pair errors required; R033 |
| C36 | The alternative branch survival factor cancels when the local converse is converted into the (1,1) path error | DERIVED, NOT INDEPENDENTLY REVIEWED; checked numerically; no independence used; R034 |
| C37 | Uniform conditional information limits give a converse for successive all ones decisions under a coherent null comparison, using conditional Type I budgets | DERIVED, NOT INDEPENDENTLY REVIEWED; four stage finite check; not an arbitrary truth map result; R035 |
| C38 | Inverting those upper information limits yields necessary n and m conditions without assuming iid, and coherent pair selection gives a restricted composite lower bound | DERIVED, NOT INDEPENDENTLY REVIEWED; necessary only, not sufficient; R036 |
| C39 | The explicitly stated correlated Gaussian model gives closed form Rényi information, order optimisation and necessary sample counts | DERIVED, NOT INDEPENDENTLY REVIEWED; covariance inverse and count checks passed; dependence remains after conditioning; R037 |
| C40 | Generalised Holder gives a nonuniform upper bound on the selected contribution in terms of averaged higher order conditional likelihood ratio moments | DERIVED, NOT INDEPENDENTLY REVIEWED; finite dependent checks; finiteness of these moments is sufficient, not necessary; R038 |
| C41 | Local integral comparison functions dominate the backward moment and bound its selected average without being uniformly bounded | DERIVED, NOT INDEPENDENTLY REVIEWED; reuses the existing recursion at the original order; inequalities must be verified from the kernels; R039 |
| C42 | In the new Gaussian feedback example the selected contribution and an explicit n,m bound can be finite despite unbounded pointwise conditional divergences | DERIVED, NOT INDEPENDENTLY REVIEWED; checked against full joint Gaussian integration; integrability thresholds retained; R040 |
| C43 | Maximising the selected contribution over all positive reach first tests subject only to a Type I upper budget recovers the essential upper bound of the pointwise conditional divergence under the root tilt | DERIVED, NOT INDEPENDENTLY REVIEWED; finite alphabet check; fixed kernels; no claim of finite uniformity when that divergence is unbounded; R041 |
| C44 | The contribution is nondecreasing in m for a coherent prefix process and fixed n and first test, but need not be monotone in n across changed experiments | Consequence of the established chain rule with updated full prefix tilts; finite checks; R042 |
| C45 | Root power yields an explicit positive lower tilted reach when it is bounded below and the root moment is finite | Elementary Holder consequence; finite checks; R043 |
| C46 | A minimising Renyi projection does not directly upper bound the selected singleton contribution, but a Holder change of measure through a tractable reference law gives an upper bound with a Renyi mismatch penalty; using the unselected root tilt bounds that penalty by minus log tilted branch reach | DERIVED, NOT INDEPENDENTLY REVIEWED; fixed singleton pair and first test; the remaining reference-law exponential moment must still be controlled; R044 |

Historical validation for the 16 September selected converse task: 47 passing local test methods, comprising the 30 existing methods and 17 new methods in `tests/test_selected_converse.py`. These are finite deterministic consistency checks, not an independent proof review, a novelty audit, a general numerical guarantee or a remote CI run. See `results/2026-09-16_selected_converse_checks.json` and `notes/2026-09-16_selected_renyi_converse_sample_complexity.md` for exact scopes.

Validation for the 23 September extension: fifteen standalone local deterministic methods passed, not a rerun of the older suite. No production code or original user notes were modified. Details are in `results/2026-09-23_nonuniform_information_verification.json` and proofs are in `notes/2026-09-23_nonuniform_selected_information_bounds.md`. F022 to F024 record the integrability and uniformity limitations. These new claims do not assert matching achievability, exact minimax sample complexity, or novelty of the underlying mathematical methods.
