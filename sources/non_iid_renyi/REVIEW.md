# Computing and controlling Rényi divergence beyond iid data

Audit date: 24 September 2026.

This is the persistent repository edition of the literature audit requested by the user. The extended conversation report includes the same conclusions, mathematical translations, and a separate reading record. This source record preserves the findings, assumptions, primary references, and outstanding checks so later agents do not repeat the search. It extends the source basis of R001, R004, R027 to R044 and O019 to O021. No original manuscript or user working note is changed.

## Scope and conventions

The focus is classical Rényi divergence of complete dependent observation records, particularly orders lambda>1 and finite sample bounds. We distinguish exact identities, finite horizon upper bounds, asymptotic rates, and numerical estimates. An endpoint divergence is not the divergence of an entire retained transcript. A restricted variational supremum is not automatically an upper bound. No universal count only bound for unrestricted kernels is claimed.

The current project quantity is

\[
d_{\lambda,1}(n,m;\varphi_0)=\frac{1}{\lambda-1}\log\mathbb E_{\nu_{\lambda,0}^{(1)}}\left[\exp\left\{(\lambda-1)D_\lambda\!\left(Q_1(\cdot\mid X_0^n,A_0=1)\middle\|P_1(\cdot\mid X_0^n,A_0=1)\right)\right\}\right].
\]

The root laws are P_0^(tensor n),Q_0^(tensor n). The new block may be arbitrarily dependent. The first test is fixed. The scalar d is the older note's T; do not use d(x) for the pointwise conditional divergence in new work. Positive branch reach, measurable kernels, and the relevant absolute continuity and moment conditions must be stated.

## Main conclusions

1. Watanabe and Hayashi provide an especially direct finite length Markov testing reference, with computable spectral and boundary terms, not merely a limiting rate. See S05.
2. Adaptive Rényi filters permit conditional information costs that vary with the preceding reports, provided their cumulative path cost is bounded. This can be less conservative than separately maximising every step. See S12.
3. Positive operator and multiplicative drift methods provide a route for unbounded state spaces, but their transform domains and initial integrability conditions must be checked. See S08 and S09.
4. Risk sensitive variational formulas directly address the logarithmic exponential expectation at issue. They optimise an exponential moment together with a divergence penalty, not just a closest reference projection. See S15 and S16.
5. Hidden Markov rates, endpoint coupling bounds, and numerical divergence estimators are relevant but require careful translation. None automatically provides an upper bound on the complete selected observation divergence at finite n,m.

## 1. Exact chain rule and conditional divergence

Polyanskiy and Wu, Section 7.12, equations (7.77) and (7.78), give the exact tilted marginal chain rule. Their equation (7.79) recovers product additivity. This is the representation already derived in the project. The updated tilt must be the tilt of the whole current prefix, not a product of locally normalised tilts. Cai and Verdú study the conditional divergence and its optimisation on general alphabets. Bleuler, Lapidoth and Pfister explain why the term conditional Rényi divergence is ambiguous. [S01 to S04]

A useful project translation is to define two auxiliary laws with the same initial marginal nu_{lambda,0}^{(1)}, followed respectively by P_1 and Q_1. Their Rényi divergence is exactly d_{lambda,1}. These are not the actual selected testing laws: the construction isolates the future contribution as a path divergence with a common initial law. This permits applying a path divergence theorem after its conditional assumptions are verified.

The chain rule is an identity, not a finiteness theorem. Independent but nonidentical observations remain a product case and are already handled by product additivity. [S02]

## 2. Finite state Markov paths and finite length testing

Rached, Alajaji and Campbell treat Rényi divergence and entropy rates for finite alphabet Markov sources. Watanabe and Hayashi's Lemma 6.1 supplies finite length cumulant bounds with spectral and boundary terms; Section 9, especially Theorem 9.1, connects them to finite length simple hypothesis testing. Their support, finite state and ergodicity assumptions matter. Complexity described as constant in sequence length does not mean independent of state dimension or numerical precision. [S05, S06]

Li and Wang consider time varying Markov chains whose transition matrices converge to a primitive matrix. Their result is a rate theorem under that convergence assumption, not a general finite horizon statement for arbitrary varying transitions. [S07]

### Algebraic translation to this project

Suppose an observed finite state determines both future conditional laws. Let s(X_0^n) be its initial value. In this illustration, each new observation is the next state and the full sequence is retained. For transition probabilities p_j(t|s),q_j(t|s), define

