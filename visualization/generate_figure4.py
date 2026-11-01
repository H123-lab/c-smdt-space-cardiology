#!/usr/bin/env python3
"""Regenerates Figure 4: Diastolic Flow Trace Curves"""
import os
import pandas as pd
import matplotlib.pyplot as plt

def run():
    csv_path = './results_reproducibility/figure4_source_data.csv'
    if not os.path.exists(csv_path): return
    df = pd.read_csv(csv_path)
    
    fig, ax = plt.subplots(figsize=(6.5, 4.5), dpi=300)
    ax.plot(df['Normalized_Diastole_Time'], df['Velocity_Core_1G_m_s'], color='#1f77b4', label='1G Earth')
    ax.plot(df['Normalized_Diastole_Time'], df['Velocity_Core_0G_m_s'], color='#d62728', linestyle=':', label='0G Space')
    
    ax.set_title('Figure 4: Intraventricular Velocity Core Waveforms', fontsize=11, fontweight='bold')
    ax.set_xlabel('Normalized Diastole Phase', fontsize=10)
    ax.set_ylabel('Velocity Core Magnitude (m/s)', fontsize=10)
    ax.legend()
    ax.grid(True, linestyle=':', alpha=0.6)
    
    out = './visualization/figure4_output.png'
    plt.savefig(out, bbox_inches='tight')
    plt.close()
    print(f"[REGEN] Exported Figure 4 to: {out}")

if __name__ == '__main__': run()
