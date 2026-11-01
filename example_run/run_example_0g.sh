#!/usr/bin/env bash
# ==============================================================================
# C-SMDT Lightweight Test Bench: 0G Microgravity Atrophy Execution Loop
# ==============================================================================
set -e

echo "[INIT] Initializing C-SMDT Lightweight Test Bench (0G Microgravity Profile)..."

python3 simulation_pipeline/run_pipeline.py \
    --model_path "./comsol_models/c_smdt_1g_setup.mph" \
    --subject_config "./example_run/example_subject.json" \
    --gravity_regime "0G" \
    --total_duration_days 5 \
    --output_suffix "demo_0g"

echo "[SUCCESS] Demo run complete."