\[
K_{\lambda,j}(s,t)=q_j(t\mid s)^\lambda p_j(t\mid s)^{1-\lambda},
\qquad
w_n(s)=\mathbb E_{\nu_{\lambda,0}^{(1)}}[\mathbf1_{\{s(X_0^n)=s\}}].
\]

Summing products of conditional likelihood factors yields the exact finite horizon identity

\[
e^{(\lambda-1)d_{\lambda,1}(n,m;\varphi_0)}=w_nK_{\lambda,1}\cdots K_{\lambda,m}\mathbf1.
\]

This is a mathematical translation of the established method, not a new theorem or an assumption that the unrestricted model is Markov. The matrices need not be identical. No independence of observations is used.

In the homogeneous case, suppose K_lambda has a strictly positive right eigenvector v_lambda with eigenvalue r_lambda>0. Write v_min and v_max for its minimum and maximum coordinates. Since v/v_max<=1<=v/v_min, nonnegativity gives

\[
r_\lambda^m\frac{w_nv_\lambda}{v_{\max}}
\leq w_nK_\lambda^m\mathbf1
\leq r_\lambda^m\frac{w_nv_\lambda}{v_{\min}}.
\]

Consequently,

\[
d_{\lambda,1}(n,m;\varphi_0)
\leq\frac{m\log r_\lambda}{\lambda-1}
+\frac{1}{\lambda-1}\log\frac{w_nv_\lambda}{v_{\min}}.
\]

This keeps a finite length initial correction instead of replacing the divergence by its rate. An irreducible finite nonnegative matrix supplies a positive Perron eigenvector. Support conditions must be checked. With k states, successive multiplication of known dense matrices costs order m k^2 arithmetic operations. State construction, w_n, entries and precision are additional costs. A history state can itself grow exponentially.

## 3. Positive operators and unbounded state spaces

Kontoyiannis and Meyn analyse exponential additive functionals of Markov paths. The 2003 work uses geometric ergodicity and bounded functionals, with multiplicative statements near the transform origin. The 2005 work develops stronger multiplicative regularity conditions, including DV3/DV3+, suitable for broader unbounded settings. [S08, S09]

A Rényi moment is an exponential moment of a path log likelihood ratio, so these weighted operators are directly relevant. The project backward recursion R039 is a finite horizon version of this viewpoint. A useful import must verify growth of the likelihood functional, transform domain, drift or domination inequalities, and integrability under the selected initial law. Ordinary mixing alone is not a guarantee at every order lambda>1.

## 4. Hidden Markov observations

Fuh and coauthors represent observed hidden Markov likelihoods through an augmented Markov construction and associated positive operator. Theorem 3.1 gives a divergence rate under C1 to C4; its order greater than one statement includes an additional positivity condition. Retain all the conditions together. [S10]

The hidden paths are summed before taking a Rényi power. In general one cannot exchange those operations, so a small hidden transition matrix does not automatically give a small exact observed divergence matrix. A rate needs a finite horizon evaluation or remainder to yield finite sample exclusion. Computing the joint hidden and observed divergence instead gives an upper bound by data processing, not equality for observed data.

## 5. Adaptive composition and cumulative budgets

Mironov's Proposition 1 gives additive adaptive Rényi composition from uniform conditional bounds. Transcript coordinates need not be independent. [S11]

Feldman and Zrnic's Theorem 3.1 allows the conditional costs to depend on the previous reports. A bound on their sum along paths controls the full transcript. Remark 3.2 explicitly includes a fixed pair; Theorem 4.3 treats a Rényi filter with stopping. The proof uses a compensated likelihood ratio moment supermartingale. A cumulative path condition is not merely an expected budget, nor a bound checked on only one realised path. [S12]

This potentially avoids incompatible separate worst cases at every step. For our d, apply the fixed pair argument to the auxiliary laws sharing nu_{lambda,0}^{(1)}, after verifying the cumulative condition for the future kernels. This is a proposed application, not a proved budget for unrestricted kernels.

Whitehouse and coauthors develop additional filters and time uniform accounting using martingale concentration, including approximate zCDP. Their privacy guarantees require translation and must not be identified with local Type I or Type II errors. [S13]

## 6. Concentration without independence

Esposito and Mondelli's Theorem 1, including equations (23) to (25), develops finite sample information based concentration and Hellinger moment bounds for dependent data. Hölder, Markov structure, hypercontractivity and strong data processing appear in the analysis. [S14]

