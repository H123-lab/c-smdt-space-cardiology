#!/usr/bin/env python3
"""Regenerates Figure 7: Autonomic Deconditioning Spectrum"""
import os
import pandas as pd
import matplotlib.pyplot as plt

def run():
    csv_path = './results_reproducibility/figure7_source_data.csv'
    if not os.path.exists(csv_path): return
    df = pd.read_csv(csv_path)
    
    fig, ax = plt.subplots(figsize=(6.5, 4.5), dpi=300)
    ax.plot(df['Timeline_Months'], df['Baroreflex_Gain_0G'], color='#d62728', linewidth=2.5, label='0G Microgravity')
    ax.plot(df['Timeline_Months'], df['Baroreflex_Gain_038G'], color='#ff7f0e', linewidth=2.5, linestyle='--', label='0.38G Mars')
    
    ax.set_title('Figure 7: Long-Term Baroreflex Sensivity Blunting', fontsize=11, fontweight='bold')
    ax.set_xlabel('Mission Timeline (Months)', fontsize=10)
    ax.set_ylabel('Baroreflex Sensitivity Gain Factor', fontsize=10)
    ax.legend()
    ax.grid(True, linestyle=':', alpha=0.6)
    
    out = './visualization/figure7_output.png'
    plt.savefig(out, bbox_inches='tight')
    plt.close()
    print(f"[REGEN] Exported Figure 7 to: {out}")

if __name__ == '__main__': run()
