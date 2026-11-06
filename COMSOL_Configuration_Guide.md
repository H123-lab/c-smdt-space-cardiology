# COMSOL Multiphysics v6.2 - Cardiovascular Implementation Configuration

This repository contains the configuration details and parameter specifications required to reproduce the integrated computational cardiac framework.

## 1. Electrical Activation (Biological Tissue Interface)
* **Physics Interface:** Electrostatics / Excitable Media (`bio`)
* **Governing Equation Type:** Aliev-Panfilov / FitzHugh-Nagumo Monodomain Variant
* **Key Differential Equations:**
  $$\frac{\partial u}{\partial t} = \nabla \cdot (D \nabla u) - k u (u - a)(u - 1) - u v$$
  $$\frac{\partial v}{\partial t} = \epsilon(u) (k_v u - v)$$
* **Fiber Alignment Strategy:** Curvilinear Coordinates interface mapping local active fiber directions ($f_0$) across the myocardial walls.
* **Myocardial Conduction Velocity:** Longitudinal ($0.6\text{ m/s}$), Transverse ($0.2\text{ m/s}$).

## 2. Fully Coupled Multiphysics Solver Sequence
To resolve the tightly coupled fluid-structure-electrophysiology interactions under varying gravitational stresses (1G, 0.38G, 0G), a monolithic fully coupled solver configuration is implemented.
* **Solver Node:** `Study 1 -> Solver Configurations -> Solution 1 -> Stationary/Time-Dependent Solver`
* **Coupling Method:** Monolithic (Fully Coupled)
* **Linear System Solver:** PARDISO (Direct Solver)
* **Time-Stepping Method:** BDF (Backward Differentiation Formula)
* **Convergence Tolerances:** Relative tolerance set strictly to $1 \times 10^{-3}$
* **Nonlinear Method:** Newton (Automatic/Constant Newton)

## 3. Baroreflex Control Loop (Global ODEs and DAEs)
The closed-loop baroreflex regulation is represented using differential-algebraic equations tracking heart rate responses to shifting mean arterial pressures ($P_{ma}$).
* **Interface:** Global ODEs and DAEs (`ge`)
* **Governing ODE Feedback Loop:**
  $$\tau_b \frac{dHR(t)}{dt} + HR(t) = HR_{baseline} - G_b \cdot (P_{ma}(t) - P_{target})$$
* **Parameters Configured:** 
  * Baroreflex time constant ($\tau_b$): $2.5\text{ s}$
  * Feedback gain ($G_b$): $1.2\text{ bpm/mmHg}$
  * Target mean arterial pressure ($P_{target}$): $95\text{ mmHg}$

## 4. Hyperelastic Tissue-Remodeling (Solid Mechanics)
* **Constitutive Structural Model:** Holzapfel-Gasser-Ogden (HGO) hyperelastic material model for passive myocardium.
* **Inelastic Remodeling Interface:** `Solid Mechanics -> External Strain / Inelastic Strain`
* **Growth Tensor Formulation:**
  $$\mathbf{F} = \mathbf{F}_e \mathbf{F}_g$$
  $$\frac{d\mathbf{F}_g}{dt} = \eta_g \left( \boldsymbol{\sigma}_{dev} - \boldsymbol{\sigma}_{target} \right) \mathbf{F}_g$$
* **Remodeling Trigger:** Driven by time-averaged deviatoric wall stresses ($\boldsymbol{\sigma}_{dev}$) departing from homeostatic baseline limits ($\boldsymbol{\sigma}_{target}$).