This is relevant prior art for the project's higher conditional moment method. Its principal comparison is a joint law against the product of its marginals. Our comparison is between two specified testing laws. A common reference argument may connect them, but simply relabelling the hypotheses is invalid. Do not claim the base Hölder method as new.

## 7. Variational reference comparison and projection

Atar, Chowdhary and Dupuis's Theorem 2.1 gives an exact variational infimum for exponential functionals, involving both a reference moment and a Rényi penalty. Their R_alpha equals our D_alpha/alpha. [S15]

In the project's convention, for bounded measurable F, a law nu, lambda>1 and s>1, their equation (2.4) translates to

\[
\frac{1}{\lambda-1}\log\mathbb E_\nu e^{(\lambda-1)F}
=
\inf_\mu\frac{D_{s/(s-1)}(\nu\|\mu)+\log\mathbb E_\mu e^{s(\lambda-1)F}}{s(\lambda-1)}.
\]

Every reference law with finite relevant terms gives an upper bound. In the present application nu is the selected old tilt and F is the full conditional divergence. For unbounded F, verify the needed integrability or the source extension; do not silently invoke the bounded theorem. Restricting the reference family still gives an upper bound when the whole objective is evaluated. Minimising the mismatch divergence alone does not optimise it. The unrestricted optimiser depends on F, so the representation is not automatically computable.

Anantharam gives variational divergence characterisations and finite state stationary Markov rate extensions. At orders above one, the direction of a supremum representation must not be confused with an upper bound from a reference infimum. Atar, Budhiraja, Dupuis and Wu apply Rényi robustness methods to queueing models at the large deviation scale. [S16, S17]

R044 is therefore an instance of established risk sensitive reference comparison machinery, not a newly discovered general inequality. Its possible new use lies in an explicit reference family for the selected experiment.

## 8. Endpoint coupling and contraction

Altschuler and Chewi's Shifted Composition I supplies finite time Rényi comparison and regularity methods; Theorem 3.10 treats discretised Langevin dynamics and Remark 3.13 discusses finiteness thresholds. Appendix A of Shifted Composition III extends local error comparisons to Rényi divergence under regularity, cross regularity and stronger transport conditions. [S18, S19]

These predominantly bound final state distributions. The full retained block in our problem is a different object. Projecting it to the last state reduces divergence, so an endpoint upper bound is not an upper bound on the full transcript. A sufficient statistic argument or an explicitly changed observation model is needed.

Vandenbroucque, Esposito and Gastpar's 2026 preprint develops Rényi contraction for discrete channels at orders above one. A KL or total variation contraction factor must not be imported without an actual Rényi comparison. Bou-Rabee, Mitra and Wibisono provide a recent tail sensitive endpoint coupling lead; only its abstract was inspected here. [S20, S29]

## 9. Gaussian and numerical calculations

Finite Gaussian blocks can have arbitrary positive definite covariance, including correlated observations. For equal covariance Sigma, direct integration gives

\[
D_\lambda(\mathcal N(\mu_Q,\Sigma)\|\mathcal N(\mu_P,\Sigma))
=\frac{\lambda}{2}(\mu_Q-\mu_P)^{\mathsf T}\Sigma^{-1}(\mu_Q-\mu_P).
\]

For unequal covariance and lambda>1, the precision combination lambda Sigma_Q^(-1)+(1-lambda)Sigma_P^(-1) must be positive definite for the Gaussian integral to be finite. These are finite dimensional Gaussian calculations, not independence assumptions. S26 identifies Gaussian formulas and stationary process rates; its formula tables were not inspected. S18 also uses Gaussian comparisons.

Cérou, Del Moral and Guyader provide finite particle error bounds for Feynman–Kac normalising constants. Theorem 1.5 requires potential ratio and multistep transition comparisons; Theorem 5.1 extends to time variation. Applying it to a Rényi moment requires those conditions on the weighted model. Unbounded likelihood ratio weights can violate them. Particle number controls numerical accuracy and is not the data sample count. [S21]

Birrell and coauthors provide a general variational formula and neural estimation methods. Restricting a population supremum yields a lower value. Empirical estimates have additional sampling and optimisation errors and are not automatically an upper bound suitable for a converse. [S27]

## 10. Sequential background and limits

