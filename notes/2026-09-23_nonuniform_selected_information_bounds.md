# Nonuniform bounds for the selected conditional Renyi contribution

Date: 23 September 2026.

Extends O019, R033 to R037 and M012 to M014. The exact chain rule and backward moment recursion are inputs from R004/R028/R029 and R001, not new claims. The extension constructs bounds using averages over histories instead of an assumed uniform information cap. The user's uploaded working notes and the original manuscript are unchanged.

Status: DERIVED, NOT INDEPENDENTLY REVIEWED. Fifteen local deterministic check methods passed. No novelty claim, general efficiency claim, achievability result, or exact minimax sample complexity claim is made.

## 1. Fixed experiment and current notation

Fix lambda>1, n, m, a coherent singleton pair, and a common first test phi_0. The root laws are P_0^(tensor n) and Q_0^(tensor n), with P_0,Q_0 single observation laws. Assume positive branch reach and finite root Renyi moment. The new block may depend on the entire old block and have arbitrary internal dependence.

In the user's current notation,

$$
d_{\lambda,1}(n,m;\varphi_0)=\frac{1}{\lambda-1}\log\mathbb E_{\nu_{\lambda,0}^{(1)}}\left[\exp\left\{(\lambda-1)D_\lambda\!\left(Q_1(\cdot\mid X_0^n,A_0=1)\middle\|P_1(\cdot\mid X_0^n,A_0=1)\right)\right\}\right]. \tag{1}
$$

This is the scalar called T_{lambda,1} in the 16 September note. Do not use d_{lambda,1}(x) for the pointwise conditional divergence in new work. Write that divergence out. The first test is fixed, not optimised independently of the selected laws.

For every nonnegative measurable f, the selected tilted old law is characterised by

$$
\mathbb E_{\nu_{\lambda,0}^{(1)}}[f(X_0^n)]
=\frac{\mathbb E_{P_0^{\otimes n}}[\varphi_0(X_0^n)L_0(X_0^n)^\lambda f(X_0^n)]}{\mathbb E_{P_0^{\otimes n}}[\varphi_0(X_0^n)L_0(X_0^n)^\lambda]},
\qquad L_0=\frac{dQ_0^{\otimes n}}{dP_0^{\otimes n}}.
$$

Assume standard Borel spaces and measurable conditional kernels. The clean derivative calculations below use common conditional support, including all checked finite and Gaussian models. The one sided extension is described in Section 8. Finiteness of a density ratio moment is an additional requirement, not a consequence of absolute continuity.

Write X_1^{j-1}=(X_{1,1},...,X_{1,j-1}), with the prefix empty at j=1. Let P_{1,j} and Q_{1,j} be the conditional laws of the single next observation given X_0^n, X_1^{j-1}, A_0=1. Let P_1^{[j-1]} denote the null law of the prefix of j-1 new observations, conditional on X_0^n,A_0=1. Square brackets indicate a marginal, not an independent product. For comparisons across m, these prefixes must belong to one coherent observation process.

## 2. Exact product of conditional likelihood ratios

Define

$$
\ell_{1,j}(x,y_1^j):=\frac{dQ_{1,j}(\cdot\mid x,y_1^{j-1},A_0=1)}{dP_{1,j}(\cdot\mid x,y_1^{j-1},A_0=1)}(y_j).
$$

The conditional likelihood ratio of the whole new block is the product of these factors. The factors are not assumed independent. Therefore

$$
\exp\{(\lambda-1)d_{\lambda,1}(n,m;\varphi_0)\}
=\mathbb E_{\nu_{\lambda,0}^{(1)}}\left[\mathbb E_{P_1(\cdot\mid X_0^n,A_0=1)}\left[\prod_{j=1}^m\ell_{1,j}(X_0^n,X_1^j)^\lambda\right]\right]. \tag{2}
$$

This identifies the probability measure under every expectation: old histories are sampled from the selected root tilt; the new observations then follow the dependent null kernels. It is an auxiliary measure for calculation, not a claim about the actual generating model.

