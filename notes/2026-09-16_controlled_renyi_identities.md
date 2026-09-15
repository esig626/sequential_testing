# Controlled Rényi identities: working derivations

Date: 16 September 2026. Base manuscript: `sequential_testing.tex` at `a7765a057b1879dc12a3fc66359e5f2b9a52ebd8`.

Status: elementary derivations with finite numerical checks. Independent mathematical review and a novelty audit remain pending. The backward recursion itself was already in the manuscript.

Throughout, use a fixed pair $\mathbf P,\mathbf Q$, a fixed common policy $\boldsymbol\phi$, finite observation alphabets and $0<\lambda<1$. Natural logarithms are used. Kernels may have zeros. Conditional expressions involving both models are evaluated at histories of positive reach under both. The initial sampler has the stronger matching conditional support requirement.

## 1. The same action kernel, two controlled path laws

For a reached pair $(h,x)$ let $k(a)=\kappa_{\phi_t}(a\mid h,x)$. The local joint masses are $p_t(x\mid h)k(a)$ and $q_t(x\mid h)k(a)$. On a common positive branch,

$$
[q_t(x\mid h)k(a)]^\lambda[p_t(x\mid h)k(a)]^{1-\lambda}
=q_t(x\mid h)^\lambda p_t(x\mid h)^{1-\lambda}k(a).
$$

If $k(a)=0$, the joint summand is zero. There is no division of zero by zero. Repeated multiplication proves the likelihood ratio cancellation and the manuscript's $G_t$ recursion.

Cancellation is not policy invariance: the history passed to the next kernel contains $a$. Only when future observations do not depend on the actions can the full action sum be removed without changing those future laws. The final action cannot change the divergence of the full transcript through time $T$, because there is no remaining observation after it. Projecting to actions alone is a different operation.

For nonidentical independent observation kernels, summing all common action probabilities for each fixed observation path gives one. Thus even with a history dependent common policy, the full transcript integral reduces to the product of the observation integrals. This agrees with Rényi additivity [R2 in the research plan].

## 2. Exact prefix accumulation

Let $p_{\leq t}^{\boldsymbol\phi}$ and $q_{\leq t}^{\boldsymbol\phi}$ be the prefix masses on $H_t$. Define

$$
\mathsf H_{\lambda,t}^{\boldsymbol\phi}
=\sum_{h_t}(q_{\leq t}^{\boldsymbol\phi}(h_t))^\lambda
               (p_{\leq t}^{\boldsymbol\phi}(h_t))^{1-\lambda},
\qquad \mathsf H_{\lambda,0}^{\boldsymbol\phi}=1.
$$

When $\mathsf H_{\lambda,t-1}^{\boldsymbol\phi}>0$, define the tilted prefix probability

$$
\nu_{\lambda,t-1}^{\boldsymbol\phi}(h)
=\frac{(q_{\leq t-1}^{\boldsymbol\phi}(h))^\lambda
       (p_{\leq t-1}^{\boldsymbol\phi}(h))^{1-\lambda}}
       {\mathsf H_{\lambda,t-1}^{\boldsymbol\phi}}.
$$

Expanding the next stage and summing the common action kernel gives

$$
\mathsf H_{\lambda,t}^{\boldsymbol\phi}
=\mathsf H_{\lambda,t-1}^{\boldsymbol\phi}
  \mathbb E_{\nu_{\lambda,t-1}^{\boldsymbol\phi}}
  [z_{\lambda,t}(H_{t-1})].
$$

Consequently, when both integrals are positive, the prefix divergence increment is

$$
\frac{1}{\lambda-1}\log
\mathbb E_{\nu_{\lambda,t-1}^{\boldsymbol\phi}}
[z_{\lambda,t}(H_{t-1})].
$$

It is not generally the expectation of $D_\lambda(Q_t(\cdot\mid H_{t-1})\Vert P_t(\cdot\mid H_{t-1}))$. If a prefix integral is zero, the two prefix laws have no common support and subsequent full transcript integrals remain zero. Do not normalise that zero measure.

## 3. Current observation conditioned on the selected branch

Fix a common positive reach history $h$ and a branch $a$. Let

$$
\rho_{P,t}(a\mid h)=\sum_xp_t(x\mid h)\kappa_{\phi_t}(a\mid h,x),
\qquad
\rho_{Q,t}(a\mid h)=\sum_xq_t(x\mid h)\kappa_{\phi_t}(a\mid h,x).
$$

Assume these are positive and $z=z_{\lambda,t}(h)>0$. Define the local tilted kernel

$$
\widetilde R_{\lambda,t}(x\mid h)
=\frac{q_t(x\mid h)^\lambda p_t(x\mid h)^{1-\lambda}}{z},
\qquad
\rho_{\lambda,t}(a\mid h)
=\sum_x\widetilde R_{\lambda,t}(x\mid h)\kappa_{\phi_t}(a\mid h,x).
$$

The selected laws of $X_t$ are

