# Notation register

## User approved amendment: 16 September 2026

For the current selected converse and sample size calculation, use the notation agreed in the subsequent discussion. This amendment takes priority over the older table below for NEW work. The original manuscript itself is preserved unchanged, so historical references must be translated explicitly, not silently edited.

* Root: V_0; first child after the selected decision: V_1=Gamma(V_0,A_0).
* Z_t is the observed past BEFORE node t under zero based indexing. Z_0 is empty and Z_1=(X_0^n,A_0). Do not use Z_{t-1} for the past before node t in this indexing. The older manuscript's H_t corresponds to the new Z_t after translating its stages by one.
* The letter h is reserved for the prior article's log likelihood ratio, not a realised history.
* Composite classes: C_t^(0) is the null and C_t^(1) the alternative. Retain C; do not replace it with a different letter or return to a double subscript.
* X_0^n and X_1^m are the old and new blocks. Counts n and m are not product assumptions. N=n+m counts observations along the stated two node branch, not an expected stopping sample size.
* Tests phi_t take values in [0,1]. A_t is the realised binary action. Error definitions use expectations.
* Separate Type I budgets epsilon_0 and epsilon_1. L_t and U_t are bounds on optimal Type II error, not actual errors of an arbitrary test.
* In the singleton selected calculation, alpha_0 and beta_0 are ACTUAL errors under P_0 and Q_0 for one fixed first test. They cannot be replaced by independently optimised or composite worst case errors inside the selected law.
* Conditioning on A_0=1 alone leaves the old data random. Conditioning on Z_1=(x,1) fixes them. Never identify these two error definitions. R033 to R037 use the former and a test that may retain the old data.

The new note defines I_{lambda,0}(n) as D_lambda(Q_0||P_0) for the whole old block, T_{lambda,1}(n,m) as the previously established selected conditional Rényi term, c_lambda=(lambda-1)/lambda, and s_0=1-beta_0. Here lambda>1 because the task concerns the published converses. Superscript minus on information terms denotes the explicitly reversed divergence and its OWN tilt. The quantities a_lambda(n), b_lambda(n,m) and u_{lambda,t} are deterministic upper information limits, not new errors. B_Q denotes the expected indicator of any error when Q's correct path is (1,1). delta_path and delta_1 are error targets, not Monte Carlo failure probabilities.

Gaussian illustration only: R_k(gamma) has entry gamma^|i-j|; sigma_t is a standard deviation, Delta_t a mean gap, and J_t(k) the squared Gaussian separation divided by two. Its auxiliary c_1 is explicitly Delta_1^2/(2 sigma_1^2), distinct from c_lambda. No new symbol is to be used without first defining it.

## Historical manuscript notation retained for reference

The following table records the earlier manuscript and approximation vocabulary. Read it with the amendment above when extending the current research. It is not permission to reintroduce conflicting history symbols into new work.

| Symbol | Meaning |
| --- | --- |
| $T$, $V_t$, $\Gamma(v,a)$ | decision horizon, occupied node and tree child map |
| $X_t$, $A_t$ | observation block and selected binary edge |
| $H_t=(X_1,A_1,\ldots,X_t,A_t)$, $\mathcal F_t$ | historical observed history and its sigma field |
| $\mathcal H_{t-1}$ | historical history space, not a Hellinger integral |
| $\mathcal C_{t,i}(h)$ | historical conditional composite class for edge $i$ |
| $\vartheta(v)$, $\Theta_t$ | fixed node truth map and correct edge at the realised node |
| $\eta$, $\mathfrak E$ | environment and admissible environment class |
| $\boldsymbol\phi$, $\kappa_{\phi_t}$ | policy and its Bernoulli action kernel |
| $\alpha_t$, $\beta_t$ | local Type I and Type II errors |
| $\lambda$ | Rényi order; the initial approximation work used orders between zero and one |
| $H_\lambda(Q,P)$, $D_\lambda(Q\Vert P)$ | Hellinger integral and directed Rényi divergence |
| $G_t(h)$ | manuscript's backward Hellinger continuation |
| $E_t$, $E_{\le T}$, $\mathcal R_T$ | local error, any error event and worst case path risk |

## Earlier approximation additions

| Symbol | Meaning |
| --- | --- |
| $\mathsf H_\lambda^{\boldsymbol\phi}$ | scalar abbreviation for the full path Hellinger integral |
| $\mathsf H_{\lambda,t}^{\boldsymbol\phi}$ | corresponding prefix integral through stage $t$ |
| $\Delta_\lambda^{\boldsymbol\phi}$ | $1-\mathsf H_\lambda^{\boldsymbol\phi}$ for $0<\lambda<1$ |
| $z_{\lambda,t}(h)$ | local conditional Hellinger integral in historical notation |
| $J$ | model label drawn for mixture simulation, not a truth map; distinct from the explicitly defined Gaussian scalar J in the new note |
| $M^{\boldsymbol\phi}$ | equal mixture of the two controlled path laws |
| $\omega_t$ | posterior probability that $J=\mathbf Q$ given observed history |
| $w_\lambda$ | posterior weight $2u^\lambda(1-u)^{1-\lambda}$ |
| $C_{\lambda,t}$, $\mathcal A_\lambda^{\boldsymbol\phi}$ | predictable increment and its sum; never the action $A_t$ |
| $\mathcal B_{\lambda,t}$ | expected remaining sum of increments |
| $\nu_{\lambda,t}^{\boldsymbol\phi}$ | normalised tilted prefix law |
| $\widetilde R_{\lambda,t}$ | local tilted observation kernel |
| $\rho_{P,t},\rho_{Q,t},\rho_{\lambda,t}$ | local branch probabilities under the three stated laws |
| $P_t^{h,a},Q_t^{h,a}$ | historical current observation laws conditioned on a selected branch |
| $S_t$, $\Psi_t$ | a proposed sufficient state and its update, not a replacement for $V_t$ or $\Gamma$ |
| $W_t^\eta$ | fixed environment probability of any future error |
| $K$, $C_{\rm path}$ | earlier remaining gain bound constant and full trajectory cost; the new note explicitly uses K only for number of decisions |

Earlier approximation tolerances were epsilon_gap for relative gap tolerance, varepsilon for relative divergence tolerance and delta for algorithmic failure probability. They are not the local Type I budgets or the explicitly labelled delta_path in this task. Reserve eta for the environment.

Existing code uses `lam`, `horizon` and tuples of `(observation, action)` pairs and retains its original one based stages. It was not silently renamed by this task. All divergence functions take Q first and P second. The local path mass dictionaries store `(P mass, Q mass)` and are labelled as such.
