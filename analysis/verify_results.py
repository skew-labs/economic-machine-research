"""Published table arithmetic; no model, wallet, network or historical journal."""
import csv, json
from collections import Counter
from decimal import Decimal as D
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def rows(name):return list(csv.DictReader((ROOT/'tables'/name).open()))
def require(value,message):
    if not value:raise ValueError(message)
def main():
    e=rows('personalized_episodes.csv')
    require(len(e)==len({r['persona'] for r in e})==30,'thirty distinct episodes')
    counts=Counter('positive' if D(r['pnl'])>0 else 'negative' if D(r['pnl'])<0 else 'flat' for r in e)
    require(counts=={'positive':23,'negative':4,'flat':3},'episode sign counts')
    for r in e:
        require(D(r['pnl'])-D(r['control_mean_pnl'])==D(r['excess_vs_control']),'paired excess')
        require(r['flat_at_handoff']=='True' and int(r['nonempty_quote_updates'])>0,'quote/handoff')
    pnl=sum(D(r['pnl']) for r in e);excess=sum(D(r['excess_vs_control']) for r in e)
    wins=sum(D(r['excess_vs_control'])>0 for r in e)
    require((pnl,excess,wins)==(D(633),D('-1536.5'),4),'episode totals')
    ledger=rows('loss_incidence.csv')
    require(len(ledger)==4 and sum(D(r['change_test_units']) for r in ledger)==0,'common window conservation')
    m=rows('paired_matches.csv')
    require(len(m)==len({(r['regime'],r['seed'],r['swapped']) for r in m})==36,'match identities')
    for r in m:
        require(int(r['steps'])==60,'steps')
        require(int(r['candidate_pnl'])-int(r['baseline_pnl'])==int(r['delta']),'match difference')
        require(sum(int(r[k]) for k in ['candidate_pnl','baseline_pnl','opponents_pnl','fees'])==0,'match ledger')
        require(int(r['conservation_residual'])==0,'match residual')
    require(sum(int(r['delta'])>0 for r in m)==23,'match wins')
    require(sum(int(r['candidate_pnl']) for r in m)==-3464,'candidate loss')
    require(sum(int(r['baseline_pnl']) for r in m)==-5578,'baseline loss')
    require(len(rows('solana_cu.csv'))==11,'CU paths')
    shocks=rows('shocks.csv')
    require(len(shocks)==7 and sum(int(r['liquidations']) for r in shocks)==45,'shock counts')
    for r in shocks:
        require((D(r['external_recapitalization'])>0)==(r['flat_depositor_exit']=='halted'),'exit incidence')
    x=json.loads((ROOT/'tables/settlement_summary.json').read_text())
    six=x['solana_six_hour'];sol=x['solana_followup'];arb=x['arbitrum_followup'];model=x['model']
    require(six['withdrawn_test_token_raw']+six['vault_fee_raw']==six['token_supply_raw'],'token conservation')
    require(all(six[k]==0 for k in ['pending','orders','open_positions','seat_collateral','conservation_residual']),'six-hour exit')
    require(sol['checked_all_runtime_finality'] and sol['original_journals_unmodified'],'Solana followup provenance')
    require(sol['orders']==0 and all(v==0 for v in sol['collateral']) and all(v==0 for v in sol['positions']),'Solana followup exit')
    require(arb['state']=='FINALIZED_SETTLED' and arb['all_receipts_finalized'] and arb['verified_receipts']==69,'Arbitrum finality')
    require(arb['deposited_usdc_raw']==arb['withdrawn_usdc_raw']+arb['session_fee_usdc_raw'],'USDC conservation')
    require(arb['initial_insurance_usdc_raw']+arb['session_fee_usdc_raw']==arb['insurance_usdc_raw']==arb['vault_usdc_raw'],'insurance lineage')
    require(all(arb[k]==0 for k in ['bad_debt_raw','base_conservation','cash_conservation_delta','residual_approval_raw','failed_transaction_count']),'Arbitrum residuals')
    require(int(arb['gas_and_prefunding_actual_wei'])<=10**15,'ETH limit')
    require(arb['currently_paused'] and arb['previous_session_journal_unmodified'],'Arbitrum exit scope')
    require(arb['accounts_checked']==6 and all(arb[k]==0 for k in ['account_cash_abs_sum','account_base_abs_sum','account_resting_lots','active_sessions']),'six accounts closed')
    require((model['reserved_attempts'],model['recorded_responses'],model['evaluated_candidates'],model['research_adoptions'])==(12,8,6,1),'model counts')
    require(model['evaluated_candidates']+model['invalid_candidates']==model['recorded_responses'],'response counts')
    require(model['recorded_responses']+model['call_timeouts']+model['unknown_after_restart']==model['reserved_attempts'],'attempt counts')
    print(json.dumps({'status':'PASS','scope':'Published table and certificate consistency; not independent live receipt verification',
        'episodes':30,'positive_episodes':23,'control_wins':wins,'episode_pnl':str(pnl),'summed_excess':str(excess),'paired_matches':36,'common_window_residual':0},indent=2))
if __name__=='__main__':main()