$$
P_t^{h,a}(x)=\frac{p_t(x\mid h)\kappa_{\phi_t}(a\mid h,x)}{\rho_{P,t}(a\mid h)},
\quad
Q_t^{h,a}(x)=\frac{q_t(x\mid h)\kappa_{\phi_t}(a\mid h,x)}{\rho_{Q,t}(a\mid h)}.
$$

Substitution, using that the power on the common action factor is one, yields

$$
H_\lambda(Q_t^{h,a},P_t^{h,a})
=z\frac{\rho_{\lambda,t}(a\mid h)}
        {\rho_{Q,t}(a\mid h)^\lambda\rho_{P,t}(a\mid h)^{1-\lambda}}.
$$

Taking logarithms gives the selection correction in the plan. If the two ordinary branch probabilities are positive but $\rho_{\lambda,t}=0$, the selected integral is zero and the selected divergence is infinite. If either ordinary branch probability is zero, its selected conditional law is undefined and the comparison is not asserted.

The same algebra applies to a common positive probability event in a full prefix or full path law, using the tilted law of that entire object. It does not justify substituting the local tilted kernel for that full tilted law. The conditioning event probability cost must be included in an algorithm.

When later observations deterministically reproduce the stored original observation, their conditional kernels coincide at every commonly reached history, so $z_{\lambda,t}=1$ for $t>1$. The full transcript has the divergence of the original observation. Conditioning that transcript on reported decisions can still produce the three probability correction. This is the precise boundary relation to the same data project.

## 4. Predictable gap estimator with observed actions

Under the mixture $M^{\boldsymbol\phi}$ let $\omega_t=\Pr(J=\mathbf Q\mid\mathcal F_t)$, with $\omega_0=1/2$. At a fixed history, write $\omega=\omega_{t-1}$ and

$$
m(x)=(1-\omega)p_t(x\mid h)+\omega q_t(x\mid h).
$$

For $m(x)>0$, the posterior after observing $x$ is

$$
\omega^+(x)=\frac{\omega q_t(x\mid h)}{m(x)}.
$$

Conditioning further on a possible action $a$ leaves that posterior unchanged, because the action has the same conditional distribution under both models. Hence $\omega_t=\omega^+(X_t)$, although its next update depends on the chosen history.

For $w_\lambda(u)=2u^\lambda(1-u)^{1-\lambda}$,

$$
\begin{aligned}
\mathbb E[w_\lambda(\omega_t)\mid\mathcal F_{t-1}]
&=\sum_{x,a}m(x)\kappa_{\phi_t}(a\mid h,x)
\,2\left(\frac{\omega q_t(x\mid h)}{m(x)}\right)^\lambda
\left(\frac{(1-\omega)p_t(x\mid h)}{m(x)}\right)^{1-\lambda}\\
&=w_\lambda(\omega)z_{\lambda,t}(h).
\end{aligned}
$$

Zero probability summands are omitted. If $\omega$ is zero or one, both the current and all future weights are zero almost surely, so set the increment to zero without consulting the absent model's conditional law.

Define $C_{\lambda,t}=w_\lambda(\omega_{t-1})(1-z_{\lambda,t})$. Hölder's inequality gives $z_{\lambda,t}\leq1$, so these increments are nonnegative. They are measurable before $X_t$. Moreover,

$$
\mathbb E\mathcal A_\lambda^{\boldsymbol\phi}
=w_\lambda(1/2)-\mathbb E w_\lambda(\omega_T).
$$

Writing the terminal posterior in terms of the two full path masses shows

$$
\mathbb E w_\lambda(\omega_T)
=H_\lambda(\mathbb P_{\mathbf Q}^{\boldsymbol\phi},
           \mathbb P_{\mathbf P}^{\boldsymbol\phi}).
$$

Since $w_\lambda(1/2)=1$, unbiasedness follows. This proof does not require observation independence. It does require that the simulation use the actual conditional kernels and the same specified policy, rather than adapt that policy to the hidden simulation label.

## 5. Remaining gain and second moment

Apply the same calculation to the entire conditional future experiment at a common reached history. Its Hellinger integral is $G_t(h)$. Conditional telescoping yields

$$
\mathcal B_{\lambda,t}
:=\mathbb E\left[\sum_{j=t}^T C_{\lambda,j}\mid\mathcal F_{t-1}\right]
=w_\lambda(\omega_{t-1})[1-G_t(H_{t-1})].
$$

At a history reached under only one model the remaining gain is zero; no intrinsic two model conditional comparison is needed there.

Suppose $\Delta=\Delta_\lambda^{\boldsymbol\phi}>0$ and a known $K\geq1$ satisfies $\mathcal B_{\lambda,t}\leq K\Delta$ almost surely for every stage. Abbreviate $\mathcal A=\sum_tC_t$. Then

$$
\mathcal A^2=2\sum_tC_t\sum_{j=t}^TC_j-\sum_tC_t^2.
$$

Because $C_t$ is measurable with respect to $\mathcal F_{t-1}$,

