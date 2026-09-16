# Conditional Rényi chain rule literature audit

Date: 16 September 2026.

Status: literature audit completed for the specific bottleneck recorded in R026. The main conclusion is that the exact divergence algebra is established literature. The unresolved research problem is the testing and minimax error propagation built on top of that algebra.

## Question audited

R026 introduced, for the realised branch `A_0=1`, the dependent new-data term

\[
T_{\lambda,1}
:=
\frac{1}{\lambda-1}
\log
\mathbb E_{\nu_{\lambda,0}^{(1)}}
\left[
\exp\!\left((\lambda-1)
D_\lambda\bigl(Q_1(\cdot\mid X_0^n,1)\|P_1(\cdot\mid X_0^n,1)\bigr)
\right)
\right].
\]

Here `nu_{lambda,0}^{(1)}` is the branch-selected Rényi tilted law of the old data, and `P_1(.|x,1)` and `Q_1(.|x,1)` are the conditional laws of the new data after old data `x` and branch 1.

The audit asked whether this logarithm of a tilted expectation is a new unresolved object, whether exact chain rules exist for dependent laws, and whether the resulting testing problem has already been solved.

## 1. The R026 new-data term is an established conditional Rényi divergence

Polyanskiy and Wu define the common-input conditional Rényi divergence by

\[
D_\lambda(P_{Y|X}\|Q_{Y|X}\mid R_X)
:=
D_\lambda(R_XP_{Y|X}\|R_XQ_{Y|X}).
\]

Equivalently,

\[
D_\lambda(P_{Y|X}\|Q_{Y|X}\mid R_X)
=
\frac{1}{\lambda-1}
\log
\mathbb E_{X\sim R_X}
\left[
\exp\!\left((\lambda-1)
D_\lambda(P_{Y|X=X}\|Q_{Y|X=X})
\right)
\right].
\]

With

\[
R_X=\nu_{\lambda,0}^{(1)},
\quad
P_{Y|X}=Q_1(\cdot\mid X,1),
\quad
Q_{Y|X}=P_1(\cdot\mid X,1),
\]

we obtain exactly

\[
T_{\lambda,1}
=
D_\lambda
\left(
Q_1(\cdot\mid\cdot,1)
\|P_1(\cdot\mid\cdot,1)
\mid\nu_{\lambda,0}^{(1)}
\right).
\]

Thus the third term in R026 is not a new divergence-like object. It is the standard common-input conditional Rényi divergence.

Cai and Verdú study this conditional Rényi divergence on general alphabets. Bleuler, Lapidoth and Pfister are important for terminology: several inequivalent quantities in the literature are called conditional Rényi divergence. For this project the relevant one is the common-input / joint-law definition above, not an arithmetic average of pointwise Rényi divergences.

Primary references:

* Y. Polyanskiy and Y. Wu, *Information Theory: From Coding to Learning*, Section 7.12, Definition and Eq. (7.77), prepublication version dated 16 August 2024, https://people.lids.mit.edu/yp/homepage/data/itbook-export.pdf
* C. Cai and S. Verdú, “Conditional Rényi Divergence Saddlepoint and the Maximization of α-Mutual Information,” *Entropy* 21(10):969, 2019, doi:10.3390/e21100969.
* C. Bleuler, A. Lapidoth and C. Pfister, “Conditional Rényi Divergences and Horse Betting,” *Entropy* 22(3):316, 2020, doi:10.3390/e22030316.

## 2. The exact two-variable chain rule is already known

Polyanskiy and Wu give the exact identity

\[
D_\lambda(P_{A,B}\|Q_{A,B})
=
D_\lambda(P_B\|Q_B)
+
D_\lambda
\left(
P_{A|B}\|Q_{A|B}
\mid P_B^{(\lambda)}
\right),
\]

where the conditioning distribution is not `P_B` itself but the Rényi tilted marginal

\[
P_B^{(\lambda)}(b)
\propto
P_B(b)^\lambda Q_B(b)^{1-\lambda}.
\]

Apply this with

* `B` = the old data after selecting branch `A_0=1`;
* `A` = the new data;
* `P_{A,B}=\widetilde Q_1`;
* `Q_{A,B}=\widetilde P_1`.

The tilted marginal `P_B^{(lambda)}` is exactly the branch-selected tilted law `nu_{lambda,0}^{(1)}` from R026. Therefore the R026 decomposition is the known Rényi chain rule applied after the branch-selection operation.

