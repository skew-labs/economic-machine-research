"""Standalone research figures from curated tables; requires matplotlib."""
import csv
from collections import defaultdict
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'figures';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,
    'figure.facecolor':'white','axes.facecolor':'white','svg.fonttype':'none','svg.hashsalt':'economic-machine-research-v0.1'})
def rows(name):return list(csv.DictReader((ROOT/'tables'/name).open()))
def save(fig,name):
    fig.savefig(OUT/(name+'.png'),dpi=200,bbox_inches='tight')
    svg=OUT/(name+'.svg')
    fig.savefig(svg,bbox_inches='tight',metadata={'Date':None})
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines())+'\n')
    plt.close(fig)
r=rows('personalized_episodes.csv');x=list(range(len(r)));p=[float(a['pnl']) for a in r];c=[float(a['control_mean_pnl']) for a in r]
fig,ax=plt.subplots(figsize=(11,4.4))
ax.bar(x,p,color=['#148477' if v>=0 else '#c94e3c' for v in p],label='Candidate episode P&L',width=.7)
ax.scatter(x,c,color='#252b35',s=24,marker='D',label='Contemporaneous control mean',zorder=3)
ax.axhline(0,color='#aab1bb',linewidth=.8);ax.set_xticks(x,[a['persona'] for a in r],rotation=90)
ax.set_ylabel('Test accounting units');ax.set_title('Positive P&L is not control superiority',loc='left',fontweight='bold',pad=16)
ax.legend(frameon=False,ncol=2,loc='upper left');ax.grid(axis='y',alpha=.15);ax.set_axisbelow(True)
fig.subplots_adjust(bottom=.28)
fig.text(.125,.025,'30 episodes; risk limits vary. 23 positive episodes, 4 above control. Not risk-normalized.',color='#555f6d',fontsize=9)
save(fig,'persona-controls')
r=rows('loss_incidence.csv');v=[int(a['change_test_units']) for a in r]
fig,ax=plt.subplots(figsize=(8.5,4))
ax.barh([a['group'] for a in r],v,color=['#148477','#44619b','#c94e3c','#8b6db0'],height=.6)
ax.invert_yaxis();ax.axvline(0,color='#8c96a5',linewidth=1);ax.set_xlim(-5000,3000)
for i,n in enumerate(v):ax.text(n+(90 if n>=0 else -90),i,f'{n:+,}',va='center',ha='left' if n>=0 else 'right',fontweight='bold')
ax.set_xlabel('Test accounting units');ax.set_title('Where maker gains came from',loc='left',fontweight='bold',pad=16)
ax.grid(axis='x',alpha=.15);ax.set_axisbelow(True)
fig.subplots_adjust(bottom=.24)
fig.text(.125,.025,'Common finalized window: participant equity changes + exchange fees = 0. Network fees excluded.',color='#555f6d',fontsize=9)
save(fig,'loss-incidence')
agg=defaultdict(lambda:[0,0])
for r in rows('paired_matches.csv'):
    agg[r['regime']][0]+=int(r['candidate_pnl']);agg[r['regime']][1]+=int(r['baseline_pnl'])
labels=['range','uptrend','downtrend','shock','oscillating','quiet'];x=list(range(6))
fig,ax=plt.subplots(figsize=(9,4.4))
ax.bar([i-.18 for i in x],[agg[k][0] for k in labels],width=.36,color='#148477',label='Candidate')
ax.bar([i+.18 for i in x],[agg[k][1] for k in labels],width=.36,color='#44619b',label='Baseline')
ax.axhline(0,color='#8c96a5',linewidth=.8);ax.set_xticks(x,labels);ax.set_ylabel('Aggregate test P&L')
ax.set_title('Relative improvement can coexist with losses',loc='left',fontweight='bold',pad=16)
ax.legend(frameon=False);ax.grid(axis='y',alpha=.15);ax.set_axisbelow(True)
fig.subplots_adjust(bottom=.24)
fig.text(.125,.025,'Six matches per regime (3 seeds x 2 seat swaps). Candidate total -3,464; baseline -5,578.',color='#555f6d',fontsize=9)
save(fig,'paired-matches')
print('Generated three PNG and three SVG figures from published tables.')