$$
\mathbb E\mathcal A^2
=2\sum_t\mathbb E[C_t\mathcal B_{\lambda,t}]-\sum_t\mathbb EC_t^2
\leq2K\Delta\sum_t\mathbb EC_t
=2K\Delta^2.
$$

Thus relative variance is at most $2K-1$. Groups of at least $\lceil8K/\epsilon_{\rm gap}^2\rceil$ independent samples have relative error at most $\epsilon_{\rm gap}$ with probability at least $3/4$ by Chebyshev. Take the median of an odd number of independent group means, at least $8\log(1/\delta)$, to obtain failure probability at most $\delta$.

At $\Delta=0$, exact nonnegativity and zero mean imply $\mathcal A=0$ almost surely. Floating point cancellation and model equality testing are separate computational issues.

In the independent observation control, the suffix gap is no larger than the full gap and

$$
w_\lambda(u)\leq 2\lambda^\lambda(1-\lambda)^{1-\lambda}=:B_\lambda.
$$

Therefore $K=B_\lambda$ suffices there. Exact additivity is still preferable computationally. In the rare action example, $\mathcal B_{\lambda,2}=d_\lambda$ on the rare branch while $\Delta=\tau d_\lambda$, forcing $K\geq1/\tau$. The conditional lemma alone is not the desired new theorem.

## 6. Local tilting versus global tilting

For $z_{\lambda,t}>0$, sampling the observation under $\widetilde R_{\lambda,t}$ and the action under $\kappa_{\phi_t}$ produces the path mass

$$
\prod_t\frac{q_t(x_t\mid h)^\lambda p_t(x_t\mid h)^{1-\lambda}
\kappa_{\phi_t}(a_t\mid h,x_t)}{z_{\lambda,t}(h)}.
$$

Multiplication by $\prod_tz_{\lambda,t}(h)$ and summation proves the locally tilted importance sampling identity in the plan, assuming the normalisers on simulated paths are positive. More general zeros require a stated killed path convention.

In contrast, the transition under the normalised global tilted path law is

$$
\frac{q_t(x\mid h)^\lambda p_t(x\mid h)^{1-\lambda}
\kappa_{\phi_t}(a\mid h,x)G_{t+1}(h,x,a)}{G_t(h)}
$$

when $G_t(h)>0$. It generally reweights actions as well as observations. Local normalisation alone does not simulate this global law. Using exact $G_t$ in a proposed fast algorithm is circular unless its construction cost is included.

## 7. Error conversion

For $H=1-\Delta>0$, the mean value theorem applied to $-\log(1-x)$ yields

$$
\frac{|\widehat D-D|}{D}
\leq\frac{|\widehat\Delta-\Delta|}
{(H-|\widehat\Delta-\Delta|)(-\log H)}
$$

whenever $|\widehat\Delta-\Delta|<H$. Substitute the relative gap bound to obtain the formula in the plan. Under $\Delta\leq\gamma$, use $-\log(1-\Delta)\geq\Delta$ and $\epsilon_{\rm gap}=\varepsilon(1-\gamma)/2$ to obtain relative divergence error at most $\varepsilon$.

For orders above one with finite divergence, write $\Delta=H-1$. Since $f(x)=\log(1+x)$ is concave and $f(0)=0$,

$$
f((1-\epsilon_{\rm gap})x)\geq(1-\epsilon_{\rm gap})f(x),\qquad
f((1+\epsilon_{\rm gap})x)\leq(1+\epsilon_{\rm gap})f(x).
$$

A relative gap bound therefore transfers directly to relative divergence error. This argument does not bound the variance of any estimator above order one.

## 8. Why path risk needs its own analysis

For a fixed environment $\eta$, define $W_t^\eta(h)$ as the conditional probability of at least one future error from stage $t$ onward, with $W_{T+1}^\eta=0$. Direct conditioning gives

$$
W_t^\eta(h)=\sum_xR_t(x\mid h)\sum_a\kappa_{\phi_t}(a\mid h,x)
\left[\mathbf1_{\{a\ne\vartheta(v_t(h))\}}+
\mathbf1_{\{a=\vartheta(v_t(h))\}}W_{t+1}^\eta(h,x,a)\right].
$$

The root value is the probability of any error. The earlier error indicator makes failure absorbing in this recursion. This is a fixed environment identity, not a robust Bellman theorem.

To see the truth map obstruction, take a fair $X_1$ and $A_1=0$, with the root truth also zero. Both possible $X_1$ values reach the same next node. Let $A_2=X_1$, ignoring any new $X_2$. For either fixed truth label at the second node, the error probability is $1/2$. An invalid history dependent choice $\Theta_2=1-X_1$ gives error probability one. Moving a supremum over node truth maps inside each history update would make exactly this invalid substitution.

This example is compatible with the manuscript's allowance of overlapping local classes. It also works with distinct classes by choosing suitable second stage kernels, since the displayed policy ignores the new observation. It explains why kernel rectangularity and truth map consistency must be addressed separately.
