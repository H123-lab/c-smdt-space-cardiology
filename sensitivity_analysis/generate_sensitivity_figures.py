#!/usr/bin/env python3
"""
C-SMDT Sensitivity Analysis Visualization Engine
Generates publication-quality Tornado Plots evaluating parameter uncertainty impacts.
"""

import os
import matplotlib.pyplot as plt
import numpy as np

def generate_tornado_plot():
    # Configure professional formatting
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
    
    fig, ax = plt.subplots(figsize=(8, 5.5), dpi=300)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    # Data from tornado_plot_source_data.csv
    parameters = ['C_vessel_input', 'R_prox_input', 'HR_input', 'W_HO_af', 'W_HO_a', 'lambda_rheo']
    low_effect = np.array([-6.2, 5.1, 4.2, 2.1, 1.4, -0.3])
    high_effect = np.array([7.4, -5.8, -3.9, -2.4, -1.6, 0.4])

    y_pos = np.arange(len(parameters))

    # Plot bars matching low and high variation spectrums
    ax.barh(y_pos, low_effect, align='center', color='#1f77b4', alpha=0.85, label='-20% Parameter Decrease')
    ax.barh(y_pos, high_effect, align='center', color='#d62728', alpha=0.85, label='+20% Parameter Increase')
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(parameters, fontsize=9, fontweight='bold')
    ax.invert_yaxis()  # Rank parameters top-down by overall impact
    
    ax.axvline(0, color='#3c4043', linewidth=1.2, linestyle='-')
    ax.set_xlabel('Percentage Change in Target Stroke Volume (%)', fontsize=10, fontweight='bold', labelpad=10)
    ax.set_title('Global Sensitivity Matrix (Sobol LHS Perturbations)\nImpact Trajectories on Left Ventricular Stroke Volume', fontsize=11, fontweight='bold', pad=15)
    
    ax.set_xlim(-10, 10)
    ax.grid(True, linestyle=':', alpha=0.6, color='#9aa0a6')
    ax.legend(loc='lower right', frameon=True, facecolor='white', edgecolor='#dadce0', fontsize=9)
    
    plt.tight_layout()
    out_path = './sensitivity_analysis/tornado_sensitivity_plot.png'
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.savefig(out_path, bbox_inches='tight', facecolor='white')
    print(f"[SENSITIVITY] Tornado variance figure successfully exported to: {out_path}")

if __name__ == "__main__":
    generate_tornado_plot()
