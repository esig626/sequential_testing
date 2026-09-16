# Conditional Rényi chain rule and dependent-testing source record

Read / checked on 16 September 2026.

## Core exact identity

1. Yury Polyanskiy and Yihong Wu, *Information Theory: From Coding to Learning*, prepublication version dated 16 August 2024.
   - Section 7.12 defines the common-input conditional Rényi divergence.
   - Eq. (7.77) gives the exact Rényi chain rule with a Rényi-tilted marginal.
   - Eq. (7.79) shows product tensorisation as a special case.
   - The text explicitly notes additive bounds for non-product distributions.
   - Source: https://people.lids.mit.edu/yp/homepage/data/itbook-export.pdf

2. Changxiao Cai and Sergio Verdú, “Conditional Rényi Divergence Saddlepoint and the Maximization of α-Mutual Information,” *Entropy* 21(10):969, 2019.
   - DOI: 10.3390/e21100969
   - Source: https://doi.org/10.3390/e21100969

3. Cédric Bleuler, Amos Lapidoth and Christoph Pfister, “Conditional Rényi Divergences and Horse Betting,” *Entropy* 22(3):316, 2020.
   - DOI: 10.3390/e22030316
   - Important terminology warning: several inequivalent conditional Rényi divergences coexist. The repository uses the common-input / joint-law definition for R026.

4. Lei Yu, *The Entropy Method*, 2023 preprint monograph.
   - Theorem 8: Full Chain Rule for Rényi Divergences for transition measures.
   - Used as an explicit multistage reference; the core two-variable identity is already covered by Polyanskiy and Wu.

## Sequential / adaptive testing neighbours

5. Masahito Hayashi, “Discrimination of Two Channels by Adaptive Methods and Its Application to Quantum System,” *IEEE Transactions on Information Theory* 55(8):3807–3820, 2009.
   - DOI: 10.1109/TIT.2009.2023726
   - arXiv:0804.0686
   - Randomised `[0,1]`-valued tests are explicit.
   - Adaptive observation selection is allowed.
   - Rényi/Hellinger-transform-type information is accumulated along the adaptive process.
   - Simple channel hypotheses and asymptotic exponents; not the present nodewise finite-sample composite propagation problem.

6. Bjarne Bergh, Nilanjana Datta and Robert Salzmann, “Composite Classical and Quantum Channel Discrimination,” arXiv:2303.02016v2, revised 16 September 2025.
   - Composite binary channel hypotheses and adaptive strategies.
   - Samples need not be identical, but independence is still required.
   - The paper explicitly states that it does not address non-independent states.
   - For classical non-convex composite hypotheses, no general entropic expression for the optimal adaptive rate is known in the paper.

7. Te Sun Han, “Hypothesis Testing with the General Source,” *IEEE Transactions on Information Theory* 46(7):2415–2427, 2000.
   - DOI: 10.1109/18.887854
   - arXiv:math/0004121
   - General nonstationary/nonergodic simple sources via information-spectrum methods.

## Filtered Hellinger / information process background

8. Jean Jacod, “Filtered statistical models and Hellinger processes,” *Stochastic Processes and their Applications* 32(1):3–45, 1989.
   - DOI: 10.1016/0304-4149(89)90052-5
   - Hellinger processes for filtered statistical experiments.

9. Kacha Dzhaparidze, Peter Spreij and Esko Valkeila, “Information concepts in filtered experiments,” *Theory of Probability and Mathematical Statistics* 67:38–56, 2002.
   - Randomized filtered experiments, generalized Hellinger processes and Hellinger integrals.

10. Eitan Greenshtein and Erik Torgersen, “Statistical information and expected number of observations for sequential experiments,” *Journal of Statistical Planning and Inference* 59(2):229–240, 1997.
    - DOI: 10.1016/S0378-3758(96)00114-0
    - Relates Hellinger transforms to expected stopping sample size in iid sequential experiments.

## Adaptive Rényi composition analogue

11. Ilya Mironov, “Rényi Differential Privacy,” *IEEE Computer Security Foundations Symposium*, 2017, pp. 263–275.
    - arXiv:1702.07476
    - Useful analogue for adaptive sequential composition from uniform conditional Rényi bounds, especially for order greater than one.

## Audit conclusion

The logarithmic tilted conditional term in R026 is established conditional Rényi divergence, and the exact dependent chain rule is known. No direct theorem was located for the repository’s full finite-sample problem in which each randomised local hypothesis decision also selects the next dependent composite experiment and the objective is propagation of nodewise Type I / Type II errors into global path error.