Jacod and Dzhaparidze, Spreij and Valkeila provide filtered experiment and Hellinger process frameworks, including randomised experiments. They are prior art for sequential information accumulation, not a verified universal finite n,m formula at orders above one. Han supplies general source asymptotic testing, Hayashi supplies adaptive simple channel discrimination, and Hayashi–Watanabe supply further finite length Markov coding applications. Their risk objects and assumptions differ. [S22 to S25, S28]

The existing Lei Yu monograph citation was traced to an author upload, but its Theorem 8 could not be reopened. Do not confuse that monograph with the different paper The Entropy Method in Large Deviation Theory. Use the checked Polyanskiy–Wu chain rule as the present foundation. [S01, S30]

An expectation over histories is compatible with finite sample analysis. The separate questions are finiteness, evaluability, computational error, and uniformity over first tests. A limiting rate or a numerical point estimate does not answer all four.

A justified upper information bound inserted into the existing converse gives necessary sample count exclusions. It does not make the first nonexcluded count sufficient. Matrix bounds with boundary terms and cumulative adaptive budgets are the first priorities; positive operator and full variational comparisons are the next routes for more general models.

## 11. References and inspection depth

[S01] Yury Polyanskiy and Yihong Wu (2024), Information Theory: From Coding to Learning, prepublication version 16 August 2024. https://people.lids.mit.edu/yp/homepage/data/itbook-export.pdf . Relevant text inspected: Section 7.12, equations (7.77) to (7.79), printed page 145. Some screenshot attempts failed. Exact chain rule, not its new discovery.

[S02] Tim van Erven and Peter Harremoës (2014), Rényi Divergence and Kullback–Leibler Divergence. IEEE Transactions on Information Theory 60(7), 3797–3820. DOI 10.1109/TIT.2014.2320500. https://arxiv.org/abs/1206.2459 . Primary record and existing project audit checked; no fresh complete proof review. Definitions, data processing, Theorem 28.

[S03] Changxiao Cai and Sergio Verdú (2019), Conditional Rényi Divergence Saddlepoint and the Maximization of α-Mutual Information. Entropy 21(10), 969. DOI 10.3390/e21100969. https://www.mdpi.com/1099-4300/21/10/969 . Primary definitions and main result descriptions inspected. General alphabet conditional optimisation, not an automatic bound for our selected pair.

[S04] Cédric Bleuler, Amos Lapidoth and Christoph Pfister (2020), Conditional Rényi Divergences and Horse Betting. Entropy 22(3), 316. DOI 10.3390/e22030316. https://doi.org/10.3390/e22030316 . Author abstract and metadata checked; fresh PMC full text access blocked. Warning about inequivalent definitions.

[S05] Shun Watanabe and Masahito Hayashi (2017), Finite-length Analysis on Tail Probability for Markov Chain and Application to Simple Hypothesis Testing. Annals of Applied Probability 27(2), 811–845. DOI 10.1214/16-AAP1216. https://arxiv.org/abs/1401.3801 . Version 2, 15 March 2015, inspected: Lemma 6.1, Section 9, Theorem 9.1. Finite length Markov moments and testing; no independent full proof review.

[S06] Ziad Rached, Fady Alajaji and L. Lorne Campbell (2001), Rényi's Divergence and Entropy Rates for Finite Alphabet Markov Sources. IEEE Transactions on Information Theory 47(4), 1553–1561. DOI 10.1109/18.923736. https://ieeexplore.ieee.org/document/923736 . Publisher abstract and metadata checked. Rate result; the explicit finite matrix translation above is not quoted as a numbered source theorem.

[S07] Wenxi Li and Zhongzhi Wang (2019), A Note on Rényi's Entropy Rate for Time-Inhomogeneous Markov Chains. Probability in the Engineering and Informational Sciences 33(4), 579–590. DOI 10.1017/S026996481800044X. https://doi.org/10.1017/S026996481800044X . Publisher abstract and metadata checked; online publication 5 December 2018. Requires convergence to a primitive matrix.

[S08] Ioannis Kontoyiannis and Sean P. Meyn (2003), Spectral Theory and Limit Theorems for Geometrically Ergodic Markov Processes. Annals of Applied Probability 13(1), 304–362. DOI 10.1214/aoap/1042765670. https://arxiv.org/abs/math/0209200 . Primary assumptions and spectral statements inspected. Transform domain restrictions matter.