The decomposition still contains a project-specific selection component: the selected old-data divergence can itself be expanded into the node-0 divergence plus the correction involving `alpha_0`, `beta_0`, and the tilted branch reach. That correction is already recorded in R005 and in the Parallel-Hypothesis boundary work.

Hence the mathematically correct interpretation is:

1. branch selection produces new selected laws and the `alpha_0`, `beta_0`, `rho_{lambda,0}` correction;
2. once those laws are formed, the future dependent data enter through the standard conditional Rényi chain rule.

The absence of iid structure destroys ordinary tensorisation, but it does not destroy an exact Rényi chain rule.

## 3. The chain rule iterates over arbitrary transition kernels

Repeated application of the two-variable chain rule gives a full sequential decomposition for dependent path laws. At each stage the conditional Rényi term is evaluated under the Rényi tilted law of the previous prefix, not under the ordinary prefix law.

Lei Yu states this explicitly as a “Full Chain Rule for Rényi Divergences” (Theorem 8 of *The Entropy Method*): for transition measures defining general dependent laws,

\[
D_\lambda(P_{X^T}\|Q_{X^T})
=
\sum_{t=1}^{T}
D_\lambda
\left(
P_{X_t|X^{t-1}}
\|Q_{X_t|X^{t-1}}
\mid P_{X^{t-1}}^{(\lambda)}
\right),
\]

under the stated finiteness assumptions. This theorem is in a preprint monograph, so the two-variable Polyanskiy–Wu chain rule is the preferable primary citation for the core identity; the multistage formula can also be obtained by iteration.

Reference:

* Lei Yu, *The Entropy Method*, 2023 preprint, Theorem 8, “Full Chain Rule for Rényi Divergences.”

## 4. Immediate generic bounds on the dependent term

Define, for each old-data value `x`,

\[
d_{\lambda,1}(x)
:=
D_\lambda
\bigl(Q_1(\cdot\mid x,1)\|P_1(\cdot\mid x,1)\bigr).
\]

Since `T_{lambda,1}` is the logarithmic exponential mean of `d_{lambda,1}` under `nu_{lambda,0}^{(1)}`, one immediately has

\[
\operatorname*{ess\,inf}_{\nu_{\lambda,0}^{(1)}}d_{\lambda,1}
\leq
T_{\lambda,1}
\leq
\operatorname*{ess\,sup}_{\nu_{\lambda,0}^{(1)}}d_{\lambda,1}.
\]

Jensen additionally gives

\[
T_{\lambda,1}
\geq
\mathbb E_{\nu_{\lambda,0}^{(1)}}[d_{\lambda,1}]
\quad\text{for }\lambda>1,
\]

and

\[
T_{\lambda,1}
\leq
\mathbb E_{\nu_{\lambda,0}^{(1)}}[d_{\lambda,1}]
\quad\text{for }0<\lambda<1.
\]

These are elementary consequences of the established conditional Rényi representation, not new results.

A related mature literature appears in Rényi differential privacy. Adaptive composition commonly replaces the exact tilted average by a uniform conditional Rényi bound, leading to additive control over sequentially adaptive mechanisms. Mironov 2017 is a standard reference. This is potentially useful as a coarse bounding technique, especially for orders above one, but it loses the branch-selected tilted structure that matters for the present testing problem.

Reference:

* I. Mironov, “Rényi Differential Privacy,” *IEEE Computer Security Foundations Symposium*, 2017, pp. 263–275, arXiv:1702.07476.

## 5. Very close testing literature: adaptive simple channel discrimination

Hayashi 2009 studies discrimination of two classical channels when the input at each use can depend on previous outputs. Randomised `[0,1]`-valued tests are explicitly allowed and the two errors are written through expectations. For the adaptive experiment, Hayashi derives an additive accumulation identity for a Rényi/Hellinger-transform-type quantity along the adaptively generated observations and uses it to obtain asymptotic Stein, Chernoff, Hoeffding and Han–Kobayashi results.

This is an important neighbour because it shows that Rényi/Hellinger information under adaptive observation laws has been used directly in hypothesis-testing converses.

It does not solve the present problem because:

* the hypotheses are simple channels;
* the unknown channel is fixed across uses;
* the adaptive input is a sensing action, separate from the final hypothesis decision;
* there is one final decision rather than a sequence of reported local hypothesis decisions;
* the main results are asymptotic exponents, not the finite-sample propagation of local Type I and Type II bounds.

Reference:

* M. Hayashi, “Discrimination of Two Channels by Adaptive Methods and Its Application to Quantum System,” *IEEE Transactions on Information Theory* 55(8):3807–3820, 2009, doi:10.1109/TIT.2009.2023726, arXiv:0804.0686.

