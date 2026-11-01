#!/usr/bin/env python3
"""Regenerates Figure 2: Spatial Grid Convergence Stability Track"""
import os
import pandas as pd
import matplotlib.pyplot as plt

def run():
    csv_path = './results_reproducibility/figure2_source_data.csv'
    if not os.path.exists(csv_path): return
    df = pd.read_csv(csv_path)
    
    fig, ax = plt.subplots(figsize=(6.5, 4.5), dpi=300)
    ax.plot(df['DoF'], df['Apex_Longitudinal_Strain_Pct'], color='#1f77b4', marker='o', linewidth=2)
    ax.axhspan(-19.2, -20.2, color='#e8f0fe', alpha=0.5, label='Stability Zone')
    
    ax.set_xscale('log')
    ax.set_title('Figure 2: Grid Independence Verification Matrix', fontsize=11, fontweight='bold')
    ax.set_xlabel('Degrees of Freedom (DoF)', fontsize=10)
    ax.set_ylabel('Peak Myocardial Longitudinal Strain (%)', fontsize=10)
    ax.grid(True, linestyle=':', alpha=0.6)
    
    out = './visualization/figure2_output.png'
    plt.savefig(out, bbox_inches='tight')
    plt.close()
    print(f"[REGEN] Exported Figure 2 to: {out}")

if __name__ == '__main__': run()
