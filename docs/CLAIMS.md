# Claims register

Date: 16 September 2026. Local derivations are supported by working proofs and finite numerical checks, not independent review or a novelty determination.

| ID | Claim | Status |
| --- | --- | --- |
| C01 | Independent nonidentical laws give additive Rényi divergence | Established literature, R2 Theorem 28 |
| C02 | G_t computes the full controlled path integral | Already in the original manuscript; checked against enumeration |
| C03 | A common policy cancels from path likelihood ratios | Derived, on common positive paths; its control of future data remains |
| C04 | Prefix accumulation uses a tilted expectation of the local integral | Derived in note Section 2; tested |
| C05 | A selected current observation has the three probability correction | Derived with support conditions in note Section 3; randomised branch test |
| C06 | The controlled predictable estimator has mean 1-H for orders below one | Derived in note Section 4; tested including one model zero reach |
| C07 | The remaining gain equals w times (1-G_t) | Derived in note Section 5; every common prefix checked in a small model |
| C08 | A remaining gain bound by K Delta implies second moment at most 2K Delta squared | Conditional lemma proved in note Section 5; not a model specific theorem |
| C09 | Positivity and bounded likelihood ratios uniformly bound the direct estimator's relative variance | False: rare action example gives 1/tau minus 1 |
| C10 | The rare action example prevents every efficient algorithm | Not claimed; explicit action integration solves it |
| C11 | A fixed truth map can be maximised separately at each history | False in general; different histories can reach the same node |
| C12 | Coupled environment parameters can be replaced by independent local choices | False in general; the rectangular enlargement changes separation |
| C13 | Same data reuse increases full transcript divergence under a common policy | False when no new information is generated; selection can change a conditioned law |
| C14 | A small sufficient state gives an exact smaller recursion | Derived finite reference, conditional on sufficiency of both kernels and policy |
| C15 | Relative gap error always transfers uniformly to relative D below order one | False without overlap control; plan gives a sufficient promise |
| C16 | Relative gap error transfers to relative D above order one | Elementary logarithmic concavity; does not establish estimator variance |
| C17 | Useful explicit K for general controlled dependent laws | Open; no such result established |
| C18 | General linear horizon approximation or optimal policy theorem | Not established |
| C19 | Pairwise path divergence determines the repository's minimax any error risk | Not established; a separate statistical connection is required |
| C20 | The predictable identities are novel | Not asserted; filtered Monte Carlo and Hellinger process audit pending |

The 30 local test methods are regression checks, not a proof of C17 or C18. There has been no remote CI run or broad stochastic comparison. Read the research plan and working note for precise hypotheses rather than treating this short register as theorem statements.
