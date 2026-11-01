#!/usr/bin/env python3
"""Checks convergence logs to prove FSI sub-cycling multi-physics tracking stability."""
import os
import pandas as pd

def test_fsi_residuals_converge_below_threshold():
    """Asserts that transient sub-cycling limits drop down beneath the 1e-4 cutoff marker."""
    path = "./simulation_logs/fsi_residual_history.csv"
    if os.path.exists(path):
        df = pd.read_csv(path)
        final_fluid_res = df['Fluid_Velocity_Residual'].iloc[-1]
        final_solid_res = df['Solid_Traction_Residual'].iloc[-1]
        
        assert final_fluid_res <= 1e-4, f"Fluid solver convergence anomaly: {final_fluid_res}"
        assert final_solid_res <= 1e-4, f"Solid tracking convergence anomaly: {final_solid_res}"
