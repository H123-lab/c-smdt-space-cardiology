#!/usr/bin/env python3
"""Verifies data ingestion pipeline parsers across the parameter json files."""
import os
import json

def test_parameter_files_load_without_exceptions():
    """Loops through parameters block to confirm valid JSON compliance formatting."""
    target_files = [
        "./parameters/baseline_parameters.json",
        "./parameters/gravity_conditions.json",
        "./parameters/holzapfel_ogden_material.json",
        "./parameters/blood_rheology.json"
    ]
    for path in target_files:
        assert os.path.exists(path), f"Required parameter node missing at: {path}"
        with open(path, 'r') as f:
            data = json.load(f)
        assert len(data) > 0, f"Parameter descriptor array is empty for file: {path}"

def test_holzapfel_ogden_constant_bounds():
    """Asserts that myocardial passive stiffness parameters are initialized positively."""
    path = "./parameters/holzapfel_ogden_material.json"
    if os.path.exists(path):
        with open(path, 'r') as f:
            data = json.load(f)
        a_param = data['Myocardial_Tissue_Constants_kPa']['a_isotropic_matrix_stiffness']
        af_param = data['Myocardial_Tissue_Constants_kPa']['a_f_fiber_direction_stiffness']
        assert a_param > 0.0, "Holzapfel-Ogden parameter 'a' must be positive."
        assert af_param > 0.0, "Holzapfel-Ogden parameter 'af' must be positive."
