#!/usr/bin/env python3
"""Regenerates Figure 3: Acute Localized Cardiac Metrics Log"""
import os
import pandas as pd
import matplotlib.pyplot as plt

def run():
    csv_path = './results_reproducibility/figure3_source_data.csv'
    if not os.path.exists(csv_path): return
    df = pd.read_csv(csv_path)
    
    fig, ax = plt.subplots(figsize=(6.5, 4.5), dpi=300)
    ax.bar(df['Gravity_Regime'], df['Intraventricular_Kinetic_Energy_mJ'], color=['#1f77b4', '#ff7f0e', '#d62728'], alpha=0.85)
    
    ax.set_title('Figure 3: Intraventricular Kinetic Energy Shift', fontsize=11, fontweight='bold')
    ax.set_xlabel('Gravitational Profile', fontsize=10)
    ax.set_ylabel('Kinetic Energy (mJ)', fontsize=10)
    ax.grid(True, linestyle=':', alpha=0.4)
    
    out = './visualization/figure3_output.png'
    plt.savefig(out, bbox_inches='tight')
    plt.close()
    print(f"[REGEN] Exported Figure 3 to: {out}")

if __name__ == '__main__': run()
