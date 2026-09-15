# Notation register

The notation table in `sequential_testing.tex` is authoritative. This register adds only what the approximation work needs.

## Existing notation retained

| Symbol | Meaning |
| --- | --- |
| $T$, $V_t$, $\Gamma(v,a)$ | decision horizon, occupied node and tree child map |
| $X_t$, $A_t$ | observation block and selected binary edge |
| $H_t=(X_1,A_1,\ldots,X_t,A_t)$, $\mathcal F_t$ | observed history and its sigma field |
| $\mathcal H_{t-1}$ | history space, not a Hellinger integral |
| $\mathcal C_{t,i}(h)$ | conditional composite class for edge $i$ |
| $\vartheta(v)$, $\Theta_t$ | fixed node truth map and correct edge at the realised node |
| $\eta$, $\mathfrak E$ | environment and admissible environment class |
| $\boldsymbol\phi$, $\kappa_{\phi_t}$ | policy and its Bernoulli action kernel |
| $\alpha_t$, $\beta_t$ | local Type I and Type II errors |
| $\lambda$ | Rényi order; initially strictly between zero and one |
| $H_\lambda(Q,P)$, $D_\lambda(Q\Vert P)$ | Hellinger integral and directed Rényi divergence |
| $G_t(h)$ | manuscript's backward Hellinger continuation |
| $E_t$, $E_{\le T}$, $\mathcal R_T$ | local error, any error event and worst case path risk |

## Additions

| Symbol | Meaning |
| --- | --- |
| $\mathsf H_\lambda^{\boldsymbol\phi}$ | scalar abbreviation for the full path Hellinger integral |
| $\mathsf H_{\lambda,t}^{\boldsymbol\phi}$ | corresponding prefix integral through stage $t$ |
| $\Delta_\lambda^{\boldsymbol\phi}$ | $1-\mathsf H_\lambda^{\boldsymbol\phi}$ for $0<\lambda<1$ |
| $z_{\lambda,t}(h)$ | local conditional Hellinger integral |
| $J$ | model label drawn for mixture simulation, not a truth map |
| $M^{\boldsymbol\phi}$ | equal mixture of the two controlled path laws |
| $\omega_t$ | posterior probability that $J=\mathbf Q$ given observed history |
| $w_\lambda$ | posterior weight $2u^\lambda(1-u)^{1-\lambda}$ |
| $C_{\lambda,t}$, $\mathcal A_\lambda^{\boldsymbol\phi}$ | predictable increment and its sum; never the action $A_t$ |
| $\mathcal B_{\lambda,t}$ | expected remaining sum of increments |
| $\nu_{\lambda,t}^{\boldsymbol\phi}$ | normalised tilted prefix law |
| $\widetilde R_{\lambda,t}$ | local tilted observation kernel |
| $\rho_{P,t},\rho_{Q,t},\rho_{\lambda,t}$ | local branch probabilities under the three stated laws |
| $P_t^{h,a},Q_t^{h,a}$ | current observation laws conditioned on a selected branch |
| $S_t$, $\Psi_t$ | a proposed sufficient state and its update, not a replacement for $V_t$ or $\Gamma$ |
| $W_t^\eta$ | fixed environment probability of any future error |
| $K$, $C_{\rm path}$ | remaining gain bound constant and full trajectory cost |

Use $\epsilon_{\rm gap}$ for relative gap tolerance, $\varepsilon$ for the requested relative divergence tolerance, and $\delta$ for algorithmic failure probability. Reserve $\eta$ exclusively for the manuscript's environment. These quantities are not the local testing errors or Type I constraints.

Code uses `lam`, `horizon` and tuples of `(observation, action)` pairs. Such a tuple is a storage representation of the original observed history, not a different information structure. All divergence functions take the Q argument first and P second. The local dictionaries storing path masses explicitly store `(P mass, Q mass)` and are labelled as such.