## 3. General bound from averaged observation moments

Choose positive weights w_1,...,w_m summing to one. Define the following moments explicitly:

$$
\begin{aligned}
K_{\lambda,j}(n;\varphi_0,w_j):=
\mathbb E_{\nu_{\lambda,0}^{(1)}}\Bigg[
\mathbb E_{P_1^{[j-1]}(\cdot\mid X_0^n,A_0=1)}\Bigg[
\exp\Bigg\{\left(\frac{\lambda}{w_j}-1\right)
D_{\lambda/w_j}\!\Big(
&Q_{1,j}(\cdot\mid X_0^n,X_1^{j-1},A_0=1)
\\[-2pt]
\Big\|\;&P_{1,j}(\cdot\mid X_0^n,X_1^{j-1},A_0=1)
\Big)\Bigg\}\Bigg]\Bigg].
\end{aligned} \tag{3}
$$

For j=1, the empty prefix average does nothing. If kernels themselves are horizon dependent, include m among the arguments as well. A constructed deterministic bound is

$$
b_\lambda^{\rm moment}(n,m;\varphi_0):=
\inf_{\substack{w_j>0\\\sum_{j=1}^m w_j=1}}
\frac{1}{\lambda-1}\sum_{j=1}^m w_j\log K_{\lambda,j}(n;\varphi_0,w_j).
\tag{4}
$$

Then

$$
d_{\lambda,1}(n,m;\varphi_0)\leq b_\lambda^{\rm moment}(n,m;\varphi_0). \tag{5}
$$

A sufficient condition for a finite bound is existence of one weight vector for which every moment in (3) is finite. This is not a uniform bound over histories. The conditional divergences may be unbounded functions of the old data or the new prefix.

Proof. Apply generalised Holder with exponents 1/w_j to (2). The result is

$$
\begin{aligned}
&\mathbb E_{\nu_{\lambda,0}^{(1)}}\left[\mathbb E_{P_1(\cdot\mid X_0^n,A_0=1)}\left[\prod_j\ell_{1,j}^\lambda\right]\right]
\\
&\quad\leq\prod_j\left(\mathbb E_{\nu_{\lambda,0}^{(1)}}\left[\mathbb E_{P_1(\cdot\mid X_0^n,A_0=1)}[\ell_{1,j}^{\lambda/w_j}]\right]\right)^{w_j}.
\end{aligned}
$$

For each factor, integrate out observations after j, then condition on the old data and the first j-1 new observations. The remaining single observation expectation is the Renyi moment at order lambda/w_j, exactly (3). Taking logarithms, dividing by lambda-1, and optimising the weights proves (5). Nonnegative integrals justify the conditioning even when a bound is infinite. No independence is used. At m=1, choose w_1=1 and obtain equality.

Limitations. Larger orders are required: equal weights use order m lambda. Thus this sufficient condition can fail when (1) is finite. For an explicit example, on positive integers put P(k)=exp(-lambda k)/(k^2 Z_P) and Q(k)=exp(-(lambda-1)k)/(k^2 Z_Q), with finite normalising sums Z_P,Z_Q. The likelihood ratio is (Z_P/Z_Q)exp(k). Its order lambda moment is finite, but every higher order moment is infinite. Let a second new observation copy the first. The whole two observation divergence remains finite, whereas (4), with both weights strictly positive, is infinite. Removing an identically one likelihood factor before Holder fixes this example; the displayed criterion is nevertheless not necessary for finiteness.

The prefix averages in (3) can also be computationally expensive. This is a mathematical bound, not a general fast algorithm. Conditional Holder before the old data average and grouping consecutive observations can sharpen the bound. The limiting choice of one group containing the entire block is merely (1), not an additional computable result.

## 4. Bounds at the original order via local integral comparisons

Reuse the backward moment recursion R001. Let G_{lambda,j}(x,y_1^j) be the moment still to be accumulated from observations j+1 through m after fixing that prefix. Set G_{lambda,m}=1 and, backwards for j=m,...,1,

