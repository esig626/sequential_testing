# Sequential composite hypothesis testing

A research workspace for new observations on decision trees, where each statistical decision can change the law of future data.

The model and fixed notation are in [sequential_testing.tex](manuscript/sequential_testing.tex). The [relation to Parallel-Hypothesis](manuscript/RELATION_TO_PARALLEL_HYPOTHESIS.md) explains which ideas transfer from the separate same data project. Both original scientific files are preserved unchanged by the September 2026 workspace recovery.

## Start here

Read [AGENTS.md](AGENTS.md), the mandatory [research ledger](docs/RESEARCH_LEDGER.md), [CURRENT_STATUS.md](CURRENT_STATUS.md), and the [Rényi approximation plan](docs/RENYI_APPROXIMATION_PLAN.md) before starting scientific work. The ledger is the persistent index of results, failures, counterexamples, attempted methods and open problems, and exists specifically to prevent duplicated research. The first executable brief is [Task 01](prompts/01_controlled_renyi_foundations.md).

The approximation project evaluates the manuscript's induced path laws under a fixed common policy. It preserves the order lambda and the direction D_lambda(Q||P). Independence without identical distribution still gives additivity; action dependent conditional laws are the substantive target.

The current work derives controlled predictable gap identities, connects them to the existing backward quantity G_t, and retains a rare action counterexample to a uniform variance bound. A literature audit now also fixes the boundary with active hypothesis testing and controlled sensing: action dependent observations, composite controlled sensing, and controlled Markovian observations are established ingredients and must not be claimed as novel on their own. No general efficient approximation theorem or optimal policy theorem is claimed.

## Research materials

| Location | Contents |
| --- | --- |
| [Research ledger](docs/RESEARCH_LEDGER.md) | Mandatory do not duplicate index of results, failures, methods, literature boundaries and open problems |
| [Xing and controlled testing literature audit](notes/2026-09-16_xing_2025_and_controlled_testing_literature_audit.md) | General information functions, reusable ideas, closest controlled sensing results and novelty boundary |
| [Research plan](docs/RENYI_APPROXIMATION_PLAN.md) | Scope, model specific routes, accuracy, cost and stages |
| [Working derivations](notes/2026-09-16_controlled_renyi_identities.md) | Prefix accumulation, branch selection, estimator and variance algebra |
| [Notation](docs/NOTATION.md) | Existing symbols and carefully separated additions |
| [Claims register](docs/CLAIMS.md) | Current claim status; the ledger additionally preserves research history and failed routes |
| [Integration record](docs/INTEGRATION.md) | Files read, preserved hashes and changes from the earlier plan |
| `src/` and `tests/` | Small finite controlled reference calculations |
| `experiments/` and `results/` | Experiment specification, validation and checkpoint |
| `sources/` | Article source records and bibliography, including SS-2025-0042 |

## Run the reference checks

Only the Python standard library is required. From the repository root:

```sh
python -m unittest discover -s tests -v
```

The initial suite has 30 passing local test methods. It includes deterministic formula checks and seeded checks that a sampled trajectory's estimator agrees with enumeration. It is not a stochastic performance study or a remote CI result. Enumeration is exponential and ordinary floating point is unsuitable for extreme numerical regimes.

## Article sources

The original approximation article is Anand, Benford and Guo, arXiv:2607.27088v1. See its [source record](sources/2607.27088/SOURCE.md).

The sequential testing literature audit begins from Yiming Xing, *Sequential Multiple Testing of Multiple Composite Hypotheses: an Asymptotic Optimality Theory with General Information Functions*, SS-2025-0042. See its [source record](sources/SS-2025-0042/SOURCE.md).

The source records link to the full external articles. Third party article bytes are not mirrored in this repository.

No project wide software or manuscript licence has been chosen on the owner's behalf.
