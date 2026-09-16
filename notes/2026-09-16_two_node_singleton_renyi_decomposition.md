# Two-node singleton Rényi decomposition after branch selection

Date: 16 September 2026.

Status: DERIVED — UNREVIEWED. No numerical check has yet been performed. This note records the first explicit two-node calculation for the current error-propagation programme. It overlaps the already-recorded branch-selection correction in R005, but adds the dependent new-data contribution explicitly.

## Setup

Consider a two-node singleton problem.

At node 0, let `P_0` and `Q_0` be the two laws for the old data `X_0^n`. Let the randomised test be `phi_0(x) in [0,1]`, and consider the realised branch `A_0 = 1`.

Define

\[
\alpha_0 = \mathbb E_{P_0}[\phi_0(X_0^n)],
\qquad
1-\beta_0 = \mathbb E_{Q_0}[\phi_0(X_0^n)].
\]

Assume positive reach under both laws:

\[
\alpha_0>0,
\qquad
1-\beta_0>0.
\]

Write `x` for a realised value of the old data `X_0^n`, and `y` for a realised value of the new data `X_1^m`.

Let `p_0(x)` and `q_0(x)` denote densities of `P_0` and `Q_0` with respect to a common dominating measure.

Let

\[
p_1(y\mid x,1),
\qquad
q_1(y\mid x,1)
\]

be the conditional densities of the new data at node 1 given old data `x` and branch `A_0=1`. No independence or iid assumption is imposed on the new block.

The branch-selected joint densities on `(x,y)` are

\[
\widetilde p_1(x,y)
=
\frac{\phi_0(x)}{\alpha_0}
 p_0(x)p_1(y\mid x,1),
\]

and

\[
\widetilde q_1(x,y)
=
\frac{\phi_0(x)}{1-\beta_0}
 q_0(x)q_1(y\mid x,1).
\]

## Exact Rényi integral

For Rényi order `lambda != 1`, use the convention

\[
D_\lambda(Q\|P)
=
\frac{1}{\lambda-1}
\log \int q^\lambda p^{1-\lambda}.
\]

Define the conditional Hellinger/Rényi integral of the new data by

\[
z_\lambda(x)
:=
\int
q_1(y\mid x,1)^\lambda
p_1(y\mid x,1)^{1-\lambda}
\,dy.
\]

Then

\[
\int\!\!\int
\widetilde q_1(x,y)^\lambda
\widetilde p_1(x,y)^{1-\lambda}
\,dx\,dy
=
\frac{1}{(1-\beta_0)^\lambda\alpha_0^{1-\lambda}}
\int
\phi_0(x)
q_0(x)^\lambda
p_0(x)^{1-\lambda}
z_\lambda(x)
\,dx.
\]

The randomisation enters only to the first power because

\[
\phi_0(x)^\lambda\phi_0(x)^{1-\lambda}=\phi_0(x).
\]

## Tilted decomposition

Define the node-0 Rényi integral

\[
H_{\lambda,0}
:=
\int q_0(x)^\lambda p_0(x)^{1-\lambda}\,dx,
\]

so that

\[
D_\lambda(Q_0\|P_0)
=
\frac{1}{\lambda-1}\log H_{\lambda,0}.
\]

Define the node-0 tilted law

\[
\nu_{\lambda,0}(dx)
:=
\frac{q_0(x)^\lambda p_0(x)^{1-\lambda}}
{H_{\lambda,0}}\,dx.
\]

Define the tilted reach of branch 1

\[
\rho_{\lambda,0}
:=
\int \phi_0(x)\,\nu_{\lambda,0}(dx).
\]

Assuming `rho_{lambda,0}>0`, define the tilted law after branch selection

\[
\nu_{\lambda,0}^{(1)}(dx)
:=
\frac{\phi_0(x)}{\rho_{\lambda,0}}
\nu_{\lambda,0}(dx).
\]

Then the exact two-node decomposition is

\[
\boxed{
\begin{aligned}
D_\lambda(\widetilde Q_1\|\widetilde P_1)
={}&D_\lambda(Q_0\|P_0)\\
&+\frac{1}{\lambda-1}
\log\frac{\rho_{\lambda,0}}
{(1-\beta_0)^\lambda\alpha_0^{1-\lambda}}\\
&+\frac{1}{\lambda-1}
\log
\mathbb E_{\nu_{\lambda,0}^{(1)}}
[z_\lambda(X_0^n)].
\end{aligned}
}
\]

Equivalently, since

\[
z_\lambda(x)
=
\exp\!\left((\lambda-1)
D_\lambda\bigl(Q_1(\cdot\mid x,1)\|P_1(\cdot\mid x,1)\bigr)\right),
\]

the dependent new-data term is

\[
\frac{1}{\lambda-1}
\log
\mathbb E_{\nu_{\lambda,0}^{(1)}}
\left[
\exp\!\left((\lambda-1)
D_\lambda\bigl(Q_1(\cdot\mid X_0^n,1)\|P_1(\cdot\mid X_0^n,1)\bigr)\right)
\right].
\]

## Interpretation and bottleneck

The decomposition has three parts:

1. the original node-0 Rényi divergence;
2. a branch-selection correction involving `alpha_0`, `beta_0`, and the tilted branch reach `rho_{lambda,0}`;
3. a dependent new-data contribution given by a logarithm of a tilted expectation of conditional Rényi integrals.

The second term is the singleton two-node specialisation of the selection correction already recorded in R005 and in the Parallel-Hypothesis boundary work.

The third term is the key bottleneck for the present genuinely dependent problem. In general it is not an ordinary average of conditional Rényi divergences and it does not tensorise. It depends on the branch-selected tilted distribution of the old data.

The next mathematical question is to determine what can be said about this third term, and then how the exact identity iterates across further nodes and lifts from singleton pairs to composite classes and error converses.
