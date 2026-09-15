# Research plan: Rényi approximation for controlled sequential testing

Date: 16 September 2026. Status: research programme with elementary derivations and small reference checks; no general efficient approximation theorem is claimed.

## 1. Starting point and scope

This plan belongs to `sequential_testing`, not to a separate generic divergence project. Before preparing it, all three files at commit `a7765a057b1879dc12a3fc66359e5f2b9a52ebd8` were read: `README.md`, `sequential_testing.tex`, and `RELATION_TO_PARALLEL_HYPOTHESIS.md`. The two scientific files are retained unchanged. They remain the authority for the model and notation.

The setting is new observations on a decision tree. At stage $t$, the data $X_t$ are observed, the test selects $A_t$, and that action can change the conditional law of future data. The main object is therefore the manuscript's joint law of observations and actions,

$$
\mathbb P_{\mathbf R}^{\boldsymbol\phi}(dx_{1:T},da_{1:T})
=\prod_{t=1}^T R_t(dx_t\mid h_{t-1})\,
\kappa_{\phi_t}(da_t\mid h_{t-1},x_t).
$$

A product of conditional kernels is not generally a product measure. Conversely, independence without identical distribution is enough for Rényi additivity [R2, Theorem 28]. The nonidentical product case is an exact control, not the difficult approximation target.

The motivating article [R1] gives a relative approximation of TV for explicit product laws in $O(nq\varepsilon^{-2}\log(1/\delta))$ work. Its useful mechanism is a sum of predictable posterior increments. Its second moment proof, particularly equation (5), uses independence to control the remaining experiment. We will adapt the mechanism and investigate a replacement for that control. We will not transfer the running time claim without its hypotheses.

The initial research question is:

> For a fixed common policy and two specified admissible conditional systems, can the induced path Rényi divergence be approximated with a rigorous finite horizon error guarantee and a useful bound on total work, despite action dependent future observations?

Composite optimisation and policy design follow only after the fixed pair evaluation problem is understood. Two comparison systems need not correspond to a single global label that is correct at every node. The repository's truth map $\vartheta$ is a separate object and is not replaced by a latent binary label used to simulate a mixture.

## 2. Notation and accuracy target

Keep $T,V_t,\Gamma,X_t,A_t,H_t,\mathcal F_t,\mathcal C_{t,i},\vartheta,\Theta_t,\eta,\mathfrak E,\phi_t,\boldsymbol\phi,\kappa_{\phi_t},\alpha_t,\beta_t$ and $G_t$ exactly as defined in the manuscript. Use $\lambda$ for Rényi order, never $\alpha$, which is already used for Type I errors. Keep the direction

$$
H_\lambda(Q,P)=\int q^\lambda p^{1-\lambda}\,d\mu,
\qquad D_\lambda(Q\Vert P)=\frac{\log H_\lambda(Q,P)}{\lambda-1}.
$$

Start with a fixed $0<\lambda<1$, first $\lambda=1/2$. For the fixed pair and policy, abbreviate

$$
\mathsf H_\lambda^{\boldsymbol\phi}
:=H_\lambda(\mathbb P_{\mathbf Q}^{\boldsymbol\phi},
             \mathbb P_{\mathbf P}^{\boldsymbol\phi}),
\qquad
\Delta_\lambda^{\boldsymbol\phi}:=1-\mathsf H_\lambda^{\boldsymbol\phi}.
$$

The scalar $\mathsf H_\lambda^{\boldsymbol\phi}$ is only an abbreviation for the displayed path integral, not a history or a history space. The notation register lists every addition.

The desired final guarantee, for a finite positive divergence, is

$$
\Pr\{|\widehat D-D|\leq\varepsilon D\}\geq1-\delta.
$$

An intermediate relative approximation of $\Delta$, a relative approximation of $H$, and an additive approximation of $D$ are different guarantees. Each must be named. At zero divergence, relative accuracy requires exact zero on the success event. At infinite divergence, a finite relative error criterion is not appropriate. Neither equality nor absence of a support violation can generally be inferred from sampled paths.

## 3. Access model and support discipline

The first implementation concerns finite observation alphabets. At a visited history, the algorithm can evaluate both conditional probability vectors, evaluate the common policy, and simulate the chosen conditional model. Count the full cost of doing so. If $X_t$ is a large block, its alphabet or conditional integration cost cannot be hidden in a constant.

Let $C_{\rm path}$ be the cost of one trajectory, including filtering, evaluating both models, evaluating the policy, sampling and numerical arithmetic. Conditional probabilities may be expensive even when unconditional simulation or joint likelihood evaluation is easy. An efficient conditional oracle is an assumption to justify for every model class.