$$
G_{\lambda,j-1}(x,y_1^{j-1})=
\mathbb E_{P_{1,j}(\cdot\mid x,y_1^{j-1},A_0=1)}\left[
\ell_{1,j}(x,y_1^{j-1},X_{1,j})^\lambda G_{\lambda,j}(x,y_1^{j-1},X_{1,j})\right]. \tag{6}
$$

Then exactly

$$
d_{\lambda,1}(n,m;\varphi_0)=\frac{1}{\lambda-1}\log\mathbb E_{\nu_{\lambda,0}^{(1)}}[G_{\lambda,0}(X_0^n)]. \tag{7}
$$

To build upper bounds, choose nonnegative measurable functions v_j on the prefixes, with v_m>=1, satisfying the checkable one observation inequalities

$$
\mathbb E_{P_{1,j}(\cdot\mid x,y_1^{j-1},A_0=1)}\left[
\ell_{1,j}(x,y_1^{j-1},X_{1,j})^\lambda v_j(x,y_1^{j-1},X_{1,j})\right]
\leq v_{j-1}(x,y_1^{j-1}). \tag{8}
$$

Backward induction proves G_{lambda,j}<=v_j. Thus

$$
d_{\lambda,1}(n,m;\varphi_0)
\leq\frac{1}{\lambda-1}\log\mathbb E_{\nu_{\lambda,0}^{(1)}}[v_0(X_0^n)]. \tag{9}
$$

The functions v_j may be unbounded, provided the final expectation is finite. Existence of useful v_j is a model calculation; (8) must be checked, not merely asserted. The following example solves (6) exactly. General full history recursion is still potentially exponential in history length.

## 5. Exact Gaussian feedback example beyond every uniform history bound

This is an illustrative model introduced for this task, not an imposed restriction on the general theorem. Unlike R037, its conditional mean difference depends on previous new data and is unbounded over histories.

Let P_0=N(0,sigma_0^2), Q_0=N(delta,sigma_0^2), delta nonzero, with iid root data. Define the observed sample mean S_n=n^(-1) sum_i X_{0,i}. Under nu_{lambda,0}, S_n has Gaussian mean lambda delta and variance sigma_0^2/n. This follows by completing the square in the root tilted density.

Initialise the stored value X_{1,0}=S_n, not an extra new sample. Choose distinct nonzero coefficients a,b and specify

$$
P_{1,j}(\cdot\mid x,y_1^{j-1},A_0=1)=\mathcal N(a y_{j-1},\sigma_1^2),
$$

$$
Q_{1,j}(\cdot\mid x,y_1^{j-1},A_0=1)=\mathcal N(b y_{j-1},\sigma_1^2),
$$

where y_0=S_n(x). Both coefficients can have absolute value below one. The new observations are correlated even conditional on the whole old block.

The single next observation divergence at a preceding value s is

$$
D_\lambda\big(\mathcal N(bs,\sigma_1^2)\|\mathcal N(as,\sigma_1^2)\big)
=\frac{\lambda(b-a)^2s^2}{2\sigma_1^2}.
$$

It is finite for every finite s, but has no finite uniform bound.

The moment of the next k observations given s has the form exp(A_k s^2+B_k), where A_k,B_k are deterministic coefficients, not actions or errors. Set A_0=B_0=0 and calculate

$$
A_{k+1}=\frac{\lambda(\lambda-1)(b-a)^2}{2\sigma_1^2}
+\frac{(a+\lambda(b-a))^2 A_k}{1-2\sigma_1^2 A_k}, \tag{10}
$$

$$
B_{k+1}=B_k-\frac12\log(1-2\sigma_1^2 A_k). \tag{11}
$$

These steps require 1-2 sigma_1^2 A_k>0. If it fails, the corresponding Gaussian moment diverges.

