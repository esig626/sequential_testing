# Sequential composite hypothesis testing

A research workspace for new observations on decision trees, where each statistical decision can change the law of future data.

The model and fixed notation are in [sequential_testing.tex](manuscript/sequential_testing.tex). The [relation to Parallel-Hypothesis](manuscript/RELATION_TO_PARALLEL_HYPOTHESIS.md) explains which ideas transfer from the separate same data project. Both original scientific files are preserved unchanged by the September 2026 workspace recovery.

## Start here

Read [AGENTS.md](AGENTS.md), [CURRENT_STATUS.md](CURRENT_STATUS.md), and the [Rényi approximation plan](docs/RENYI_APPROXIMATION_PLAN.md). The first executable brief is [Task 01](prompts/01_controlled_renyi_foundations.md).

The approximation project evaluates the manuscript's induced path laws under a fixed common policy. It preserves the order lambda and the direction D_lambda(Q||P). Independence without identical distribution still gives additivity; action dependent conditional laws are the substantive target.

The current work derives controlled predictable gap identities, connects them to the existing backward quantity G_t, and retains a rare action counterexample to a uniform variance bound. No general efficient approximation theorem or optimal policy theorem is claimed.

## Research materials

| Location | Contents |
| --- | --- |
| [Research plan](docs/RENYI_APPROXIMATION_PLAN.md) | Scope, model specific routes, accuracy, cost and stages |
| [Working derivations](notes/2026-09-16_controlled_renyi_identities.md) | Prefix accumulation, branch selection, estimator and variance algebra |
| [Notation](docs/NOTATION.md) | Existing symbols and carefully separated additions |
| [Claims register](docs/CLAIMS.md) | Established facts, local derivations, obstructions and open tasks |
| [Integration record](docs/INTEGRATION.md) | Files read, preserved hashes and changes from the earlier plan |
| `src/` and `tests/` | Small finite controlled reference calculations |
| `experiments/` and `results/` | Experiment specification, validation and checkpoint |
| `sources/` | Article record, PDF shortcut and bibliography |

## Run the reference checks

Only the Python standard library is required. From the repository root:

```sh
python -m unittest discover -s tests -v
```

The initial suite has 30 passing local test methods. It includes deterministic formula checks and seeded checks that a sampled trajectory's estimator agrees with enumeration. It is not a stochastic performance study or a remote CI result. Enumeration is exponential and ordinary floating point is unsuitable for extreme numerical regimes.

## Article source

The motivating article is Anand, Benford and Guo, arXiv:2607.27088v1. See its [source record](sources/2607.27088/SOURCE.md). The versioned HTML and author PDF were read. The record and shortcut link to the full article, but no article bytes are mirrored: the displayed arXiv licence does not establish permission to republish the complete text in this public repository.

No project wide software or manuscript licence has been chosen on the owner's behalf.
