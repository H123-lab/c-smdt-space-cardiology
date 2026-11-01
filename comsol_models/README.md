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

## 📋 Step-by-Step Operator Setup Checklist (COMSOL GUI Configuration)

Follow this precise sequential protocol to reconstruct or verify the C-SMDT multiphysics workspace within the COMSOL Multiphysics v6.2 desktop interface:

### Step 1: Global Parameters Ingestion
1. Open COMSOL Multiphysics and select **Blank Model**.
2. Right-click **Global Definitions** and select **Parameters \(\rightarrow\) Parameters 1**.
3. Click the **Load from File** button at the bottom of the Settings window panel.
4. Select the provided text parameter spreadsheet: `comsol_models/c_smdt_1g_setup.mph.txt` to auto-populate all fluid, mechanical, and electrical variables along with their corresponding metric units.

### Step 2: Component Mounting & 3D Geometry Import
1. On the Home ribbon tab, click **Add Component \(\rightarrow\) 3D**.
2. Expand **Component 1 \(\rightarrow\) Geometry 1**, right-click it, and select **Import**.
3. In the Import settings window, change the Source dropdown menu to **Mesh**.
4. Browse to and select the baseline left ventricular model file: `geometry_and_mesh/baseline_lv_geometry.stl`. Click **Import**.

### Step 3: Material and Domain Property Configuration
1. Right-click **Component 1 \(\rightarrow\) Materials** and select **Blank Material**. Name it `Blood_Fluid`.
   * Set its domain selection strictly to the **Internal Ventricular Cavity (Domain 1)**.
   * Define its properties using the parameter nodes: Density = `rho_blood`, Dynamic Viscosity = `mu_blood`.
2. Create a second Blank Material and name it `Myocardium_Tissue`.
   * Set its domain selection strictly to the **Ventricular Wall Structure (Domain 2)**.

### Step 4: Fluid-Structure Interaction (FSI) Interface Settings
1. On the Home tab, click **Add Physics** and choose **Fluid-Structure Interaction, Laminar Flow**. Click **Add to Component 1**.
2. Expand the **Laminar Flow (spf)** node:
   * Right-click and choose **Inlet**. Set selection to the **Mitral Valve Plane (Boundary 2)**. Choose velocity boundary types driven by your diastolic parameters.
   * Right-click and choose **Outlet**. Set selection to the **Aortic Valve Plane (Boundary 3)**. Change pressure boundary type to use the dynamic parameter entry: `p_Windkessel_afterload`.
3. Expand the **Solid Mechanics (solid)** node:
   * Right-click and select **Hyperelastic Material**. Set selection to the **Ventricular Wall Structure (Domain 2)**. Change Material Model dropdown menu to **Holzapfel-Ogden**. Link properties to variables: `W_HO_a`, `W_HO_b`, `W_HO_af`, `W_HO_bf`.
   * Right-click and select **Fixed Constraint**. Set selection to the rigid epicardial valve plane ring edges to stabilize the structure.

### Step 5: Mesh Discretization (Production Fine Grid Standard)
1. Select the **Mesh 1** node in the model builder tree.
2. In the settings window panel, change the Sequence Type dropdown option to **User-controlled mesh**.
3. Expand the nested **Size** node under Mesh 1, change geometric limits to:
   * Maximum element size = `1.5[mm]`
   * Minimum element size = `0.4[mm]`
4. Click **Build All** at the top of the pane to generate the 302,140 tetrahedral elements mapping your grid arrays.

### Step 6: Solver Interfacing & Headless Python Automation
1. Right-click **Study 1** and choose **Study Steps \(\rightarrow\) Time Dependent**.
2. Change the Times entry text field string to: `range(0,0.001,1.0)` (1ms transient increments).
3. Under the **Job Configurations** matrix trees, expand the solver properties block and set the linear solver engine choice strictly to **PARDISO** to enable multi-threaded core processing.
4. Save the template setup into the project tree directory path as: `comsol_models/c_smdt_1g_setup.mph`. 
5. The model is now ready to receive incoming parallel automated execution loops from the orchestration script `simulation_pipeline/run_pipeline.py`.
