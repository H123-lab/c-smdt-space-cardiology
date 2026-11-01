#!/usr/bin/env python3
"""Regenerates Figure 5: Chronic Remodeling Timeline Curves"""
import os
import pandas as pd
import matplotlib.pyplot as plt

def run():
    csv_path = './results_reproducibility/figure5_source_data.csv'
    if not os.path.exists(csv_path): return
    df = pd.read_csv(csv_path)
    
    fig, ax = plt.subplots(figsize=(6.5, 4.5), dpi=300)
    ax.plot(df['Timeline_Months'], df['LV_Mass_0G_g'], color='#d62728', marker='^', linewidth=2)
    
    ax.set_title('Figure 5: Left Ventricular Mass Remodeling (0G)', fontsize=11, fontweight='bold')
    ax.set_xlabel('Mission Timeline (Months)', fontsize=10)
    ax.set_ylabel('Myocardial Left Ventricle Mass (g)', fontsize=10)
    ax.grid(True, linestyle=':', alpha=0.6)
    
    out = './visualization/figure5_output.png'
    plt.savefig(out, bbox_inches='tight')
    plt.close()
    print(f"[REGEN] Exported Figure 5 to: {out}")

if __name__ == '__main__': run()