Use unnormalised prefix masses to handle unreachable histories. For discrete histories, an intrinsic conditional comparison requires positive reach under the relevant law; two law conditional identities require positive reach under both. If one posterior model probability is zero and $0<\lambda<1$, the predictable weight is zero and the unavailable conditional law must not be queried. A deterministic action with probability zero is skipped, not replaced by a small positive probability.

For general observation spaces, state kernel, domination and measurability assumptions and interpret identities almost surely, rather than requiring a continuous history singleton to have positive probability. The initial finite calculations do not settle every measure theoretic extension.

The code supports exact zeros in the finite path enumeration and backward calculation for $0<\lambda<1$. Its sampling routine is deliberately narrower: conditional supports must match. Extending that sampler is a separate task. No implementation is promised to be numerically reliable for extreme orders, extremely small gaps or long paths in ordinary floating point.

## 4. Establish the controlled identities first

The companion note `notes/2026-09-16_controlled_renyi_identities.md` contains derivations. These are elementary working results, not claims of novelty or independent mathematical review.

### 4.1 Common policy cancellation does not remove control

On a path with positive probability under both models,

$$
\frac{d\mathbb P_{\mathbf Q}^{\boldsymbol\phi}}
     {d\mathbb P_{\mathbf P}^{\boldsymbol\phi}}
=
\prod_{t=1}^T\frac{q_t(X_t\mid H_{t-1})}{p_t(X_t\mid H_{t-1})}.
$$

The action kernels cancel because the same policy is used under both laws. However, $H_{t-1}$ includes earlier actions, so the conditional observation kernels and the distribution of visited histories still depend on the policy. Comparing two different policies does not permit this cancellation. Evaluating several candidate policies means a separate common policy comparison for each one.

### 4.2 Retain the manuscript's exact backward quantity

For finite alphabets, the existing recursion is

$$
G_t(h)=\sum_x q_t(x\mid h)^\lambda p_t(x\mid h)^{1-\lambda}
\sum_a\kappa_{\phi_t}(a\mid h,x)G_{t+1}(h,x,a),
\qquad G_{T+1}=1.
$$

It gives $G_1(\varnothing)=\mathsf H_\lambda^{\boldsymbol\phi}$. This is already in the manuscript and is not a new result of the recovery task. A recursion over all histories may still be exponential in $T$.

### 4.3 Separate new observation information from branch selection

Define the local integral

$$
z_{\lambda,t}(h)=H_\lambda(Q_t(\cdot\mid h),P_t(\cdot\mid h)).
$$

The full prefix integral after stage $t$ equals the preceding prefix integral multiplied by the expectation of $z_{\lambda,t}$ under the tilted preceding prefix law. The logarithmic increment is therefore a logarithm of a tilted average, not an ordinary average of local divergences.

At a fixed history of positive reach, conditioning the current observation on the selected action gives a different identity. With local branch probabilities $\rho_{P,t},\rho_{Q,t},\rho_{\lambda,t}$ under $P_t,Q_t$ and the local tilted kernel,

$$
D_\lambda(Q_t^{h,a}\Vert P_t^{h,a})
=D_\lambda(Q_t(\cdot\mid h)\Vert P_t(\cdot\mid h))
+\frac{\log\rho_{\lambda,t}-\lambda\log\rho_{Q,t}
 -(1-\lambda)\log\rho_{P,t}}{\lambda-1}.
$$

This concerns the law of the current observation conditional on selecting $a$. It is not the divergence of future data or the complete action path. The note states the positive probability conditions and distinguishes the local tilted kernel from the globally tilted continuation law.

In the same data boundary case, later observations merely reproduce stored data. There is no new divergence in the full transcript under a common policy, although conditioning on a selected branch can change the selected law's divergence. This is the required connection to `Parallel-Hypothesis`, not permission to import its formulas as if new data were absent.

## 5. Adapted predictable estimator

Draw a fair simulation label $J\in\{\mathbf P,\mathbf Q\}$ once, and simulate the entire controlled path under that model and the common policy. Write

$$
M^{\boldsymbol\phi}=\tfrac12(\mathbb P_{\mathbf P}^{\boldsymbol\phi}
                             +\mathbb P_{\mathbf Q}^{\boldsymbol\phi}),
\quad
\omega_t=\Pr(J=\mathbf Q\mid\mathcal F_t),
\quad \omega_0=1/2.
$$

The observed filtration includes observations and actions, but excludes the simulation label and unrevealed random seeds. The label $J$ is not $\Theta_t$ and has no role in declaring a correct edge.