## 6. Composite adaptive testing exists, but it stops short of our dependence structure

Bergh, Datta and Salzmann study binary composite classical and quantum channel discrimination, including adaptive strategies. Their model does not require the supplied states or channels to be identical, but it still requires independence. They explicitly state that their theorems do not address sets of non-independent states.

For classical composite channel hypotheses they show that adaptive strategies can outperform parallel ones for non-convex sets. They also leave an important classical problem open: for non-convex composite hypotheses they do not have an entropic expression for the optimal adaptive error exponent in general.

This is a useful boundary for the current project. Even a neighbouring asymptotic composite adaptive problem with independence retained is not completely reduced to a simple entropic formula.

Reference:

* B. Bergh, N. Datta and R. Salzmann, “Composite Classical and Quantum Channel Discrimination,” arXiv:2303.02016v2, 2025 revision.

## 7. General dependence in simple testing is also classical

Han 2000 develops asymptotically optimal simple hypothesis testing for completely general sources, including nonstationary and nonergodic sources on abstract alphabets, using the information-spectrum method. Therefore arbitrary dependence by itself is not a novelty boundary.

Reference:

* T. S. Han, “Hypothesis Testing with the General Source,” *IEEE Transactions on Information Theory* 46(7):2415–2427, 2000, doi:10.1109/18.887854, arXiv:math/0004121.

## 8. Filtered statistical experiments and Hellinger processes

Jacod 1989 develops Hellinger processes for filtered statistical experiments. Dzhaparidze, Spreij and Valkeila later explicitly study randomized filtered experiments with abstract parameter spaces, generalized Hellinger processes and Hellinger integrals.

This literature is structurally relevant because our process is filtered, randomised, and history dependent. It supplies a mature language for information accumulation without independence. It does not, in the sources checked here, provide the finite-sample composite nodewise Type I/Type II error propagation theorem sought in UQ001.

References:

* J. Jacod, “Filtered statistical models and Hellinger processes,” *Stochastic Processes and their Applications* 32(1):3–45, 1989, doi:10.1016/0304-4149(89)90052-5.
* K. Dzhaparidze, P. Spreij and E. Valkeila, “Information concepts in filtered experiments,” *Theory of Probability and Mathematical Statistics* 67:38–56, 2002.

A related sequential-experiment result is Greenshtein and Torgersen 1997, who connect the Hellinger transform of a stopped iid experiment to expected sample size. It is useful historical background but retains iid sampling before stopping.

## 9. What has therefore been solved

The following part of R026 is solved by existing information theory:

* exact decomposition of Rényi divergence for dependent joint laws;
* the logarithmic tilted expectation of pointwise conditional Rényi divergences;
* iteration across arbitrary transition kernels through tilted prefix laws;
* coarse accumulation bounds from uniform conditional Rényi bounds.

Accordingly, it would be wrong to present `T_{lambda,1}` itself, or the existence of a non-iid Rényi chain rule, as a new mathematical contribution.

## 10. What has not been located as a solved theorem

No source in this audit was found to solve the complete statistical problem of this repository:

1. every node is a binary hypothesis test with its own Type I and Type II tradeoff;
2. the test is randomised;
3. the reported local hypothesis decision is itself the branch action selecting the next experiment;
4. future observations may depend on the realised past without conditional iid assumptions;
5. future hypotheses are composite and may be history dependent;
6. uncertainty must remain coherent across the path rather than being independently re-selected at each history;
7. the objective is a finite-sample achievability/converse theory for propagation of nodewise errors into a global path error.

This is `NO DIRECT MATCH LOCATED`, not a novelty claim.

## 11. Revised bottleneck

The bottleneck should therefore be reformulated.

It is not:

> How do we define or evaluate Rényi divergence when the future data are dependent?

The chain rule answers that exactly.

The actual bottleneck is:

> Starting from the exact conditional Rényi chain rule under the branch-selected tilted prefix law, how do the local finite-sample testing errors and their converse bounds propagate when each randomised hypothesis decision also selects the next dependent composite experiment?

For the singleton converse, the next step is to insert the established conditional Rényi representation into the finite-sample Rényi testing converse and determine what can be stated recursively in terms of the previous node’s error quantities and the conditional information term.

For the composite problem, the further difficulty is to take the pairwise converse over coherent history-dependent composite classes without illegitimately rectangularising a coupled environment.

This revised bottleneck is the research target that should replace the earlier interpretation of O016.
