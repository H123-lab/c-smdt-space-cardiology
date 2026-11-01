# Grid Independence Verification and Mesh Convergence Report
**Project:** Cardio-Spatial Multi-Domain Digital Twin (C-SMDT)  
**Platform:** COMSOL Multiphysics v6.2 / Python API Orchestrator  
**Status:** PASSED (Asymptotic Stability Achieved)

## 1. Study Objective
To establish computational grid independence for the bidirectional Fluid-Structure-Electrophysiology Interaction (FSEI) left ventricular models. This verification guarantees that spatial discretization limits do not introduce numerical artifacts or cross-domain instability when switching between gravitational acceleration inputs ($1\text{G}$, $0.38\text{G}$, $0\text{G}$).

## 2. Spatial Discretization Metrics
Five mesh densities were investigated using adaptive tetrahedral structural elements featuring localized boundary-layer refinement at high-curvature regions: the Mitral Valve Annulus, Left Ventricular Outflow Tract (LVOT), and the Ventricular Apex.

### Mesh Convergence Matrix

| Mesh ID | Elements Count | Degrees of Freedom (DoF) | Peak Myocardial Strain ($\epsilon_{max}$) | PV Loop Area Deviation vs. M5 | Cycle Solve Runtime (NVIDIA RTX 8090) | Convergence Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **M1** (Coarse) | 45,210 | 316,470 | -14.2% | 14.85% | 0.42 hours | Failed |
| **M2** (Medium) | 112,800 | 789,600 | -17.5% | 8.12% | 1.15 hours | Failed |
| **M3** (Fine) | 210,450 | 1,473,150 | -19.2% | 3.45% | 2.10 hours | Marginal |
| **M4 (Selected)**| **302,140** | **2,114,980** | **-19.8%** | **0.84%** | **3.22 hours** | **PASSED** |
| **M5** (Extreme)| 524,000 | 3,668,000 | -19.9% | *Baseline* | 7.65 hours | Asymptotic |

## 3. Convergence Verification Criteria
* **Primary Target Bounds:** Spatial independence is verified when the variation in peak longitudinal wall strain is $<5\%$ and the relative change in the integrated Pressure-Volume (PV) loop area is $<3\%$ across consecutive mesh refinements.
* **Outcome:** The transition from **M4** to **M5** yielded a negligible **0.84%** change in the dynamic PV energy loop profile despite a 73% increase in DoF workload. **Mesh M4** optimizes the speed-to-fidelity tradeoff and is locked as the production standard for all three gravity mission configurations.

## 4. Time-Step ($\Delta t$) Dependency Sweeps
With the M4 spatial grid fixed, transient solver sensitivity checks were executed across an intentional range of backward differentiation formula (BDF) time steps under acute microgravity ($0\text{G}$) initial fluid constraints:

* $\Delta t = 5.0\text{ ms}$: Divergence encountered at early systolic ejection due to ALE boundary mesh distortion.
* $\Delta t = 2.0\text{ ms}$: Stable execution; peak pressure residuals capped at $< 10^{-4}$.
* $\Delta t = 1.0\text{ ms}$ **(Production Default)**: Maximum FSI velocity residual stabilized at $< 10^{-5}$.
* $\Delta t = 0.5\text{ ms}$: Identical hemodynamic waveforms produced; increases computing wall-clock times by 95%.