Let $w_\lambda(u)=2u^\lambda(1-u)^{1-\lambda}$. Before observing $X_t$, compute

$$
C_{\lambda,t}=w_\lambda(\omega_{t-1})[1-z_{\lambda,t}(H_{t-1})],
\qquad
\mathcal A_\lambda^{\boldsymbol\phi}=\sum_{t=1}^T C_{\lambda,t}.
$$

Update the posterior after the observation using both kernels. The common action adds no posterior likelihood factor, but determines the next history. Conditional expectation and telescoping give

$$
\mathbb E_{M^{\boldsymbol\phi}}\mathcal A_\lambda^{\boldsymbol\phi}
=\Delta_\lambda^{\boldsymbol\phi}.
$$

For orders below one the increments are nonnegative. This is an unbiased estimator of the gap only. Taking a logarithm of a sample mean is not unbiased estimation of divergence.

The exact remaining gain is tied directly to the existing $G_t$:

$$
\mathbb E\!\left[\sum_{j=t}^T C_{\lambda,j}\mid\mathcal F_{t-1}\right]
=w_\lambda(\omega_{t-1})[1-G_t(H_{t-1})].
$$

If the right side is at most $K\Delta_\lambda^{\boldsymbol\phi}$ at every reachable history, then

$$
\mathbb E[(\mathcal A_\lambda^{\boldsymbol\phi})^2]
\leq2K(\Delta_\lambda^{\boldsymbol\phi})^2.
$$

Independent repetitions and a median of means then give relative gap error $\epsilon_{\rm gap}$ in

$$
O\!\left(C_{\rm path}K\epsilon_{\rm gap}^{-2}\log(1/\delta)\right)
$$

work. The note proves this conditional statement. Deriving a useful $K$ from accessible model parameters is unresolved. Computing the exact maximum using all $G_t$ would already require solving the original continuation problem and is not an efficient justification.

## 6. A decision dependent obstruction to the direct extension

Use two stages. The first observation is an identical fair binary observation under both laws. Let the common first action satisfy $\Pr(A_1=1\mid X_1)=\tau$. If $A_1=0$, the second observation is again identically distributed. If $A_1=1$, its laws are $P_2=(3/4,1/4)$ and $Q_2=(1/4,3/4)$. The last action can use any common policy.

With $d_\lambda=1-H_\lambda(Q_2,P_2)>0$,

$$
\mathcal A_\lambda^{\boldsymbol\phi}
=d_\lambda\mathbf1_{\{A_1=1\}},
\quad
\Delta_\lambda^{\boldsymbol\phi}=\tau d_\lambda,
\quad
\frac{\operatorname{Var}(\mathcal A_\lambda^{\boldsymbol\phi})}
     {(\mathbb E\mathcal A_\lambda^{\boldsymbol\phi})^2}
=\frac1\tau-1.
$$

The likelihood ratio remains between $1/3$ and $3$. A short horizon, bounded likelihood ratio and positive observation probabilities do not provide a uniform bound for this estimator. The example is genuinely about the action selecting the future experiment, as required by this repository.

This is not a lower bound for every algorithm. Summing the two first action branches explicitly gives $\tau d_\lambda$ without sampling variance. The next method should exploit that structure rather than discard the counterexample.

## 7. Computational routes in the revised order

### Route A: exact controlled references and genuinely sufficient state

First compare direct path enumeration with the existing $G_t$ recursion. When a state $S_t=s_t(H_{t-1})$ determines both observation kernels, the policy and a deterministic update $S_{t+1}=\Psi_t(S_t,X_t,A_t)$, the recursion can be evaluated on that state. With at most $m$ states at each stage and observation alphabet size $q$, the arithmetic work is $O(Tmq)$ for two actions, plus oracle costs.

A small observed Markov model is a special case. A generic state transition with up to $m$ successors introduces an additional summation. A node $V_t$ alone is not sufficient when the observation history still affects the kernels. Approximate state compression requires its own error analysis. Hidden states are not observed sufficient states, and augmenting the target with them changes the divergence.

Do not describe an algorithm as linear in the horizon merely because it visits a tree once. An explicitly supplied tree can already have exponentially many nodes in $T$.

### Route B: integrate actions or short blocks before simulation

The first research method beyond the reference calculation should sum over selected action branches, or a short block of observation and action transitions, and simulate only the unresolved continuation. Study whether this removes the rare action obstruction with a controlled increase in work.