[S09] Ioannis Kontoyiannis and Sean P. Meyn (2005), Large Deviations Asymptotics and the Spectral Theory of Multiplicatively Regular Markov Processes. Electronic Journal of Probability 10, paper 3, 61–123. DOI 10.1214/EJP.v10-231. https://arxiv.org/abs/math/0509310 . Primary DV3/DV3+ and Theorem 1.2 inspected. Unbounded state operator route with substantial conditions.

[S10] Cheng-Der Fuh, Su-Chi Fuh, Yuan-Chen Liu and Chuan-Ju Wang (2025), Rényi Divergence in Hidden Markov Models. Machine Learning 114, article 232. DOI 10.1007/s10994-025-06872-4. https://link.springer.com/article/10.1007/s10994-025-06872-4 . Primary full article: conditions C1 to C4 and Theorem 3.1 inspected. Observed hidden Markov rates require filtering construction and order restrictions.

[S11] Ilya Mironov (2017), Rényi Differential Privacy. IEEE Computer Security Foundations Symposium, 263–275. https://arxiv.org/abs/1702.07476 . Primary Proposition 1 inspected. Adaptive finite transcript composition from conditional bounds.

[S12] Vitaly Feldman and Tijana Zrnic (2021), Individual Privacy Accounting via a Rényi Filter. Advances in Neural Information Processing Systems 34. https://arxiv.org/abs/2008.11193 . Primary Theorem 3.1, proof, Remark 3.2 and Theorem 4.3 inspected. Cumulative path budget and fixed pair application.

[S13] Justin Whitehouse, Aaditya Ramdas, Ryan Rogers and Steven Wu (2023), Fully-Adaptive Composition in Differential Privacy. PMLR 202, 36990–37007. https://proceedings.mlr.press/v202/whitehouse23a.html . Official abstract and metadata checked, not full theorem review. Preprint uses Zhiwei Steven Wu. Further filters, odometers and approximate zCDP.

[S14] Amedeo Roberto Esposito and Marco Mondelli (2024), Concentration without Independence via Information Measures. IEEE Transactions on Information Theory 70(6), 3823–3839. DOI 10.1109/TIT.2024.3367767. https://arxiv.org/abs/2303.07245 . Primary Theorem 1 and equations (23) to (25) inspected; theorem page visually checked. Joint versus product comparison must not be confused with arbitrary testing laws.

[S15] Rami Atar, Kamaljit Chowdhary and Paul Dupuis (2015), Robust Bounds on Risk-Sensitive Functionals via Rényi Divergence. SIAM/ASA Journal on Uncertainty Quantification 3(1), 18–33. DOI 10.1137/130939730. https://arxiv.org/abs/1310.6391 . Primary Theorem 2.1, Corollary 2.4, normalisation and optimiser inspected. R_alpha=D_alpha/alpha.

[S16] Venkat Anantharam (2018), A Variational Characterization of Rényi Divergences. IEEE Transactions on Information Theory 64(11), 6979–6989. DOI 10.1109/TIT.2018.2861013. https://arxiv.org/abs/1701.07796 . Primary Theorem 1 and Section 7 extensions inspected; author's publication list checked. Supremum direction and normalisation matter.

[S17] Rami Atar, Amarjit Budhiraja, Paul Dupuis and Ruoyu Wu (2021), Robust Bounds and Optimization at the Large Deviations Scale for Queueing Models via Rényi Divergence. Annals of Applied Probability 31(3), 1061–1099. DOI 10.1214/20-AAP1613. https://arxiv.org/abs/2001.02110 . Primary abstract and publication record checked. Large deviation scale path robustness, not an automatic finite bound for our model.

[S18] Jason M. Altschuler and Sinho Chewi (2025), Shifted Composition I: Harnack and Reverse Transport Inequalities. IEEE Transactions on Information Theory 71(1), 90–113. DOI 10.1109/TIT.2024.3475290. https://arxiv.org/abs/2311.14520 . Primary shifted composition and Theorem 3.10 inspected; finiteness discussion checked. Endpoint laws, not full retained histories.

[S19] Jason M. Altschuler and Sinho Chewi (2026), Shifted Composition III: Local Error Framework for KL Divergence. Foundations of Computational Mathematics, online 11 June 2026. DOI 10.1007/s10208-026-09753-x. https://arxiv.org/abs/2412.17997 . Primary Appendix A, Theorems A.4 and A.5 inspected. Rényi extension has explicit stronger transport conditions.

