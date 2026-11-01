# Automated Software Quality Testing & Workflow Verification Suite

This directory contains automated unit tests built on the `pytest` framework to verify code architecture stability, data ingestion, and boundary range constraints for the C-SMDT pipeline.

## 🚀 Execution Instructions

To execute the entire verification suite locally or on an HPC cluster node, run the following terminal command from your repository root directory:

```bash
pytest -v tests/
```

## 🛠️ Verification Coverage Matrices
* **Mesh & Geometry**: Verifies facet manifold properties and production grid boundary sizes.
* **Parameter Ingestion**: Guarantees unit systems and constants match input bounds.
* **Hemodynamic Clamping**: Ensures computed physiological values do not drift into unphysiological boundaries.
