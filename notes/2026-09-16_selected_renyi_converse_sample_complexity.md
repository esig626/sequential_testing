# Selected Rényi converses and necessary sample sizes

Date: 16 September 2026.

Branch: `research/selected-renyi-converse-sample-complexity`.
Base: `f7e6dab50b296b1a0f9faf21b6cb1a18911e2c92`.
Status: DERIVED, NOT INDEPENDENTLY REVIEWED. The accompanying finite checks are consistency checks, not a proof or a novelty audit.

## 1. Task, existing inputs, and scope

This task extends O016 and contributes to UQ001. It imports SB001/R025 and R026 to R029, rather than deriving the original testing converse or conditional Rényi chain rule again. M013 permits coarse bounds using uniform conditional information limits. F003, F004 and F007 prohibit replacing a coherent environment by unrelated local choices or identifying a divergence with path risk.

The requested source is the uploaded *Finite Sample Bounds for Composite Hypothesis Testing*, Vera-Sigüenza and Esposito, arXiv:2608.28068v1. We use Theorem 1, equation (4), its proof in Appendix A-A, and the opposite direction converse in equation (48). The uploaded version remains the basis even though the online record lists a later version. In the supplied version, Appendix A-A uses change of measure and Hölder's inequality; we do not silently replace that proof by a different argument.

This note concerns converses only. A necessary sample size is not an achievable sample size. No claim of matching upper and lower sample complexity is made.

The principal calculation is for a fixed coherent singleton pair. Under the comparison environment P the root and the child reached through edge 1 both have truth label 0. Under Q both have truth label 1. This is the concrete path (1,1) case agreed in the discussion, not an assumption that all possible environments on the original tree have one global label. Section 8 states exactly how this comparison gives a composite lower bound.

## 2. Notation and the conditioning convention

The root is V_0. Its old observation block is X_0^n, with realised value x. The child reached through A_0=1 is V_1. Its new block is X_1^m, with realised value y. The superscripts n and m count observations; they do not assert a product law. Let N=n+m be the total number along this two node path.

Use Z_0=empty and Z_1=(X_0^n,A_0). More generally, Z_t is the observed past BEFORE node t under this zero based indexing. The symbol h remains reserved for the log likelihood ratio. Composite class notation remains C_t^(0) and C_t^(1). These conventions are the user's approved update to the older one based manuscript notation.

Let P_0 and Q_0 denote laws of the WHOLE old block. They are not automatically single observation laws. Their densities are p_0 and q_0. The same measurable randomised test phi_0(x) in [0,1] is used under both laws. Define its actual pair errors by

$$
\alpha_0=\mathbb E_{P_0}[\phi_0],\qquad
s_0:=1-\beta_0=\mathbb E_{Q_0}[\phi_0].
$$

Here s_0 is an abbreviation for the alternative's reach of branch 1. These are actual errors of the selected first rule, not beta_0^star and not worst case composite errors. Assume alpha_0>0 and s_0>0 whenever a selected law is used.

The conditional new block densities are p_1(y|x,1) and q_1(y|x,1). Their coordinates may be dependent and differently distributed even after x and A_0 are fixed. Both blocks may be dependent internally; no independence across blocks is imposed.

Let tilde P_1 and tilde Q_1 be the joint laws of (x,y) conditional ONLY on A_0=1:

$$
\widetilde p_1(x,y)=\frac{\phi_0(x)p_0(x)p_1(y\mid x,1)}{\alpha_0},
\qquad
\widetilde q_1(x,y)=\frac{\phi_0(x)q_0(x)q_1(y\mid x,1)}{s_0}.
$$

The old data remain random under these branch selected laws. This is not conditioning on a particular old observation x as well. A test phi_1(x,y) may retain the old data. Its branch conditional errors are

$$
\alpha_1=\mathbb E_{\widetilde P_1}[\phi_1],\qquad
\beta_1=\mathbb E_{\widetilde Q_1}[1-\phi_1].
$$

We impose alpha_0<=epsilon_0 and alpha_1<=epsilon_1 with separate budgets in (0,1). A uniform error guarantee at every realised old history implies this branch conditional guarantee by averaging, but the converse implication is not assumed.

Fix lambda>1 and write c_lambda=(lambda-1)/lambda. All logarithms are natural. Work with finite relevant Rényi moments and their usual absolute continuity conditions. Zero weight branches are omitted, not evaluated using an artificial positive mass. When the original root moment is infinite the root tilt decomposition may be unavailable even if a selected moment is finite; apply the source converse directly to the selected laws in that case. No infinity minus infinity manipulation is permitted. If finite forward Rényi moments hold and a branch has zero P reach, it also has zero Q reach, so the all ones path error under Q is already one; no conditional normalisation is needed.

