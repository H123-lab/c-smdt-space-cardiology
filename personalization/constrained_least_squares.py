#!/usr/bin/env python3
"""
C-SMDT Personalization System - Constrained Least-Squares
Demonstrates optimization bounding sweeps matching target clinical metrics.
"""

import numpy as np
from scipy.optimize import minimize
from calibration_objective_function import compute_calibration_residual

def mock_forward_model(params):
    """Emulates output parameters returned by COMSOL structural parameters."""
    r_prox, c_vessel = params[0], params[1]
    
    # System response scaling equations
    edv = 140.0 * (c_vessel / 0.015)
    esv = 40.0 * (r_prox / 16.2)
    map_val = 6.0 * r_prox
    ef = ((edv - esv) / edv) * 100.0
    return [edv, esv, map_val, ef]

def run_constrained_least_squares(target_clinical):
    # Parameter limits structure: [R_prox, C_vessel]
    initial_guess = [14.0, 0.012]
    bounds = [(10.0, 25.0), (0.005, 0.030)]
    
    loss_closure = lambda p: compute_calibration_residual(mock_forward_model(p), target_clinical)
    
    result = minimize(loss_closure, initial_guess, method='L-BFGS-B', bounds=bounds)
    return result

if __name__ == "__main__":
    clinical_benchmarks = [122.0, 44.0, 93.3, 63.93]
    opt_res = run_constrained_least_squares(clinical_benchmarks)
    print(f"[L-BFGS-B] Optimization Complete. Success: {opt_res.success}")
    print(f"  -> Calibrated Parameters Matrix: R_prox={opt_res.x[0]:.2f}, C_vessel={opt_res.x[1]:.4f}")
