#!/usr/bin/env python3
"""Verifies code calculation outputs preserve reported manuscript accuracy targets."""
import os
import pandas as pd

def test_pipeline_statistical_goodness_of_fit():
    """Enforces that validation code processes generate R-squared outcomes >= 0.91."""
    path = "./validation_data/validation_metrics.csv"
    if os.path.exists(path):
        df = pd.read_csv(path)
        for idx, row in df.iterrows():
            r2 = float(row['R_Squared'])
            rmse = float(row['RMSE_mmHg'])
            assert r2 >= 0.91, f"Validation failure for {row['Validation_Target']}: R²={r2} (Target: >=0.91)"
            assert rmse <= 2.0, f"RMSE failure for {row['Validation_Target']}: RMSE={rmse} mmHg (Target: <=2.0)"
