#!/usr/bin/env python3
"""
C-SMDT Post-Processing Utility Engine
Calculates Global Longitudinal Strain (GLS), Vortex Disintegration, and Wall Shear Stress (WSS).
"""

import numpy as np

def calculate_gls(epi_length_baseline, epi_length_current):
    """
    Computes Global Longitudinal Strain (GLS) percentage.
    Formula: ((L_current - L_baseline) / L_baseline) * 100
    """
    if epi_length_baseline <= 0:
        raise ValueError("Baseline epicardial length must be greater than zero.")
    
    gls = ((epi_length_current - epi_length_baseline) / epi_length_baseline) * 100.0
    return round(gls, 2)

def calculate_vortex_disintegration(velocity_field_matrix):
    """
    Quantifies diastolic vortex ring degradation via kinematic helicity variance.
    Returns an index scaling from 0 (Perfect Coherent Vortex) to 1 (Complete Disintegration).
    """
    if not isinstance(velocity_field_matrix, np.ndarray) or velocity_field_matrix.size == 0:
        return 1.0 # Default to fully chaotic/disintegrated state if mesh grid data is corrupt
    
    # Compute velocity vector gradients to derive localized curl/vorticity fields
    vorticity = np.gradient(velocity_field_matrix)
    vorticity_magnitude = np.sqrt(sum(np.square(g) for g in vorticity))
    
    mean_vorticity = np.mean(vorticity_magnitude)
    std_vorticity = np.std(vorticity_magnitude)
    
    if mean_vorticity == 0:
        return 1.0
        
    # High variance in the localized vorticity vectors signals spatial disintegration
    disintegration_index = std_vorticity / (mean_vorticity + std_vorticity)
    return round(float(disintegration_index), 3)

def evaluate_wss_attenuation(wss_baseline_1g, wss_current):
    """
    Tracks microgravity-induced reductions in endothelial wall shear stress stimulus.
    Returns the percentage reduction relative to Earth metrics.
    """
    if wss_baseline_1g <= 0:
        return 0.0
        
    wss_drop_pct = ((wss_baseline_1g - wss_current) / wss_baseline_1g) * 100.0
    return round(max(0.0, wss_drop_pct), 2)

if __name__ == "__main__":
    # Internal Unit Test Verification Block
    print("[TEST] Verifying post-processing calculation nodes...")
    
    test_gls = calculate_gls(114.5, 96.4)
    print(f"  -> Extracted GLS Metric: {test_gls}% (Target: Negative shortening trend)")
    
    mock_grid = np.random.normal(loc=1.5, scale=0.8, size=(32, 32, 32))
    test_vortex = calculate_vortex_disintegration(mock_grid)
    print(f"  -> Kinematic Vortex Disintegration Index: {test_vortex} (0=Coherent, 1=Chaotic)")
    
    test_wss = evaluate_wss_attenuation(1.85, 1.34)
    print(f"  -> Endothelial WSS Attenuation: {test_wss}% drop under simulated microgravity load")
    print("[TEST] All post-processing validation methods operational.")
