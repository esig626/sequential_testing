# Relation to `Parallel-Hypothesis`

## Research decision

The `Parallel-Hypothesis` project and the present `sequential_testing` project should remain separate.

They study related but genuinely different statistical problems.

`Parallel-Hypothesis` studies repeated statistical decisions made from the same realised dataset. A sample is generated once, an earlier test reports an answer, and later tests reuse the same data conditional on the answers already reported. The main difficulty is selection: earlier answers change the conditional law of the already observed sample.

The present project studies a different mechanism. At stage `t`, new data `X_t` are observed, a binary decision `A_t` selects one of two outgoing edges, and the chosen edge determines the next node and therefore the law of the future data. In general,

\[
X_{t+1}\sim R_{t+1}(\cdot\mid H_t),
\qquad
H_t=(X_1,A_1,\ldots,X_t,A_t).
\]

Thus an earlier decision does not merely reveal information about fixed data. It changes the future statistical experiment.

The two repositories should therefore not be merged. However, several structural ideas from `Parallel-Hypothesis` should be imported into the present project because they provide the correct language for path propagation, zero probability histories, local versus global performance, and Rényi corrections.

---

## 1. The main distinction

The same data problem has the schematic form

\[
X^n \longrightarrow A_1 \longrightarrow A_2 \longrightarrow \cdots,
\]

where every decision is a function of the same realised sample.

The present problem has the form

\[
X_1 \longrightarrow A_1 \longrightarrow X_2 \longrightarrow A_2
\longrightarrow X_3 \longrightarrow \cdots,
\]

with

\[
\mathcal L(X_{t+1}\mid H_t)
\]

depending on the path already taken.

This distinction is fundamental. In the same data setting, a complete policy can be represented as one Markov kernel from the original observation to the final answer vector. In the present setting, such a flattening is generally impossible because later observations have not yet been generated and their laws depend on previous decisions.

The present project is therefore better viewed as **sequential composite testing with controlled, history dependent statistical experiments**.

---

## 2. Positive reach and zero reach histories

One of the most useful lessons from `Parallel-Hypothesis` is that conditional quantities must only be used on histories that have positive probability under the law being considered.

If a history `h_t` is reached with probability zero, then an expression such as

\[
\mathbb P(A_{t+1}=1\mid H_t=h_t)
\]

is not an intrinsic quantity of the model. One may choose a conditional probability version there, but that value is arbitrary and must not enter a theorem as though it were determined by the process.

The same rule should be adopted here.

For a policy `\boldsymbol\phi` and environment `\eta`, define the reach probability, in the discrete history case, by

\[
r_{\eta}^{\boldsymbol\phi}(h_t)
:=
\mathbb P_{\eta}^{\boldsymbol\phi}(H_t=h_t).
\]

Any conditional statement at `h_t` should explicitly require

\[
r_{\eta}^{\boldsymbol\phi}(h_t)>0.
\]

When possible, unnormalised path masses or flows should be preferred to ratios because they remain meaningful at zero reach histories.

This convention should be fixed from the beginning and never relaxed later for convenience.

---

## 3. Local error guarantees do not determine global path behaviour

`Parallel-Hypothesis` contains an explicit construction showing that two sequential policies can have the same nominal Type I and Type II errors at every node while inducing different complete path laws.

The conceptual lesson carries over directly:

\[
\text{local Type I and Type II errors}
\quad\not\Rightarrow\quad
\text{global path law}.
\]

In the present problem the gap is potentially larger, because the decision at one node also changes the law of the future observations.

Therefore quantities such as

\[
\alpha_t(\phi_t\mid h),
\qquad
\beta_t(\phi_t\mid h)
\]

cannot by themselves determine

\[
\mathbb P_{\eta}^{\boldsymbol\phi}(A_{1:T}=a_{1:T})
\]

or

\[
\mathbb P_{\eta}^{\boldsymbol\phi}
\left(\bigcup_{t=1}^T\{A_t\neq\Theta_t\}\right).
\]

The complete sequential problem therefore requires pathwise information in addition to local testing guarantees.

A useful early theorem in the present project should establish this insufficiency explicitly for the new data setting.

---

## 4. Rectangular versus coupled uncertainty

This is probably the most important structural lesson to import.

The current formulation allows conditional kernels satisfying

\[
R_t(\cdot\mid h_{t-1})
\in
\mathcal C_{t,\vartheta(v_t(h_{t-1}))}(h_{t-1}).
\]

This notation hides two very different classes of models.

### 4.1 Rectangular environments

In a rectangular model, the admissible conditional law at each stage and history can be selected independently of the choices made at other histories, subject only to local membership constraints.

Write the corresponding environment class as

\[
\mathfrak E_{\mathrm{rect}}.
\]

This is the natural setting for exact backward minimax recursion because local worst case choices can be pasted together across disjoint subtrees.

### 4.2 Coupled environments

In a coupled model, one common latent parameter, physical state, stochastic process, or model choice determines the kernels across multiple stages and histories simultaneously.

For example,

\[
\theta\in\Theta,
\qquad
R_t=R_t^{\theta},
\]

so that nature cannot independently choose the worst kernel at each node.

Write this class as

\[
\mathfrak E_{\mathrm{coup}}.
\]

In this setting, a supremum over environments generally cannot be moved inside a backward recursion. The same global environment must remain consistent across the whole path.

This distinction should be added explicitly to the main formulation before any minimax theorem is proved.

---

## 5. Backward recursion as the natural propagation mechanism

`Parallel-Hypothesis` already showed that path events are naturally propagated backwards through a binary tree.

The present project has the same architecture, but the local update now includes the observation kernel itself.

For two systems of conditional laws `\mathbf P` and `\mathbf Q`, and a common policy `\boldsymbol\phi`, the current formulation introduces

