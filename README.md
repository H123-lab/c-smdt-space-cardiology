# Cardio-Spatial Multi-Domain Digital Twin (C-SMDT) for Spaceflight Hemodynamics

The **Cardio-Spatial Multi-Domain Digital Twin (C-SMDT)** is an end-to-end multi-physics computational framework designed to simulate left ventricular electromechanics, fluid-structure interaction (FSI), and closed-loop autonomic nervous system (ANS) regulatory responses across varying gravitational domains ($1\text{G}$ Earth, $0.38\text{G}$ Mars, $0\text{G}$ Microgravity).

This repository hosts the source pipelines, template structural parameters, and evaluation protocols supporting our 2026 space medicine initiative.

## 🚀 System Architecture & Pipeline Workflow

1. **Geometry Discretization**: High-resolution anatomical reconstruction using Arbitrary Lagrangian-Eulerian (ALE) grid formulation.
2. **Multiphysics Coupling**: Strong bidirectional coupling combining fiber-aligned electromechanics, anisotropic hyperelastic tissue formulations, and incompressible fluid dynamics solvers.
3. **Circulatory Autonomic Loop**: Real-time evaluation of dynamic baroreflex resetting via coupled MATLAB external feedback scripts.


