# Experimental specification

Completed so far: the local regression tests in `tests/`. Planned: a stochastic comparison after the independent review and exact action integration checks in Task 01.

Begin at lambda = 1/4, 1/2 and 3/4 with horizons small enough to enumerate complete histories. Treat orders above one separately.

| Family | Required comparison |
| --- | --- |
| Nonidentical independent observations | Additive divergence versus full transcript calculation |
| Controlled observed models | G_t recursion versus path enumeration and sufficient state recursion |
| Rare informative actions | Direct estimator's 1/tau second moment ratio versus action integration |
| Same node, different observation histories | Detect invalid state compression and truth map optimisation |
| Same data boundary | Unchanged full transcript information versus branch selection correction |
| Exact zeros and deterministic policies | Positive reach discipline and skipped impossible branches |
| Controlled mixtures and hidden observations | Observable divergence, filtering cost and continuation variance |
| Coupled and rectangular uncertainty | Preserve complete environment consistency |

Record every observation probability, policy probability, state update, truth map restriction, order, horizon, algorithm, seed where relevant, sample allocation, variance, reference value, runtime, error criterion and commit. Compare statistical interval coverage using independent repetitions. Do not infer an accuracy guarantee from the seeded trajectory consistency checks already in the unit suite.

Use increased precision for small gaps and low overlap. Report adverse cases. Keep statistical, numerical, model approximation and optimisation errors separate. Do not store large generated path tables in Git.