[S20] Adrien Vandenbroucque, Amedeo Roberto Esposito and Michael Gastpar (2026), Contraction of Rényi Divergences for Discrete Channels: Properties and Applications. arXiv:2601.09328v1. https://arxiv.org/html/2601.09328v1 . Primary definitions, contraction results and applications inspected. No blanket transfer of other divergence contraction coefficients.

[S21] Frédéric Cérou, Pierre Del Moral and Arnaud Guyader (2011), A Nonasymptotic Theorem for Unnormalized Feynman–Kac Particle Models. Annales de l'Institut Henri Poincaré, Probabilités et Statistiques 47(3), 629–649. DOI 10.1214/10-AIHP358. https://www.numdam.org/item/10.1214/10-AIHP358.pdf . Primary normalising constant setup, Theorems 1.4/1.5 and time varying extension inspected. Potential and transition assumptions are essential.

[S22] Jean Jacod (1989), Filtered Statistical Models and Hellinger Processes. Stochastic Processes and their Applications 32(1), 3–45. DOI 10.1016/0304-4149(89)90052-5. https://doi.org/10.1016/0304-4149(89)90052-5 . Publisher record and previous project audit checked; no fresh full theorem review.

[S23] Kacha Dzhaparidze, Peter Spreij and Esko Valkeila (2002), Information Concepts in Filtered Experiments. Theory of Probability and Mathematical Statistics 67, 38–56. https://staff.fnwi.uva.nl/p.j.c.spreij/information-compressed.pdf . Scanned primary PDF: selected page visually inspected; author abstract and prior metadata checked. Not a complete theorem audit.

[S24] Te Sun Han (2000), Hypothesis Testing with the General Source. IEEE Transactions on Information Theory 46(7), 2415–2427. DOI 10.1109/18.887854. https://arxiv.org/abs/math/0004121 . Primary abstract and existing audit checked. General source asymptotic testing.

[S25] Masahito Hayashi (2009), Discrimination of Two Channels by Adaptive Methods and Its Application to Quantum System. IEEE Transactions on Information Theory 55(8), 3807–3820. DOI 10.1109/TIT.2009.2023726. https://arxiv.org/abs/0804.0686 . Primary abstract and prior equation level audit checked. Adaptive simple channel discrimination with one terminal decision.

[S26] M. Gil, Fady Alajaji and Tamás Linder (2013), Rényi Divergence Measures for Commonly Used Univariate Continuous Distributions. Information Sciences 249, 124–131. DOI 10.1016/j.ins.2013.06.018. https://doi.org/10.1016/j.ins.2013.06.018 . Publisher abstract and metadata checked; tables not inspected. Abstract also identifies multivariate Gaussian and stationary Gaussian process formulas.

[S27] Jeremiah Birrell, Paul Dupuis, Markos A. Katsoulakis, Luc Rey-Bellet and Jie Wang (2021), Variational Representations and Neural Network Estimation of Rényi Divergences. SIAM Journal on Mathematics of Data Science. DOI 10.1137/20M1368926. https://arxiv.org/abs/2007.03814 . Primary Theorem 3.1, Corollary 3.2 and consistency setup inspected. Restricted population supremum is a lower bound.

[S28] Masahito Hayashi and Shun Watanabe (2020), Finite-Length Analyses for Source and Channel Coding on Markov Chains. Entropy 22(4), 460. DOI 10.3390/e22040460. https://www.mdpi.com/1099-4300/22/4/460 . Primary abstract and metadata checked. Adjacent coding risk, not our testing risk.

[S29] Nawaf Bou-Rabee, Siddharth Mitra and Andre Wibisono (2026), Tail-Sensitive KL and Rényi Convergence of Unadjusted Hamiltonian Monte Carlo via One-Shot Couplings. arXiv:2601.09019. https://arxiv.org/abs/2601.09019 . Recent lead, primary abstract only. No theorem transfer asserted.

[S30] Lei Yu (2023), The Entropy Method. Author preprint monograph. DOI 10.13140/RG.2.2.26552.11527/1. https://www.researchgate.net/publication/372389516_The_Entropy_Method . Access limited lead: author metadata checked; the repository's Theorem 8 citation was not freshly verified. Distinct from arXiv:2210.13121.

## Audit limits

Selected primary theorem statements and assumptions were inspected, not every proof in full. Several publisher endpoints and screenshots failed. No third party full texts are mirrored. This literature task did not change production code, run new stochastic experiments or rerun prior regression tests. No novelty claim is made. Future work must consult this record and the ledger before another broad search.
