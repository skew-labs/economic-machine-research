# Economic Machine Research

**Fast Machines, Endogenous Losses: Strategy Evolution in Agent-Native Perpetual Markets**

SKEW Research · Working paper v0.1 · 9 October 2026

[Read the paper](paper.md) · [한국어 개요](overview.ko.md) ·
[Methods](methods/README.md) · [Engine source](https://github.com/skew-labs/economic-machine/tree/main/markets)

We study frozen-model strategy search, microsecond native execution and exact
on-chain accounting across Solana and Arbitrum. The central question is economic:
when an agent wins, who pays for that win, and does it beat an appropriate baseline?

| Finding | Observed result | Interpretation |
| --- | --- | --- |
| Native personalized decision | p50 5.447 µs; p99 7.837 µs | CPU-only; excludes model, network, signing and chain |
| 30 personalized devnet episodes | 23 positive; 4 beat control; summed excess −1,536.5 | Positive P&L does not establish baseline superiority |
| Common-window transfers | +1,095 makers; +942 controls; −4,245 demand; +2,208 fees | Sum 0; identifies who loses |
| 36 paired SBF matches | Candidate wins 23; total P&L −3,464 | Relative loss reduction is not absolute profitability |
| Two-chain lifecycle | Finalized reconciliation and zero residual account state | Controlled settlement proof, not external alpha |

![Loss incidence](figures/loss-incidence.png)

This is a research publication, not a runtime-log archive. Numerical tables are
curated with defined units and comparison windows; figures and accounting checks
are reproducible from those tables. Historical live journals and private provider
records are not distributed. See the paper's limitations and data-availability
section before interpreting the results.

```sh
python3 analysis/verify_results.py
# Optional: matplotlib is needed only to regenerate figures.
python3 analysis/make_figures.py
```

Offline program and native conformance tests live in the engine repository.
Neither analysis command calls a model, signs a transaction or connects a wallet.
The manuscript is an exploratory working paper and has not been peer reviewed.
