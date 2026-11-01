#!/usr/bin/env python3
"""
C-SMDT Personalization System - Objective Function
Calculates residual error scores checking simulated parameters against clinical benchmarks.
"""

import numpy as np

def compute_calibration_residual(simulated_vector, clinical_target_vector):
    """
    Computes the weighted least-squares residual distance.
    Vector structure: [EDV, ESV, MAP, EF]
    """
    sim = np.array(simulated_vector)
    target = np.array(clinical_target_vector)
    
    # Validation weight scaling matrices matching clinical measurement trust counts
    # Prioritizes volumetric and core arterial tracking channels
    weights = np.array([1.0, 1.0, 2.0, 1.5]) 
    
    squared_error = np.square(sim - target) * weights
    weighted_residual = np.sum(squared_error)
    
    return float(weighted_residual)

if __name__ == "__main__":
    # Internal component execution validation sweep
    mock_sim = [120.5, 45.2, 91.8, 62.5]
    mock_target = [122.0, 44.0, 93.3, 63.93]
    score = compute_calibration_residual(mock_sim, mock_target)
    print(f"[OBJECTIVE] Calculated Residual Penalty Score: {score:.5f}")
