# Task 01: controlled identities and action integration

Read AGENTS.md and the scientific files it lists. Work on a new descriptive research branch unless the owner specifies otherwise. Do not modify the original manuscript or merge without instruction.

## Objective

Determine whether integrating selected actions improves approximation of the existing controlled path Rényi gap, with a useful error and work bound. This is not a generic mixture study detached from the decision tree.

## Sequence

1. Independently review the working note. Check common policy cancellation, prefix tilting, local branch selection, predictable unbiasedness, remaining gain, the conditional second moment bound and logarithmic conversion. State exactly which histories and supports each formula permits. Record any correction before changing code.
2. Reproduce all 30 tests. Keep the rare action, zero reach, same data, coupled parameter and fixed truth map examples. Add a direct test of the fixed environment any error recursion against path enumeration. Do not turn it into a robust Bellman theorem.
3. Implement a first action integration method on the two stage rare action example, then on a three stage version with nontrivial observation history dependence. Evaluate the same observable path functional as the direct predictable estimator.
4. At an internal history use the posterior mixture weights. For independent branch rollouts, sample each model label from that posterior and keep it fixed within that rollout. Add a regression example showing that restarting each continuation with a fair model label gives the wrong answer when the posterior is not fair.
5. Compute means and second moments by enumerating all short continuations before running performance simulations. Account for branch probabilities, allocation and all additional conditional oracle calls. Compare zero, one and two integrated action stages. Do not hide a factor 2^b in an unspecified constant.
6. Use lambda values 1/4, 1/2 and 3/4 and horizons two to four initially. Include equal laws, nearby laws, deterministic actions, rare informative actions, dependence on earlier observations within the same tree node, and a genuinely sufficient finite state control.
7. Audit the closest prior work. R1 and R2 have been read for the indicated results; R3 to R6 have only the stated limited reading depth. In particular compare filtered Monte Carlo and predictable Hellinger processes, and distinguish additive autoregressive TV estimation from relative Rényi approximation.

## Deliverables and stopping condition

A dated reviewed derivation note, an action integration implementation with tests, exact moment comparisons, a full work count, and updated claims and status. Record the source commit and software environment. Publish completed milestones with CURRENT_STATUS.md and results/checkpoint.json; do not leave the only copy in a temporary workspace.

Conclude with a proved improvement for an explicit controlled class, a counterexample to the proposed improvement, or a precisely stated unresolved condition. Numerical success alone does not establish a uniform variance theorem. Keep composite optimisation and policy design for later tasks, while preserving their model constraints now.
