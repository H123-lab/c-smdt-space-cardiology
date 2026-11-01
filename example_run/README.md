# Lightweight End-to-End Example Demonstration

This directory contains a standalone, lightweight test bench designed to quickly verify the installation, solver configurations, and mathematical loops of the C-SMDT pipeline using a synthetic test subject.

## 🚀 Quick-Start Execution Guide

To run a rapid 5-cycle initialization simulation for any targeted gravitational environment, execute the corresponding shell script directly from your terminal:

```bash
# Run Earth Baseline (1G) Demonstration
bash example_run/run_example_1g.sh

# Run Martian Paradigm (0.38G) Demonstration
bash example_run/run_example_038g.sh

# Run Microgravity Atrophy (0G) Demonstration
bash example_run/run_example_0g.sh
```

## 📊 Verification and Numerical Tolerance Checks
Upon completion, the execution loops will output computed metrics into your localized workspace. Cross-reference your results with the matrix profiles inside `expected_outputs/`. Installations are verified as **successful and correct** if your locally computed metrics fall within the acceptable boundary tolerances ($\pm1.5\%$ variation limits) detailed in the expected tracking files.