## 3. Import the two source converses exactly

For a randomised test phi on any joint observation space, let alpha=E_P[phi] and beta=E_Q[1-phi]. Equation (4), applied to one observation whose value is the entire record, gives for each lambda>1

$$
\beta\geq\left[1-\varepsilon^{c_\lambda}
 \exp\{c_\lambda D_\lambda(Q\Vert P)\}\right]_+,
\qquad \alpha\leq\varepsilon. \tag{1}
$$

The notation [u]_+ means max(u,0). Optimising (1) over lambda gives the source Theorem 1. Treating a whole dependent block as one observation requires no tensorisation and does not make its coordinates iid.

Equation (48) of the supplied article gives the second, opposite direction bound

$$
\beta\geq(1-\varepsilon)^{1/c_\lambda}
 \exp\{-D_\lambda(P\Vert Q)\}. \tag{2}
$$

Both directions can be used; neither is new here. In particular, (2) can be useful for a small target Type II error when the positive part in (1) is zero.

## 4. Substitute R026: an explicit local converse

Define the root divergence I_{lambda,0}(n)=D_lambda(Q_0||P_0). Retain R026's tilted root law nu_{lambda,0}, tilted branch reach rho_{lambda,0}=E_nu[phi_0], and selected tilted law nu_{lambda,0}^(1).

Define the conditional divergence of the whole new block at old value x by

$$
d_{\lambda,1}(x;m)
 =D_\lambda\bigl(Q_1(\cdot\mid x,1)\Vert P_1(\cdot\mid x,1)\bigr).
$$

The already established conditional Rényi term is

$$
T_{\lambda,1}(n,m)
 =\frac{1}{\lambda-1}\log
 \mathbb E_{\nu_{\lambda,0}^{(1)}}
 \left[\exp\{(\lambda-1)d_{\lambda,1}(X_0^n;m)\}\right].
$$

Its dependence on the fixed first rule is implicit, not absent. R026 states

$$
D_\lambda(\widetilde Q_1\Vert\widetilde P_1)
=I_{\lambda,0}(n)+T_{\lambda,1}(n,m)
+\frac{\log\rho_{\lambda,0}-\lambda\log s_0-(1-\lambda)\log\alpha_0}{\lambda-1}. \tag{3}
$$

Substituting (3) into (1) gives

$$
\beta_1\geq
\left[
1-\frac{(\alpha_0\varepsilon_1)^{c_\lambda}}{s_0}
\rho_{\lambda,0}^{1/\lambda}
\exp\{c_\lambda(I_{\lambda,0}(n)+T_{\lambda,1}(n,m))\}
\right]_+. \tag{4}
$$

Thus the same lower bound holds for beta_1^star(epsilon_1;phi_0), where the first rule and therefore the selected experiment are fixed. It is not a bound obtained by independently optimising the first and second tests.

For (2), explicitly introduce opposite direction quantities: I^-_{lambda,0}=D_lambda(P_0||Q_0), the tilt proportional to p_0^lambda q_0^(1-lambda), its branch reach rho^-_{lambda,0}, and T^-_{lambda,1} formed from D_lambda(P_1||Q_1) under that selected opposite tilt. These are generally DIFFERENT from their unmarked counterparts. Then

$$
\beta_1\geq
\frac{[\alpha_0(1-\varepsilon_1)]^{1/c_\lambda}}{s_0}
(\rho^-_{\lambda,0})^{-1/(\lambda-1)}
\exp\{-I^-_{\lambda,0}(n)-T^-_{\lambda,1}(n,m)\}. \tag{5}
$$

A bound for T in one direction is not automatically a bound for T^-.

## 5. Convert to the two node error: survival cancels

Under Q the correct path is (1,1). Define B_Q as the expected indicator of any wrong decision along this two node procedure:

$$
B_Q:=\mathbb E_Q[(1-A_0)+A_0(1-A_1)]
=\beta_0+s_0\beta_1.
$$

A_1 in this expression is needed only on branch A_0=1. The root decision is irreversible, so B_Q>=beta_0.

Multiplying (4) by s_0 and adding beta_0 gives, for every admissible pair of randomised tests,

$$
B_Q\geq\max\left\{\beta_0,
1-(\alpha_0\varepsilon_1)^{c_\lambda}
\rho_{\lambda,0}^{1/\lambda}
\exp\{c_\lambda(I_{\lambda,0}(n)+T_{\lambda,1}(n,m))\}
\right\}. \tag{6}
$$

