# Claims register

Date: 16 September 2026. Local derivations are supported by working proofs and finite numerical checks where stated, not by default by independent review or a novelty determination.

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
| C28 | In the two-node singleton branch `A_0=1`, the selected joint-law Rényi divergence decomposes into node-0 divergence, branch-selection correction, and dependent future-data term | Correct; the future-data term is now identified by C29 and the whole identity follows from R005 plus the established chain rule |
| C29 | The R026 future-data term is exactly the common-input conditional Rényi divergence of the future kernels under the branch-selected tilted old-data law | ESTABLISHED LITERATURE mapping; Polyanskiy and Wu §7.12; Cai and Verdú 2019 |
| C30 | Rényi divergence has an exact chain rule for arbitrary joint dependent laws using a Rényi-tilted marginal as the conditioning law | ESTABLISHED; Polyanskiy and Wu Eq. (7.77)–(7.78) |
| C31 | The exact Rényi chain rule iterates across general dependent transition kernels using tilted prefix laws; ordinary tensorisation is only a special product case | ESTABLISHED by iteration; explicit full-chain theorem also appears in Lei Yu’s preprint monograph |
| C32 | Adaptive simple channel discrimination already accumulates Rényi/Hellinger-transform information under adaptive observation laws | ESTABLISHED; Hayashi 2009; simple hypotheses and asymptotic error exponents |
| C33 | Composite adaptive channel discrimination does not settle this project: the checked Bergh–Datta–Salzmann theory still requires independence and leaves important classical non-convex adaptive exponent questions open | ESTABLISHED BOUNDARY; arXiv:2303.02016v2 |
| C34 | The current mathematical bottleneck is not dependent Rényi algebra itself, but converting the exact branch-selected conditional Rényi chain into finite-sample local/composite converse recursion and ultimately global error propagation | OPEN; this is the revised O016/O017 direction |

The earlier 30 local test methods remain regression checks, not proofs of C17, C18 or C34. No new code was changed in the conditional Rényi literature audit, so those tests were not rerun for this task.
