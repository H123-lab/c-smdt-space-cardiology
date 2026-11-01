#!/usr/bin/env python3
"""Automated verification check for Left Ventricular tetrahedral grid boundaries."""
import os
import pandas as pd

def test_mesh_quality_metrics_file_exists():
    """Asserts that the mesh metrics database is present in the repository tree."""
    path = "./geometry_and_mesh/mesh_quality_metrics.csv"
    assert os.path.exists(path), f"Missing core mesh quality parameters at: {path}"

def test_mesh_production_Locked_bounds():
    """Asserts that the locked M4 mesh elements do not exceed skewness tolerances."""
    path = "./geometry_and_mesh/mesh_quality_metrics.csv"
    if os.path.exists(path):
        df = pd.read_csv(path, index_with='Metric' if 'Metric' in pd.read_csv(path).columns else None)
        df.set_index('Metric', inplace=True)
        
        avg_skewness = float(df.loc['Element_Skewness', 'Average_Value'])
        inverted_count = int(df.loc['Inverted_Elements_Count', 'Average_Value'])
        
        assert avg_skewness < 0.75, f"Mesh element skewness critical error: {avg_skewness}"
        assert inverted_count == 0, f"Critical Element Inversion detected! Count: {inverted_count}"
