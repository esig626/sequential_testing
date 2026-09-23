# Projection assisted upper bounds for the selected singleton contribution

Date: 23 September 2026.

Status: DERIVED, NOT INDEPENDENTLY REVIEWED. This note extends O020 in the singleton case. It does not claim that a Renyi projection alone solves the sample complexity problem.

## Question

For fixed lambda>1, n,m and first test phi_0, the exact selected future contribution is

[
d_{\lambda,1}(n,m;\varphi_0)
=
\frac{1}{\lambda-1}
\log
\mathbb E_{\nu_{\lambda,0}^{(1)}}
\left[
\exp\left\{
(\lambda-1)
D_\lambda\!\left(
Q_1(\cdot\mid X_0^n,A_0=1)
\middle\|
P_1(\cdot\mid X_0^n,A_0=1)
\right)
\right\}
\right].
]

Can a Renyi projection upper bound this quantity?

## 1. Why the projection from the finite sample composite paper does not directly help

A standard Renyi projection minimises a Renyi divergence over a set. Therefore, when the target pair itself belongs to the set being projected over, the projected value is no larger than the target divergence. It supplies a lower information value, not an upper information value.

In particular, if one minimises the conditional divergence over histories or over a family of candidate pairs, the resulting infimum is below the relevant conditional divergences. For lambda>1,

[
\inf_x D_\lambda(Q_1(\cdot\mid x,1)\Vert P_1(\cdot\mid x,1))
\leq
d_{\lambda,1}(n,m;\varphi_0)
\leq
\sup_x D_\lambda(Q_1(\cdot\mid x,1)\Vert P_1(\cdot\mid x,1)),
]

whenever the displayed extrema are interpreted on the relevant support and are finite. Thus the minimising projection points in the wrong direction for the converse upper-information step.

For singleton classes the joint Renyi projection is trivial: it returns the single pair itself.

## 2. Projection assisted change of measure

A projection can nevertheless be used indirectly as a choice of tractable reference law.

Let mu be any probability law on the old-data space such that
nu_{lambda,0}^{(1)} is absolutely continuous with respect to mu. Let r>1 and let s=r/(r-1). Holder gives

[
\begin{aligned}
&\mathbb E_{\nu_{\lambda,0}^{(1)}}
\left[
\exp\left\{
(\lambda-1)
D_\lambda\!\left(
Q_1(\cdot\mid X_0^n,1)
\middle\|
P_1(\cdot\mid X_0^n,1)
\right)
\right\}
\right]
\\
&\quad\leq
\exp\left\{\frac1s
D_r(\nu_{\lambda,0}^{(1)}\Vert\mu)\right\}
\left(
\mathbb E_\mu
\left[
\exp\left\{
s(\lambda-1)
D_\lambda\!\left(
Q_1(\cdot\mid X_0^n,1)
\middle\|
P_1(\cdot\mid X_0^n,1)
\right)
\right\}
\right]
\right)^{1/s}.
\end{aligned}
]

Consequently,

[
\begin{aligned}
d_{\lambda,1}(n,m;\varphi_0)
\leq
\frac{1}{s(\lambda-1)}
\Bigg[
&D_r(\nu_{\lambda,0}^{(1)}\Vert\mu)
\\
&+
\log
\mathbb E_\mu
\left[
\exp\left\{
s(\lambda-1)
D_\lambda\!\left(
Q_1(\cdot\mid X_0^n,1)
\middle\|
P_1(\cdot\mid X_0^n,1)
\right)
\right\}
\right]
\Bigg].
\end{aligned}
]

If mu is chosen from a tractable family by minimising the first Renyi divergence term, it is a projection assisted bound. But the minimiser of the mismatch term alone need not minimise the total right hand side, because the exponential future-information moment also depends on mu.

## 3. Natural reference: the unselected root tilt

The most immediate reference is mu=nu_{lambda,0}. Writing

[
\rho_{\lambda,0}
=
\mathbb E_{\nu_{\lambda,0}}[\varphi_0(X_0^n)],
]

we have

[
\frac{d\nu_{\lambda,0}^{(1)}}{d\nu_{\lambda,0}}(x)
=
\frac{\varphi_0(x)}{\rho_{\lambda,0}}.
]

Therefore

[
D_r(\nu_{\lambda,0}^{(1)}\Vert\nu_{\lambda,0})
=
\frac{1}{r-1}
\log
\frac{
\mathbb E_{\nu_{\lambda,0}}[\varphi_0(X_0^n)^r]
}{
\rho_{\lambda,0}^r
}
\leq
-\log\rho_{\lambda,0},
]

because 0<=phi_0<=1 implies phi_0^r<=phi_0.

Hence

[
\begin{aligned}
d_{\lambda,1}(n,m;\varphi_0)
\leq
\frac{1}{s(\lambda-1)}
\Bigg[
&-\log\rho_{\lambda,0}
\\
&+
\log
\mathbb E_{\nu_{\lambda,0}}
\left[
\exp\left\{
s(\lambda-1)
D_\lambda\!\left(
Q_1(\cdot\mid X_0^n,1)
\middle\|
P_1(\cdot\mid X_0^n,1)
\right)
\right\}
\right]
\Bigg].
\end{aligned}
]

At the iid root, nu_{lambda,0} is itself a product tilted law, so this may be easier to analyse than the selected law. It still does not remove the need to control the finite-sample exponential moment of the future conditional divergence.

## 4. Scope

The Renyi projection from the user's finite sample composite paper is an achievability construction and does not, by itself, provide the upper information bound needed here. In the singleton case it is also trivial. A projection can only assist after a change-of-measure inequality introduces a reference law and an explicit mismatch penalty.

No triangle inequality for Renyi divergence is being assumed. Any stronger comparison between the projected and original conditional kernels would need an additional model-specific inequality.
