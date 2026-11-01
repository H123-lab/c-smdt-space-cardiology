# Cardio-Spatial Multi-Domain Digital Twin (C-SMDT) for Spaceflight Hemodynamics

The **Cardio-Spatial Multi-Domain Digital Twin (C-SMDT)** is an end-to-end multi-physics computational framework designed to simulate left ventricular electromechanics, fluid-structure interaction (FSI), and closed-loop autonomic nervous system (ANS) regulatory responses across varying gravitational domains ($1\text{G}$ Earth, $0.38\text{G}$ Mars, $0\text{G}$ Microgravity).

This repository hosts the source pipelines, template structural parameters, and evaluation protocols supporting our 2026 space medicine initiative.

## 🚀 System Architecture & Pipeline Workflow

1. **Geometry Discretization**: High-resolution anatomical reconstruction using Arbitrary Lagrangian-Eulerian (ALE) grid formulation.
2. **Multiphysics Coupling**: Strong bidirectional coupling combining fiber-aligned electromechanics, anisotropic hyperelastic tissue formulations, and incompressible fluid dynamics solvers.
3. **Circulatory Autonomic Loop**: Real-time evaluation of dynamic baroreflex resetting via coupled MATLAB external feedback scripts.


## 💻 Compute Infrastructure Requirements

Due to the intensive degrees of freedom ($2.1 \times 10^6$) required by the FSI interface loops, the execution engine requires the following high-performance computing environment:

* **Operating System**: Ubuntu 24.04 LTS
* **Processor Hardware**: Dedicated parallel execution clusters (Minimum 16-thread hardware allocation)
* **GPU Hardware Accelerators**: NVIDIA RTX 8090 GPU (Minimum 64GB VRAM deployment)
* **System Volatile Memory**: Minimum 512GB System RAM
* **Average Computing Cycle Runtime**: 2.5 to 4.5 hours per full simulated cardiac sequence

## 📄 Computational Protocol

The formalized setup execution steps are documented in [PROTOCOL.md](./PROTOCOL.md).

## 🔏 Open Access & Commercial Dependency Disclaimer

The core structural-mechanics templates, data-generation engines, and boundary condition profiles shared here are open source under the MIT License. The underlying fluid solver modules require active runtime execution licensing for COMSOL Multiphysics v6.2 and MATLAB R2025a.
