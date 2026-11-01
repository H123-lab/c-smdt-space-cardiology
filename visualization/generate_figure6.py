#!/usr/bin/env python3
"""Regenerates Figure 6: Flow Vortex Disintegration Track"""
import os
import pandas as pd
import matplotlib.pyplot as plt

def run():
    csv_path = './results_reproducibility/figure6_source_data.csv'
    if not os.path.exists(csv_path): return
    df = pd.read_csv(csv_path)
    
    fig, ax = plt.subplots(figsize=(6.5, 4.5), dpi=300)
    ax.plot(df['Timeline_Months'], df['Vortex_Disintegration_0G'], color='#d62728', marker='s', label='0G Array')
    ax.plot(df['Timeline_Months'], df['Vortex_Disintegration_038G'], color='#ff7f0e', marker='o', linestyle='--', label='0.38G Target')
    
    ax.set_title('Figure 6: Diastolic Vortex Disintegration Evolution', fontsize=11, fontweight='bold')
    ax.set_xlabel('Mission Timeline (Months)', fontsize=10)
    ax.set_ylabel('Kinematic Vortex Disintegration Index', fontsize=10)
    ax.legend()
    ax.grid(True, linestyle=':', alpha=0.6)
    
    out = './visualization/figure6_output.png'
    plt.savefig(out, bbox_inches='tight')
    plt.close()
    print(f"[REGEN] Exported Figure 6 to: {out}")

if __name__ == '__main__': run()