Proof of recursion. The unnormalised integrand q^lambda p^(1-lambda) is a Gaussian density of mean (a+lambda(b-a))s and variance sigma_1^2, multiplied by exp(lambda(lambda-1)(b-a)^2 s^2/(2 sigma_1^2)). Integrating exp(A_k y^2+B_k) against it gives (10) and (11) by completing the square.

It follows that

$$
d_{\lambda,1}(n,m;\varphi_0)=\frac{B_m}{\lambda-1}
+\frac{1}{\lambda-1}\log
\frac{\mathbb E_{\nu_{\lambda,0}}[\varphi_0(X_0^n)e^{A_m S_n^2}]}{\mathbb E_{\nu_{\lambda,0}}[\varphi_0(X_0^n)]}. \tag{12}
$$

For any fixed first test, bounding its numerator by E_nu exp(A_m S_n^2), using phi_0<=1, gives the explicit finite bound

$$
\begin{aligned}
b_\lambda^{\rm Gaussian}(n,m;\varphi_0)=\frac{1}{\lambda-1}\Bigg[
&B_m-\log\mathbb E_{\nu_{\lambda,0}}[\varphi_0(X_0^n)]
\\
&-\frac12\log\left(1-\frac{2A_m\sigma_0^2}{n}\right)
+\frac{A_m\lambda^2\delta^2}{1-2A_m\sigma_0^2/n}\Bigg],
\end{aligned} \tag{13}
$$

provided 1-2 A_m sigma_0^2/n>0. This is a sufficient condition for this bound, not a necessary condition for the selected quantity to be finite: the first test could remove the problematic old tails.

The m dependence comes from a scalar recursion; n appears explicitly and through the first test's tilted branch reach. A uniform bound on the conditional block divergence over old histories is infinite, but (13) can be finite.

Numerical example: lambda=2, a=0.5, b=0.6, sigma_0=sigma_1=1, delta=0.5. Use phi_0(x)=0.05+0.90 times the indicator that S_n(x)>0.5. For n=4 and n=20 this satisfies epsilon_0=0.2. At n=4,m=5, exact (12) is 0.09124582897 and (13) is 0.30145769764. At n=20,m=5 they are 0.08338494617 and 0.14655199210. These are information quantities, not sufficient sample counts. The first test is an illustration, not an optimality claim.

The recursion was also checked against direct integration of the complete joint Gaussian vector for multiple n,m,lambda. For the displayed nonconstant first rule the selected square moment can be integrated by Gaussian truncation. Fifteen finite check methods covered these cases and the general inequalities.

## 6. What the chain rule says about sample counts

Let nu_{lambda,1}^{[j]} denote the normalised Renyi tilt of the full selected prefix (X_0^n,X_1^j), not the root tilt held fixed. Its expectations are proportional to

$$
\mathbb E_{\nu_{\lambda,0}^{(1)}}\left[\mathbb E_{P_1^{[j]}(\cdot\mid X_0^n,A_0=1)}\left[f\prod_{i=1}^j\ell_{1,i}^\lambda\right]\right],
$$

normalised by the same expression with f=1. At j=0 this is exactly nu_{lambda,0}^{(1)}. The established chain rule then gives

$$
\begin{aligned}
d_{\lambda,1}(n,j;\varphi_0)-d_{\lambda,1}(n,j-1;\varphi_0)
=\frac{1}{\lambda-1}\log\mathbb E_{\nu_{\lambda,1}^{[j-1]}}\Big[\exp\big\{(\lambda-1)D_\lambda\big(
&Q_{1,j}(\cdot\mid X_0^n,X_1^{j-1},A_0=1)
\\[-2pt]
\big\|\;&P_{1,j}(\cdot\mid X_0^n,X_1^{j-1},A_0=1)\big)\big\}\Big].
\end{aligned} \tag{14}
$$

This exact identity requires finite prefix normalisers. It shows monotonicity in j for a coherent prefix process and fixed n,phi_0. There is no automatic monotonicity in n when the first test or future experiment changes. The tilted prefix laws must be updated, not replaced by a product of locally normalised tilts; F009 still applies.

