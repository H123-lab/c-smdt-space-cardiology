# COMSOL Multiphysics Model Setup and Boundary Configurations

This directory hosts the parameter files and templates required to reconstruct the **Cardio-Spatial Multi-Domain Digital Twin (C-SMDT)** inside COMSOL Multiphysics v6.2.

## 🔧 Core Physics Interface Layout
The `.mph` template file links three independent, strongly coupled physical domains via an Arbitrary Lagrangian-Eulerian (ALE) grid kinematic interface:

1. **Laminar Flow (CFD)**: Governs intracardiac fluid velocity fields via incompressible Navier-Stokes formulations.
2. **Structural Mechanics**: Models fiber-aligned myocardium tissue stress profiles using the Holzapfel–Ogden passive strain energy density parameters.
3. **Electrical Activation (AC/DC)**: Computes the transmembrane depolarization propagation sequence across a monodomain PDE interface mapping.

## 🎛️ Dynamic Parameter Controls
During transient step executions, the master Python orchestrator (`run_pipeline.py`) dynamically targets and overwrites three global variable definitions inside the geometry parameters window:
* `HR_input`: Modulates cycle frequency parameters.
* `R_prox_input`: Adjusts proximal systemic afterload constraints.
* `C_vessel_input`: Tweaks distal vascular compliance matrices.
