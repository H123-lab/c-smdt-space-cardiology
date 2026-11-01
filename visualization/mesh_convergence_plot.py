#!/usr/bin/env python3
"""
C-SMDT Spatial Grid Independence & Mesh Convergence Chart Generator
Proves numerical stability by mapping peak myocardial strain against DoF.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

def render_mesh_convergence():
    # Configure publication-grade styling
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
    
    fig, ax1 = plt.subplots(figsize=(7.5, 5.5), dpi=300)
    ax1.set_facecolor('white')
    fig.patch.set_facecolor('white')

    # Data from mesh convergence report matrix
    dof = np.array([316470, 789600, 1473150, 2114980, 3668000])
    strain = np.array([-14.2, -17.5, -19.2, -19.8, -19.9])
    labels = ['M1\n(Coarse)', 'M2\n(Medium)', 'M3\n(Fine)', 'M4\n(Selected)', 'M5\n(Extreme)']

    # Plot spatial convergence trend line
    color_primary = '#1f77b4'
    ax1.set_xlabel('Degrees of Freedom (DoF)', fontsize=10, fontweight='bold', labelpad=10)
    ax1.set_ylabel('Peak Myocardial Longitudinal Strain ($\epsilon_{max}$, %)', fontsize=10, fontweight='bold', color=color_primary, labelpad=10)
    
    line1 = ax1.plot(dof, strain, color=color_primary, linestyle='-', marker='o', markersize=8, linewidth=2, label='Peak Longitudinal Strain')
    ax1.tick_params(axis='y', labelcolor=color_primary)
    ax1.set_ylim(-13.0, -21.0) # Invert axis physiologically for negative strain values

    # Add text labels above individual coordinates
    for i, txt in enumerate(labels):
        ax1.annotate(txt, (dof[i], strain[i]), textcoords="offset points", xytext=(0,10 if i!=3 else -20), ha='center', fontsize=8, fontweight='bold')

    # Shade the asymptotic convergence structural zone (<5% strain variation threshold)
    ax1.axhspan(-19.2, -20.2, color='#e8f0fe', alpha=0.6, label='Asymptotic Stability Zone (<5% Δ)')
    
    # Target anchor callout box at production standard mesh choice
    ax1.plot(2114980, -19.8, marker='X', color='#d62728', markersize=12, label='Production locked Grid (M4)')
    
    # Clean chart details
    ax1.set_title('Left Ventricular Spatial Discretization Independent Sweeps\nGrid Convergence Verification Metrics', fontsize=11, fontweight='bold', pad=15)
    ax1.grid(True, linestyle=':', alpha=0.6, color='#9aa0a6')
    
    # Force scannable formatting layout on DoF axis ticks
    ax1.set_xscale('log')
    ax1.set_xlim(200000, 5000000)
    ax1.get_xaxis().set_major_formatter(plt.ScalarFormatter())
    
    # Combine legend entities cleanly
    ax1.legend(loc='lower left', frameon=True, facecolor='white', edgecolor='#dadce0', fontsize=9)
    plt.tight_layout()

    # Save output asset array
    output_path = './visualization/mesh_convergence_plot.png'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, bbox_inches='tight', facecolor='white')
    print(f"[RENDER] Convergence verification chart successfully saved to: {output_path}")

if __name__ == "__main__":
    render_mesh_convergence()