## 7. Two precise obstructions to stronger blanket claims

First, there is no finite bound depending on counts alone over all unrestricted models. At m=1 let Q_1 be Bernoulli(1/2) and P_1 be Bernoulli(p), independently of x. For lambda=2,

$$
d_{2,1}=\log\left(\frac{1}{4p}+\frac{1}{4(1-p)}\right),
$$

which grows without bound as p approaches zero even though every p>0 has common support and finite divergence. An independent example suffices because it is a subclass of the unrestricted model.

Pointwise finiteness is also insufficient. If an old tilted Gaussian variable S has variance at least 1/2, the next laws N(0,1) and N(S,1) have finite order two divergence S^2 at every realised S, but E exp(S^2) is infinite. Positive constant branch randomisation leaves that divergence of the outer moment unchanged.

Second, for fixed kernels and root laws, maximising (1) over every positive reach root test with alpha_0<=epsilon_0 recovers the least upper bound on the pointwise conditional block divergence outside a set of total nu_{lambda,0} measure zero. Thus an unbounded conditional divergence prevents a finite upper bound uniform over ALL such tests, even when the fixed test bound is finite.

Proof. The upper direction is the uniform bound implication. Conversely take a level t below the asserted upper bound and the set E of histories whose conditional block divergence exceeds t. It has positive tilted and null measure. The rule

$$
\varphi_0(x)=\min\left\{1,\frac{\varepsilon_0}{\mathbb E_{P_0^{\otimes n}}[\mathbf1_E(X_0^n)]}\right\}\mathbf1_E(x)
$$

is admissible. Its selected tilted law is the root tilt conditional on E, so (1) is at least t. Let t increase. No least favourable distribution is used.

A lower root power requirement changes this issue. Holder gives

$$
\mathbb E_{\nu_{\lambda,0}}[\varphi_0]
\geq\frac{(1-\beta_0)^\lambda}{\alpha_0^{\lambda-1}\exp\{(\lambda-1)nD_\lambda(Q_0\|P_0)\}}.
$$

This can control the selection denominator when root power is bounded below. A Type I upper budget alone does not give that lower reach.

## 8. Support and scope

For one sided absolute continuity, if a prefix already has zero alternative density relative to the null, its accumulated likelihood ratio is zero. Later ratios may be set to one in the product and upper moment bound, equivalently by declaring a matching null kernel extension on those absent alternative histories. Do not query undefined alternative conditionals as intrinsic data. Null zero histories are not integrated under the null. A singular alternative component on a positively weighted history makes the finite order above one bound inapplicable. Conditional versions and extension conventions must be stated.

The results concern a fixed coherent pair and first test. No composite minimax optimisation is silently moved inside history averages. A general formula for b need not be finite for every model or cheap to evaluate. The original source converse is not rederived. These bounds can be inserted into R033/R034 subject to their original scopes, but matching achievability and general sample complexity remain separate problems.

## 9. Source and verification record

Repository inputs checked: R001/R004/R026 to R037, M012 to M014, O019 and F009/F019 to F021; source library README and bibliographies; the conditional Renyi source record and original controlled identities note. The uploaded 16 September note and current user notes supply the starting definitions and uniform bound implication, not the new constructions above.

Existing primary reference rechecked: Polyanskiy and Wu, Information Theory: From Coding to Learning, prepublication version 16 August 2024, Section 7.12, equations (7.77) and (7.78), printed page 145, https://people.lids.mit.edu/yp/homepage/data/itbook-export.pdf . Reading depth: parsed primary source equation text; the requested screenshots failed to fetch. No broad literature survey or independent novelty audit was performed. No third party full text is mirrored. Holder and Gaussian square completion are standard tools; no novelty for those tools or these general methods is asserted.

Local verification: fifteen deterministic methods passed, zero failures and errors, under Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. Finite enumeration and full joint Gaussian integrals checked the formulas. The older repository suite was not rerun and no production code was modified. This is not independent mathematical review or remote CI evidence. See the associated verification record for numerical values and scope.
