#!/usr/bin/env bash
# ==============================================================================
# C-SMDT Lightweight Test Bench: 1G Earth Baseline Execution Loop
# ==============================================================================
set -e

echo "[INIT] Initializing C-SMDT Lightweight Test Bench (1G Earth Profile)..."
echo "[INFO] Target Workspace: Synthetic Test Subject (example_subject.json)"

# Execute the core Python orchestrator restricted to 5 demonstration tracking cycles
python3 simulation_pipeline/run_pipeline.py \
    --model_path "./comsol_models/c_smdt_1g_setup.mph" \
    --subject_config "./example_run/example_subject.json" \
    --gravity_regime "1G" \
    --total_duration_days 5 \
    --output_suffix "demo_1g"

echo "[SUCCESS] Demo run complete. Comparing generated data against expected thresholds..."
python3 -c "
import pandas as pd
df = pd.read_csv('./validation_data/raw_simulation_outputs_demo_1g.csv').iloc[-1]
exp = pd.read_csv('./example_run/expected_outputs/expected_ef.csv').iloc[0]
diff = abs(df['EF_Pct'] - exp['Expected_1G_EF'])
print(f'-> Local EF: {df[\"EF_Pct\"]:.2f}%, Expected: {exp[\"Expected_1G_EF\"]:.2f}%')
print('-> Installation Status: VERIFIED' if diff < 1.5 else '-> Installation Status: DEFECTIVE / RE-MESH')
"
