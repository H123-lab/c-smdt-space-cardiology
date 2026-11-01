# Sensitivity Analysis and Uncertainty Quantification (UQ) Protocol

This directory hosts the statistical datasets and automation scripts verifying the robustness of the **Cardio-Spatial Multi-Domain Digital Twin (C-SMDT)** framework under localized parameter variations.

## 1. Methodology Framework
A variance-based **Sobol Sensitivity Analysis** was executed to evaluate the relative contributions of individual input parameters to primary hemodynamic outputs (Ejection Fraction, Stroke Volume, Peak Systolic Pressure, and Global Longitudinal Strain). 

1. **Sampling Strategy**: A Latin Hypercube Sampling (LHS) grid generated $N = 1000$ model configurations across bounded parameter uncertainty intervals ($\pm20\%$ variation loops).
2. **Perturbation Bounds**: Evaluated across preload configurations, vascular afterload resistances ($R_{\mathrm{prox}}$), distal smooth muscle vessel compliance ($C_{\mathrm{vessel}}$), non-Newtonian blood rheology parameters ($\lambda$), and anisotropic myocardial hyperelastic stiffness constants ($a, a_f$).
3. **Robustness Threshold**: Gravity-dependent trends across the regimes ($1\text{G}$, $0.38\text{G}$, $0\text{G}$) are verified as robust if the direction of the gravitational effect is preserved across the entire sampled variance grid space.
