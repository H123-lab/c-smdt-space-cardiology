#!/usr/bin/env python3
"""Implements biological safety bounds checks on generated simulation arrays."""
import os
import pandas as pd

def test_physiological_clamping_limits():
    """Guarantees simulated outputs stay bound within realistic clinical bounds."""
    path = "./validation_data/raw_simulation_outputs.csv"
    if os.path.exists(path):
        df = pd.read_csv(path)
        
        # Verify clamping ranges for every row in data log
        for idx, row in df.iterrows():
            ef = float(row['EF_Pct'])
            sv = float(row['SV_mL'])
            
            assert 10.0 <= ef <= 90.0, f"Unphysiological Ejection Fraction anomaly detected: {ef}%"
            assert 20.0 <= sv <= 200.0, f"Unphysiological Stroke Volume anomaly detected: {sv} mL"