\[
G_{T+1}(h_T)=1
\]

and

\[
\begin{aligned}
G_t(h_{t-1})
=
\int
&q_t(x_t\mid h_{t-1})^{\lambda}
 p_t(x_t\mid h_{t-1})^{1-\lambda}
\\
&\times
\sum_{a_t\in\{0,1\}}
\kappa_{\phi_t}(a_t\mid h_{t-1},x_t)
G_{t+1}(h_{t-1},x_t,a_t)
\,dx_t.
\end{aligned}
\]

Then

\[
H_{\lambda}
\left(
\mathbb P_{\mathbf Q}^{\boldsymbol\phi},
\mathbb P_{\mathbf P}^{\boldsymbol\phi}
\right)
=
G_1(\varnothing).
\]

This is the natural replacement for ordinary tensorisation.

In a rectangular model, this recursion is likely to interact naturally with minimax optimisation. In a coupled model, the environment label must remain outside the recursion until the end unless additional structure justifies otherwise.

---

## 6. The Rényi selection correction idea should survive

A central result in `Parallel-Hypothesis` is that, along a realised same data path, the Rényi divergence between selected laws changes by an exact correction involving three quantities:

\[
\rho_{P,t},
\qquad
\rho_{Q,t},
\qquad
\rho_{\lambda,t},
\]

where the third term is a branch probability under the Rényi tilted law.

This yields identities of the schematic form

\[
D_{\lambda}^{(t)}
=
D_{\lambda}^{(t-1)}
+
\text{selection correction}.
\]

The exact formula from the same data problem should not be copied into the present setting because the present model generates new observations at every stage.

However, the three measure structure is likely to remain important.

For fixed conditional laws `P_t` and `Q_t`, define the local tilted kernel formally by

\[
\widetilde R_{\lambda,t}(dx_t\mid h_{t-1})
\propto
q_t(x_t\mid h_{t-1})^{\lambda}
 p_t(x_t\mid h_{t-1})^{1-\lambda}
\,dx_t.
\]

The effect of a decision may then be expressible through three branch probabilities:

\[
P_t(A_t=a\mid h),
\qquad
Q_t(A_t=a\mid h),
\qquad
\widetilde R_{\lambda,t}(A_t=a\mid h).
\]

This suggests that the dependent new data problem may admit a decomposition of the form

\[
\boxed{
\text{previous Rényi information}
+
\text{new conditional Rényi information}
+
\text{branch selection correction}
}
\]

rather than the same data formula containing only the selection correction.

This is one of the main mathematical directions to investigate.

---

## 7. Ideas that should not be imported directly

Several old constructions are specific to the same data setting and should remain in `Parallel-Hypothesis`.

### 7.1 Same data flattening

When all stages reuse one observation, the whole procedure can be represented as a single kernel

\[
K^{\Pi}(a\mid x).
\]

This does not extend to the present setting because future data are generated only after earlier actions have been taken.

### 7.2 Auxiliary root test compression

In the same data composite problem, products such as

\[
h_n=\varphi_n^0\psi_n
\]

remain ordinary tests on the original root sample. This can preserve root tensorisation.

There is no analogous reduction in general when the second test observes genuinely new data `X_2` whose law depends on the first decision.

### 7.3 Neyman Pearson nesting

The exact singleton same data identities rely on the fact that tests of one fixed pair of laws can be ordered by a common likelihood ratio.

That is a benchmark special case, not a foundation for the present composite sequential theory.

---

## 8. The same data model as a boundary case of the new theory

The most useful relationship between the two projects is not that one should replace the other, but that the old problem should emerge as a limiting special case of the new one.

Conceptually, the new theory should contain two important reductions.

### Independent stage reduction

If

\[
R_t(\cdot\mid h_{t-1})=R(\cdot)
\]

for every stage and history, then the backward Hellinger recursion should reduce to ordinary tensorisation.

### Same data reduction

If no genuinely new observation is generated and later tests act only on the stored original data, or equivalently if the later observation kernel deterministically reproduces the existing data, then the general recursion should reduce to the same data selection structure developed in `Parallel-Hypothesis`.

The desired architecture is therefore

\[
\begin{array}{ccc}
&\text{general history dependent sequential theory}&\\[4pt]
\swarrow&&\searrow\\[-2pt]
\text{independent stages}
&&
\text{same data reuse}.
\end{array}
\]

A satisfactory theory should recover both special cases exactly.

---

## 9. Immediate consequences for `sequential_testing`

Before proving new theorems, the main formulation should be strengthened in three ways.

First, positive reach should be treated explicitly whenever conditional laws or local errors are evaluated at a realised history.

Second, the admissible environment class should be split into rectangular and coupled versions. The minimax order of optimisation must then be handled differently in the two cases.

Third, the Rényi analysis should search for a local tilted conditional kernel and an exact decomposition separating new information from branch selection.

A useful first mathematical target is therefore:

> For a fixed history of positive reach and two admissible conditional systems `\mathbf P` and `\mathbf Q`, derive the exact one step relation between the Rényi quantity before observing `X_t`, the conditional Rényi information supplied by `X_t`, and the branch selected by `A_t`.

Only after that one step identity is exact should we attempt pathwise telescoping, minimax optimisation, or dynamic programming.

---

## Working principle

`Parallel-Hypothesis` should remain a separate same data project.

The present project should reuse its structural lessons, especially:

1. positive reach discipline;
2. pathwise rather than merely local performance;
3. rectangular versus coupled uncertainty;
4. backward propagation;
5. Rényi tilted branch probabilities;
6. exact reduction checks against the same data case.

The new theory should not be built by extending the old formula mechanically. It should be built so that the old formula reappears automatically when genuinely new observations are removed from the model.