Conditioning and averaging are with respect to $M^{\boldsymbol\phi}$. At an internal observed history the model mixture weights are the current posterior, not a fresh fair prior. For conditionally independent branch rollouts, draw each rollout's model label from that posterior. It remains fixed within the rollout. Averaging labels or latent states must never change the target to an augmented law.

When exact stratum probabilities $r_b$ and exact conditional simulation are available, independent estimates with $N_b$ draws have variance $\sum_b r_b^2\operatorname{Var}(Y_b)/N_b$. Derive this for the chosen strata and count the cost of their probabilities, simulation and allocation. Integrating every binary action at every stage can cost $2^T$; integrating $b$ selected stages can still cost $2^b$. A favourable variance calculation without this cost is insufficient.

Initial target: two and three stage controlled examples with an informative rare branch, followed by models with a fixed small number of such branching stages. Establish a result for that explicit class or find the additional obstruction.

### Route C: approximate continuation for controlled latent models

Next use finite product mixtures or small hidden Markov observation models whose filtering calculations can be performed at each visited history and whose future observation mechanism depends on the selected action. This retains the original research setting while providing tractable conditional oracles.

Compare the predictable estimator, action integration and locally tilted path sampling. Normalising $q_t^\lambda p_t^{1-\lambda}$ at each history defines a local tilted observation kernel, with the same action policy. Along this locally tilted process,

$$
\mathsf H_\lambda^{\boldsymbol\phi}
=\mathbb E\prod_{t=1}^T z_{\lambda,t}(H_{t-1}).
$$

Its weights are random and can have large variance. The ideal global tilted transition also contains $G_{t+1}/G_t$ and can change action probabilities. Do not confuse the two tilted laws. Exact evaluation of that ideal transition already requires the hard continuation.

Investigate block methods, controlled discretisation of a filtering state, or particle approximations with explicit error bounds. A particle count increasing with $T$ can make total work quadratic even when one particle update has constant cost. Audit [R5] before applying a particle normalising constant result. Existing hidden Markov divergence rate results [R6] are not a finite horizon approximation theorem for this controlled path problem.

## 8. Composite uncertainty and path risk remain separate tasks

A fixed pair estimate is not an estimate of a composite infimum. Specify a feasible set of complete pairs of conditional systems, including truth maps and any parameter coupling. For $0<\lambda<1$, minimising divergence corresponds to maximising the Hellinger integral because $\lambda-1<0$. This reversal must remain explicit.

Under genuinely rectangular kernel uncertainty, compatible local choices may be pasted together for a fixed truth map. Under a common parameter or latent environment, nature cannot change that parameter after seeing each history. A two model regression example demonstrates that local optimisation over a rectangular enlargement gives zero separation while both original coherent models have positive separation.

There is an extra issue specific to the manuscript: $\vartheta(v)$ is fixed across all histories reaching the same node. Rectangularity of the conditional kernels alone does not allow a separate worst case truth label at each such history. Either fix the truth map during the recursion and optimise over coherent maps outside it, or prove a valid state augmentation or game formulation. Allowing nature to choose the truth separately at each history is a different uncertainty class. A reference example gives worst case error $1/2$ with a fixed node truth and error $1$ with an impermissibly history dependent truth.

The target $\mathcal R_T(\boldsymbol\phi)$ is the probability of at least one wrong edge. It is neither a pairwise path divergence nor the error of a single terminal test. Evaluate its exact recursion separately on tiny fixed environments. Develop local composite error inequalities, propagation and policy optimisation only with an explicit connection to that risk. Do not multiply marginal correctness probabilities.

For a finite predetermined collection of $N$ evaluations, allocate failure probabilities jointly, for example $\delta/N$ per evaluation. Infinite model classes, policy search, or choices made after inspecting estimates require a uniform analysis or a valid sequential allocation, not repeated use of one fixed pair confidence statement.

## 9. Error conversion, higher orders and numerical work

For $0<\lambda<1$,

$$
D=\frac{-\log(1-\Delta)}{1-\lambda}.
$$

If $|\widehat\Delta-\Delta|\leq\epsilon_{\rm gap}\Delta$ and $\epsilon_{\rm gap}\Delta<H=1-\Delta$, then

$$
\frac{|\widehat D-D|}{D}
\leq\frac{\epsilon_{\rm gap}\Delta}{(H-\epsilon_{\rm gap}\Delta)(-\log H)}.
$$

Under a proved promise $\Delta\leq\gamma<1$, choosing $\epsilon_{\rm gap}=\varepsilon(1-\gamma)/2$ suffices for $0<\varepsilon\leq1$. Without overlap control, a relative gap guarantee does not uniformly transfer to a relative divergence guarantee. Use a separate power integral estimate or state an interval with an infinite endpoint when that is all the evidence supports.

