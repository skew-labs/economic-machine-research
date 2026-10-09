# Methods and table dictionary

This is a descriptive systems study. Rows are correlated observations, not
independently sampled customers. The publication transforms archived measurements
into defined numerical tables rather than distributing operational logs.

| Table | Population and units | Transformation |
| --- | --- | --- |
| `personalized_episodes.csv` | 30 devnet episodes; test accounting units/lots | Select metrics; omit display names, operator roles, slots, hashes and receipt payloads |
| `paired_matches.csv` | 36 SBF matches; integer test P&L/fees | Keep regime/seed/swap; aggregate 30 opponents; check all participant P&L plus fees |
| `loss_incidence.csv` | One common finalized window | Aggregate experimental makers, controls, demand and exchange |
| `native_latency.csv` | Warmed decision/boundary/replay/storage; nanoseconds | Observed quantiles with explicit timing boundary |
| `solana_cu.csv` | 11 matched paths; consumed CU | Fee-corrected baseline, undeployed v7, SDK-compatible Phoenix rebuild |
| `arbitrum_gas.csv` | Matched Anvil paths; receipt gas | Immediate/cumulative same-safety baselines; not Nitro total fee |
| `shocks.csv` | 30 fixed profiles × 7 independent price branches | Liquidation counts, compensation, outside capital and flat-account exit |
| `settlement_summary.json` | Three closed sessions; raw token/wei fields | Explicit aggregate field projection from finalized reconciliations |

## Personalized episodes

Six evaluated Muse candidates cross with five styles. Six existing experimental
maker roles each run five settings in sequence; two existing makers retain the
original strategy. A setting has a ninety-second active interval followed by
cleanup. Original limits, signers, sessions and journals are preserved. A
flat/no-pending handoff precedes installation and restoration.

P&L includes funding and trading/cleanup fees in test units. The control is the
mean of two unchanged makers at the same finalized endpoints. Different inventory
limits, queue assignments, sequential timing and selection effects prevent a
causal or risk-normalized interpretation. Observed position changes are a snapshot
lower bound, not complete maker fills. A quote update proves quoting, not a fill.

The common incidence window spans slots 508532341–508534842 and includes some
original-strategy time around episodes. Its endpoint changes conserve; independently
timed episode totals cannot replace that window.

## Paired competition

Thirty opponents cover inventory making, trend following, mean reversion,
imbalance reading, liquidity defense and regime switching crossed with five risk
styles. Candidate and baseline add two pilots. All execute the actual v6 ELF in
LiteSVM. Six regimes, three seeds and two seat assignments produce thirty-six
sixty-step matches. Swapping pilots preserves each seed's order schedule. Each
match closes inventory by matching and checks summed participant P&L plus fees.

Opponents use current fair-value and fee criteria, not predetermined losses.
Their fair-value model and price paths remain synthetic and simplified. We report
paired differences and aggregate losses without a significance test. Curated
tables reproduce the analysis, not an outside-market sample or the full VM run.

## Performance comparisons

Native measurements use a shared Intel Xeon E-2386G Linux server, warm-up and
affinity. Personalized decisions have 20,000 samples. Timings exclude models,
signing, network transport, inclusion and finality. The prepared replay excludes
one-time packing and includes program install. First-use comparison adds 628,801 ns.

Solana uses platform tools 1.57, SBF v0, LTO and two build jobs. The optimization
baseline first corrects cumulative IOC fee rounding. Phoenix matching source
`5a34f7f901fd9e04057198d4fc7b7286f78b53f2` is rebuilt for SDK compatibility. It is
spot, not perp, and not official deployment bytes. Quantity, direction, visits
and platform are matched by path, not collateral functionality.

Arbitrum uses Solidity 0.8.30, optimizer 10,000, via-IR, Cancun, metadata hash
disabled and Foundry 1.4.4. Anvil receipt gas uses synthetic collateral/oracle
fixtures and includes intrinsic gas. Nitro posting cost and public latency are
separate. TTL batching forces fifteen-second advances and equivalent final state.

## Finality and archived evidence

The six-hour Solana run and thirty-minute followup are different sessions. Their
test collateral has six decimals; normalized units are not USD. The Arbitrum
followup uses native USDC and a separate ETH budget. Old insurance is not new fees.

All Arbitrum followup receipts and account state were checked against canonical
finalized blocks. Historical baseline insurance/debt/USDC values were read from
both Blast and Tenderly, matching each other and the baseline block hash. Other
finalized reads used the official RPC. Reconciliation was read-only and made no
new signatures/trades. Empty IOC was the previously recorded loop-stop reason.

[Provenance](provenance.json) records source/build identities, archived-file hashes
and representative public transaction links. Hashes identify source files, not
their truth. Full historical SQLite journals, signed payloads, API responses,
private profiles and credentials are not distributed. Reproduction here means
table arithmetic, figures and engine offline fixtures, not the whole live run.

## License and citation

Original manuscript, tables and scripts use the repository's MIT license.
Third-party documentation/software retain their terms; their page contents are
not redistributed. `CITATION.cff` identifies a working paper without a fabricated
DOI, review status or institutional author list.
