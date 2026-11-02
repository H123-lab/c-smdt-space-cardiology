#!/usr/bin/env python3
"""
C-SMDT Methodological Rigor Suite - Calibration Validator
Enforces that subject personalization errors remain strictly below clinical thresholds.
"""
import os
import pandas as pd

def test_subject_personalization_error_bounds():
    """Asserts that individual calibrated parameter errors do not exceed clinical limits."""
    path = "./personalization/calibration_error_residuals.csv"
    assert os.path.exists(path), f"Missing calibration error logs at: {path}"
    
    df = pd.read_csv(path)
    
    for idx, row in df.iterrows():
        ef_error = float(row['EF_Absolute_Error_Pct'])
        sv_error = float(row['SV_Absolute_Error_mL'])
        cv_score = float(row['Cross_Validation_Score'])
        
        # Enforce strict engineering limits on optimization quality
        assert ef_error <= 1.0, f"Subject {row['Subject_Profile_ID']} EF calibration error too high: {ef_error}%"
        assert sv_error <= 1.5, f"Subject {row['Subject_Profile_ID']} SV calibration error too high: {sv_error} mL"
        assert cv_score >= 0.90, f"Subject {row['Subject_Profile_ID']} cross-validation score too low: {cv_score}"