A relative $\epsilon_{\rm gap}<1$ approximation of $H$ gives additive divergence error at most $-\log(1-\epsilon_{\rm gap})/|\lambda-1|$. This can be inadequate near zero divergence. For orders above one, define the nonnegative gap $H-1$ instead: a relative gap error transfers to relative divergence error by concavity of $\log(1+x)$, but high likelihood ratio moments can make the gap itself difficult to estimate. Analyse those orders in a separate package, not by changing a sign and retaining the same variance theorem.

Use stable logarithmic computations, `log1p` and `expm1`, with increased precision references for cancellation. Distinguish statistical error, numerical error, approximation of conditional kernels and optimisation error. Preserve exact support, never smooth zero masses, and never clip a failed estimate into the valid range and call it a successful bound. The present code is a small reference tool, not that final stable implementation.

## 10. Stages and completion conditions

| Stage | Work | Required output |
| --- | --- | --- |
| 0 | Read and integrate the existing repository | Notation register, source record and preserved scientific files |
| 1 | Review controlled identities and support | Proof note and exact finite path regression checks |
| 2 | Integrate selected action branches | Unbiased algorithm, conditional posterior handling and full work count |
| 3 | Analyse the chosen controlled model class | Explicit useful variance bound or a precise failure example |
| 4 | Extend beyond exact state recursion | Controlled mixture or hidden observation implementation and oracle validation |
| 5 | Establish the requested accuracy and cost | Gap conversion, numerical error analysis and reproducible comparisons |
| 6 | Connect to composite testing and path risk | Coherent uncertainty class, optimisation order and a proved risk connection |

Stages 0 and initial parts of Stage 1 are implemented in this recovery. Independent proof review, novelty assessment and Stages 2 onward remain unfinished research tasks. No broad simulation study or remote CI run is reported as completed.

The initial suite has 30 passing test methods, several with parameter subcases. It includes path normalisation, nonidentical products, policy cancellation with continuing policy dependence, exact backward and compressed state recursions, predictable means and conditional remaining gain, branch selection, same data reuse, support, action projection, the rare action failure, and the two uncertainty consistency examples.

The next executable brief is `prompts/01_controlled_renyi_foundations.md`. Record each result with its model, order, horizon, policy, environment restrictions, method, reference value, seed where relevant, sample count, runtime, error criterion and commit. Publish completed milestones with updated status and a machine readable checkpoint rather than leave the only copy in a temporary workspace.

## References and reading status

[R1] Konrad Anand, Alistair Benford and Heng Guo. *Linear time approximation of the TV distance between product distributions*. arXiv:2607.27088v1, 2026. Versioned HTML and author PDF read, including the second moment proof. See `sources/2607.27088/SOURCE.md`.

[R2] Tim van Erven and Peter Harremoës. *Rényi Divergence and Kullback–Leibler Divergence*. IEEE Transactions on Information Theory, 2014. Definition, support conventions, data processing and Theorem 28 checked. https://arxiv.org/html/1206.2459v2

[R3] Paul Glasserman. *Filtered Monte Carlo*. Mathematics of Operations Research 18, 610–634, 1993. Author institution record and abstract checked; full comparison of hypotheses remains pending. https://business.columbia.edu/faculty/research/filtered-monte-carlo

[R4] Eric Price, Kevin Tian, Zhiyang Xun and Yusong Zhu. *Total Variation Distance Estimation in Autoregressive Models*. arXiv:2607.19510, 2026. Abstract checked. This is relevant to access models for dependent sequence distributions; its stated accuracy target is additive TV, not our relative Rényi target. https://arxiv.org/abs/2607.19510

[R5] F. Cérou, P. Del Moral and A. Guyader. *A nonasymptotic theorem for unnormalized Feynman–Kac particle models*. Annales de l'Institut Henri Poincaré, Probabilités et Statistiques 47, 629–649, 2011. Journal record checked; applicable theorem assumptions still require review. https://www.numdam.org/articles/10.1214/10-AIHP358/

[R6] Cheng-Der Fuh, Su-Chi Fuh, Yuan-Chen Liu and Chuan-Ju Wang. *Rényi Divergence in General Hidden Markov Models*. arXiv:2106.01645, 2021. Abstract checked; full audit and final publication details remain pending. https://arxiv.org/abs/2106.01645

The novelty audit must also cover predictable Hellinger processes and controlled statistical experiments. This bibliography is a starting point, not an assertion of a complete literature search. Exact bibliographic titles are retained even where their terminology differs from the prose conventions used in this repository.