This is the useful cancellation: the selected divergence contains a factor 1/s_0, but multiplying by the actual reach s_0 removes it. No independence was used. The first test still matters through alpha_0, rho and the selected conditional information T.

The opposite direction gives the companion bound

$$
B_Q\geq\beta_0+
[\alpha_0(1-\varepsilon_1)]^{1/c_\lambda}
(\rho^-_{\lambda,0})^{-1/(\lambda-1)}
\exp\{-I^-_{\lambda,0}(n)-T^-_{\lambda,1}(n,m)\}. \tag{7}
$$

Replacing alpha_0 by its UPPER budget epsilon_0 is safe as a weakening of (6), but is NOT safe in (7): its contribution has the opposite monotonicity. Also, beta_0, rho, and T come from the SAME first test. Substituting separately chosen optimisers for them is invalid.

## 6. Necessary sample sizes without independence

For a converse based on (1), an UPPER bound on information is useful: it limits how well any test can perform. A lower information bound does not serve this purpose.

Assume that, for the pair under study,

$$
I_{\lambda,0}(n)\leq a_\lambda(n),\qquad
T_{\lambda,1}(n,m)\leq b_\lambda(n,m). \tag{8}
$$

The letters a_lambda and b_lambda denote deterministic information bounds, not actions or testing errors. For a bound uniform over first tests, the second inequality must hold uniformly over those tests. One sufficient condition is

$$
d_{\lambda,1}(x;m)\leq b_\lambda(n,m)
$$

for every relevant old history x. An upper bound on the ordinary mean of d does not suffice, since lambda>1 makes its logarithmic exponential mean at least its mean.

Using rho<=1 and the two error budgets in (6) yields

$$
B_Q\geq
1-\exp\left\{-\sup_{\lambda>1}
 c_\lambda\left[\log\frac{1}{\varepsilon_0\varepsilon_1}
 -a_\lambda(n)-b_\lambda(n,m)\right]_+\right\}. \tag{9}
$$

Optimisation uses only orders for which the stated finite information bounds hold. This is a converse for an actual sequential event, not merely a relabelling of path divergence.

Let delta_path in (0,1) be a desired upper limit on B_Q; this is a statistical error target, not a simulation confidence level. A necessary condition is, for EVERY permitted lambda,

$$
a_\lambda(n)+b_\lambda(n,m)
\geq \log\frac{1}{\varepsilon_0\varepsilon_1}
 +\frac{1}{c_\lambda}\log(1-\delta_{\rm path}). \tag{10}
$$

Consequently a necessary lower bound on the new block size is

$$
m\geq\inf\left\{k\in\mathbb N,\ k\geq1:
\text{(10) holds with }m=k\text{ for every permitted }\lambda\right\}, \tag{11}
$$

with an empty set interpreted as infinity. If the information bounds are nondecreasing, this is an ordinary inverse information growth condition. Without monotonicity it remains an exclusion of impossible sample sizes, not an assertion that all larger sizes work.

A transparent specialisation assumes

$$
a_\lambda(n)=n u_{\lambda,0},\qquad
b_\lambda(n,m)=m u_{\lambda,1},
$$

where u_{lambda,0} and u_{lambda,1} are positive information limits per observation. Then

$$
m\geq\max\left\{1,
\left\lceil\sup_{\lambda>1}
\frac{\left[\log\frac1{\varepsilon_0\varepsilon_1}
 +c_\lambda^{-1}\log(1-\delta_{\rm path})-n u_{\lambda,0}\right]_+}
 {u_{\lambda,1}}\right\rceil\right\}. \tag{12}
$$

If a denominator is zero and the numerator positive, that order excludes all m; if both are zero it imposes no new restriction.

These linear upper limits do NOT require iid data. For example, it suffices to bound the conditional divergence of each next raw observation, given all preceding raw observations and actions, by u_{lambda,t}. Applying the established chain rule and the upper bound by the essential supremum gives the block bound. The conditional laws themselves may depend on the entire past and differ at every observation. This uses M013, not a product assumption.

The previously used iid root is only an OPTIONAL special case: if P_0=bar P_0^(tensor n) and Q_0=bar Q_0^(tensor n), then I_{lambda,0}(n)=n D_lambda(bar Q_0||bar P_0). Equation (9) also permits a fully dependent root.

For a prescribed first rule and a target beta_1<=delta_1, (4) and (5) give stronger local necessary conditions. Let S_{lambda,0} denote the logarithmic selection correction in (3), and let S^-_{lambda,0} denote its opposite direction version. Write D^+_{lambda,sel}=I+S+T and D^-_{lambda,sel}=I^-+S^-+T^- for the two selected divergences. Then necessarily

