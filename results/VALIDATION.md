# Initial validation

Date: 16 September 2026. Environment: local execution container, Python 3.13.5.

Command: `python -m unittest discover -s tests -v`.

Result: **30 test methods passed**, with no failures or errors. Several tests contain multiple parameter subcases. These are finite numerical checks, including path enumeration and seeded checks of individual sampled trajectory values. They are not a stochastic performance study, independent mathematical review, or a remote GitHub Actions result.

## Coverage

The suite checks the Q then P orientation; independent nonidentical observations; path normalisation; the manuscript's backward recursion; common policy cancellation with continuing control of future data; final action invariance; deterministic action support; predictable means, remaining gains and the conditional second moment bound; the rare action failure and exact integration of that example; prefix tilting; randomised branch selection; same data reuse; action projection; zero reach under one or both models; a sufficient state recursion; equality; sampler consistency and its support restriction; higher order support orientation; invalid inputs and horizons; coherent versus rectangular parameters; fixed truth labels across histories at one node; and the two logarithmic error conversions.

## Tested file provenance

| File | SHA256 |
| --- | --- |
| `src/__init__.py` | `4b887b10d121fad3f8f359cac014147c63d25342562cc3b90a54080251c9c667` |
| `src/controlled_renyi.py` | `0104f0860ede4d90f333590f6069b750d232b61a24c8c64b96594b39d1f31a95` |
| `tests/test_controlled_renyi.py` | `c4c9aa8bba9a21dd86853c2515c814e48404fb989bc311cfacc7c02ae75c77c1` |

All calculations use ordinary floating point. Full path enumeration is exponential and is deliberately a small model reference. The code does not implement a generally stable large scale approximation method or prove a uniform dependent variance bound.

The original scientific files were not edited. Their original Git blob identifiers are recorded in `docs/INTEGRATION.md` and `results/checkpoint.json`. Publication should verify them against the final remote tree.
