# Source for the selected converse calculation

Recorded: 16 September 2026.

Authors: Elías Vera-Sigüenza and Amedeo Roberto Esposito.
Title: *Finite Sample Bounds for Composite Hypothesis Testing*.
Version used: arXiv:2608.28068v1, dated 28 August 2026, supplied by the user as `Finite Sample Bounds for Composite Hypothesis Testing.pdf`.
Version record: https://arxiv.org/abs/2608.28068v1

The online record was checked on 16 September 2026 and also lists version 2 dated 31 August 2026. The present calculation uses the uploaded version 1, not an unannounced replacement by version 2. No journal publication status was independently verified in this task.

SHA256 of the uploaded PDF actually read:
`c906e6232ac3e525c4f50a335dca535d82f8b76cbcdc768f7f7526b4b1f8e81d`.

The checksum identifies the consulted upload. The PDF bytes are not mirrored by this task. The bibliography is `references.bib` in this directory.

## Reading depth and imported results

The definitions and Theorem 1 on printed page 5, its proof in Appendix A-A on printed page 17, and the numerical appendix equation (48) on printed page 32 were inspected directly. Relevant PDF pages were rendered to check notation. This is source reading for the current calculation, not an independent proof review of the complete article.

For lambda>1, write c_lambda=(lambda-1)/lambda. Theorem 1, equation (4), supplies the converse based on D_lambda(Q||P):

$$
\beta\geq[1-\varepsilon^{c_\lambda}\exp\{c_\lambda D_\lambda(Q\Vert P)\}]_+.
$$

The paper optimises this over orders and, in the composite product setting, over pairs in the classes. In Appendix A-A, the inspected derivation uses change of measure and Hölder's inequality. These ingredients apply to a whole dependent record regarded as one observation. Only the replacement of the joint divergence by n times the single observation divergence requires a product structure.

Equation (48) supplies the companion converse in the opposite direction:

$$
\beta\geq (1-\varepsilon)^{\lambda/(\lambda-1)}
\exp\{-D_\lambda(P\Vert Q)\}.
$$

This direction must use its own tilted measure after selection. The source's original minimax and expectation conventions are preserved.

## Contribution to this repository

This source supports solved base case SB001 and R025. It is an input to R033 to R037, not a result rediscovered by the new branch. The current contribution is substitution of the already recorded selected Rényi expression, conversion to a specified path error, and inversion under explicit information growth limits.

The source alone does not establish our selected path sample counts, a converse for arbitrary tree truth patterns, or a necessary AND sufficient sample complexity under arbitrary dependence. Those are separate claims. The current note derives necessary conditions only.

Before further research, consult `docs/RESEARCH_LEDGER.md`, particularly SB001, R026 to R029, R033 to R037, and F019 to F021. Do not search again for the basic single node converse unless verifying a specific version or changed hypothesis.