$$
D^+_{\lambda,\rm sel}\geq\log(1/\varepsilon_1)
+c_\lambda^{-1}\log(1-\delta_1), \tag{13}
$$

$$
D^-_{\lambda,\rm sel}\geq\log(1/\delta_1)
+c_\lambda^{-1}\log(1-\varepsilon_1). \tag{14}
$$

The second condition explicitly retains log(1/delta_1). Neither condition is sufficient. A fully specified model and fixed first test make S and S^- computable; otherwise they cannot be treated as known constants independent of sample size or the policy.

If the Type I budgets themselves shrink with sample count, substitute their actual functions into (9). For example epsilon_0=exp(-n r_0) and epsilon_1=exp(-m r_1) give the lower bound with exponent c_lambda[n(r_0-u_{lambda,0})+m(r_1-u_{lambda,1})]_+. Increasing sample size while tightening constraints is a different question from keeping the error budgets fixed.

## 7. Repetition over further nodes

Consider K decisions, numbered 0 through K-1. Under Q the correct path is all ones. A coherent comparison environment P has local null label 0 at every node of that path. At each stage, impose the Type I budget epsilon_t conditional on reaching that node through preceding ones. Let n_t be its block size and u_{lambda,t}(n_t) a uniform upper bound on the conditional block divergence Q_t||P_t given all previous data and actions on surviving histories.

Write B_{Q,K} for the expected indicator of any wrong edge under Q. Then

$$
B_{Q,K}\geq
1-\exp\left\{-\sup_{\lambda>1}c_\lambda
\left[\sum_{t=0}^{K-1}\log(1/\varepsilon_t)
-\sum_{t=0}^{K-1}u_{\lambda,t}(n_t)\right]_+\right\}. \tag{15}
$$

Proof: retain unnormalised densities of the observation histories on the all ones path. Before the final test, their order lambda moment contains each preceding common action factor phi_t to power ONE. Integrating the next observation bounds its contribution by exp((lambda-1)u_{lambda,t}); preceding factors phi_t<=1 cannot increase this moment. Induction bounds the moment by exp((lambda-1)sum u). The first measure's mass of the complete all ones event is at most product epsilon_t by conditional expectation. Apply the source change of measure/Hölder step to the final test on the surviving subprobability measures. Its second measure's success mass is at most (product epsilon_t)^c_lambda exp(c_lambda sum u). Subtract from one and optimise the order. This proof never assigns data to unobserved off support histories; factors of zero kill those histories.

Equation (15) is not multiplication of marginal correctness probabilities. It combines conditional Type I budgets with a controlled information bound. It requires the stated coherent null comparison along the target path. Arbitrary changing truth maps and other path losses have not been reduced to this special case.

## 8. What transfers to composite testing

For fixed phi_0, form the branch selected joint null class C_1^(0) and alternative class C_1^(1) by conditioning WHOLE admissible environments, not by pasting arbitrary marginals and conditional kernels. Equations (1) and (2) apply to every coherent pair and can be optimised over those pairs. This needs no attained minimiser and no least favourable distributions. For each order the complete selected divergence, including its selection and conditional terms, must be optimised as one quantity. Infima of its separate terms cannot be added and assumed attainable by one pair.

For global risk, if the original composite model contains a coherent pair of the kind in Sections 5 or 7, and the information caps are uniform over admissible policies, every policy satisfying the composite conditional Type I constraints satisfies the corresponding bound on B_Q for that same pair. Its worst environment risk is at least B_Q. Taking an infimum over policies therefore preserves (9) or (15), and one may choose the coherent pair yielding the largest such lower bound. This is a valid composite converse, not an exact minimax characterisation or a rectangular Bellman result.

## 9. A fully dependent Gaussian model with explicit n and m

This is a NEW illustrative model choice, not an assertion from the user's paper. It allows dependence in both blocks and after conditioning on the old block.

For k>=1 and a correlation parameter gamma in (0,1), define the k by k matrix R_k(gamma) with entry gamma^|i-j|. Let 1_k be the vector of k ones. Choose positive sigma_0,sigma_1 and nonzero mean gaps Delta_0,Delta_1. Let gamma_0,gamma_1 be in (0,1).

At the root take

$$
P_0=\mathcal N(0,\sigma_0^2R_n(\gamma_0)),\qquad
Q_0=\mathcal N(\Delta_0\mathbf1_n,\sigma_0^2R_n(\gamma_0)).
$$

At the child on branch 1 take

$$
P_1(\cdot\mid x,1)=\mathcal N(g(x)\mathbf1_m,\sigma_1^2R_m(\gamma_1)),
$$

$$
Q_1(\cdot\mid x,1)=\mathcal N((g(x)+\Delta_1)\mathbf1_m,\sigma_1^2R_m(\gamma_1)),
$$

where g(x), for example the final coordinate x_n, is a fixed observed function shared by the two models. The other branch may specify different kernels. The nonconstant g produces cross block dependence. The positive off diagonal covariances preserve dependence inside the new block even after x is fixed. Nothing here is a conditionally iid block.

Define

$$
J_t(k)=\frac{\Delta_t^2}{2\sigma_t^2}
\frac{k(1-\gamma_t)+2\gamma_t}{1+\gamma_t},\qquad t=0,1.
$$

A direct Gaussian calculation gives

$$
I_{\lambda,0}(n)=\lambda J_0(n),\qquad
 d_{\lambda,1}(x;m)=T_{\lambda,1}(n,m)=\lambda J_1(m). \tag{16}
$$

The same expressions hold in the opposite direction. For k>=2, the inverse correlation matrix has boundary diagonal 1, interior diagonal 1+gamma^2, and neighbouring entries -gamma, all divided by 1-gamma^2. Summing its entries gives [k(1-gamma)+2gamma]/(1+gamma). For k=1 the matrix and its inverse are [1], and the same scalar sum formula equals 1. Equal covariance Gaussian Rényi divergence is lambda/2 times the squared mean displacement in the inverse covariance metric; substitution proves (16). The conditional divergence is constant in x because g(x) cancels between the two means, not because the data are independent.

Let J=J_0(n)+J_1(m) and L=log(1/(epsilon_0 epsilon_1)). Equation (9) can now be optimised in closed form:

$$
B_Q\geq1-\exp\left\{-\left[\sqrt L-\sqrt J\right]_+^2\right\}. \tag{17}
$$

Indeed, maximising (lambda-1)(L-lambda J)/lambda gives lambda=sqrt(L/J) when L>J>0; otherwise its positive maximum is zero. The zero information case follows by taking lambda to infinity.

For the target B_Q<=delta_path, define

$$
J_{\rm req}:=\left[\sqrt{\log(1/(\varepsilon_0\varepsilon_1))}
-\sqrt{-\log(1-\delta_{\rm path})}\right]_+^2.
$$

Then a necessary sample size condition is

$$
J_0(n)+J_1(m)\geq J_{\rm req}. \tag{18}
$$

Write c_1=Delta_1^2/(2 sigma_1^2), used only in this Gaussian formula and distinct from c_lambda. For fixed n, inversion is explicit:

$$
m\geq\max\left\{1,
\left\lceil\frac{(1+\gamma_1)[J_{\rm req}-J_0(n)]/c_1-2\gamma_1}
 {1-\gamma_1}\right\rceil\right\}. \tag{19}
$$

Example: Delta_0=Delta_1=sigma_0=sigma_1=1, gamma_0=gamma_1=0.6, epsilon_0=epsilon_1=0.05, and delta_path=0.1. Then J=(n+m)/8+3/4 and J_req=4.507782842774305. Thus n+m must be at least 31. With n=20 this excludes m<=10. At total 30 the lower bound is 0.1010737213; at total 31 it is 0.0845205324. The latter does NOT assert that 31 observations suffice. Root reliability can impose additional necessary conditions; passing (18) does not discharge them.

The general fixed budget root sample necessary condition is obtained by applying the same source converse to the root itself. In the Gaussian example it is J_0(n)>=[sqrt(log(1/epsilon_0))-sqrt(-log(1-delta_path))]_+^2, since any path error target also requires beta_0<=delta_path.

## 10. Limits and current outcome

There is no distribution free conversion from the raw count m alone to information under arbitrary dependence. For a concrete counterexample, let every new coordinate be the same freshly generated Bernoulli variable U. Repeating U m times supplies exactly the information of one draw, however large m becomes. If both models have the same conditional U law, T is zero. At the other extreme disjoint new supports can permit exact discrimination at m=1. These are model distinctions, not difficulties that more algebra or a larger n can remove.

What has been obtained is: the exact local substitution in both directions; the two node survival cancellation; a converse for successive all ones decisions under a coherent comparison; necessary sample counts under explicit conditional information limits; and a closed form count relationship for an explicitly dependent Gaussian model. The exact composite minimax tradeoff, matching achievability, arbitrary truth patterns and sharpness of the coarse information limits remain unproved here.

The next research decision should consult the ledger. One relevant extension is to retain the selection factor rather than replace rho by one and to compare the resulting necessary counts with exact selected experiment performance. Do not restart a search for a dependent Rényi chain rule or rederive SB001.
