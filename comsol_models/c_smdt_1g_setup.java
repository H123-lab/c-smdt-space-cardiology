/*
 * COMSOL Multiphysics API Model Architecture Blueprint
 * File: c_smdt_1g_setup.java
 * Description: Programmatic synthesis of the Cardio-Spatial Multi-Domain Digital Twin (C-SMDT).
 * Target Engine: COMSOL Multiphysics v6.2 API compiler framework.
 */

import com.comsol.model.*;
import com.comsol.model.util.*;

public class c_smdt_1g_setup {

  public static Model run() {
    // Instantiate the primary core model container
    Model model = ModelUtil.create("Model");

    // =========================================================================
    // 1. GLOBAL PARAMETER REGISTRY INGESTION
    // =========================================================================
    model.param().set("HR_input", "70[1/min]", "Target cycle heart rate frequency");
    model.param().set("R_prox_input", "16.20[mmHg*min/L]", "Proximal characteristic aortic resistor");
    model.param().set("C_vessel_input", "0.0150[mL/mmHg]", "Systemic compliance afterload matrix parameter");
    model.param().set("g_vector", "9.81[m/s^2]", "Gravitational body force acceleration magnitude");
    model.param().set("rho_blood", "1060[kg/m^3]", "Incompressible fluid blood mass density");
    model.param().set("mu_blood", "0.0035[Pa*s]", "Newtonian dynamic blood shear viscosity");

    // =========================================================================
    // 2. Component Setup & 3D Topographic Mesh Mount
    // =========================================================================
    ModelNode comp1 = model.component().create("comp1", true);
    GeometryFeature geom1 = comp1.geom().create("geom1", 3);
    
    // Mount the reconstructed baseline 3D geometry surface mesh layer
    GeometryFeature imp1 = geom1.feature().create("imp1", "Import");
    imp1.set("filename", "geometry_and_mesh/baseline_lv_geometry.stl");
    imp1.set("type", "mesh");
    geom1.run();

    // =========================================================================
    // 3. MULTIPHYSICS DOMAIN NODE SELECTIONS & COUPLING SETUP
    // =========================================================================
    
    // Domain Interface A: Laminar Flow Computational Fluid Dynamics (spf)
    PhysicsFeature spf = comp1.physics().create("spf", "LaminarFlow", "geom1");
    spf.selection().set(new int[]{1}); // Cavity internal domain indexing
    spf.feature("fluid1").set("rho", "rho_blood");
    spf.feature("fluid1").set("mu", "mu_blood");
    
    // Boundary Conditions: Mitral Inlet and Aortic Windkessel Pressure Outlet
    spf.feature().create("inl1", "InletBoundary", 2);
    spf.feature("inl1").selection().set(new int[]{2}); // Mitral valve coordinate patch
    
    spf.feature().create("out1", "OutletBoundary", 2);
    spf.feature("out1").selection().set(new int[]{3}); // Aortic valve coordinate patch
    spf.feature("out1").set("outletType", "Pressure");
    spf.feature("out1").set("p0", "p_Windkessel_afterload");

    // Domain Interface B: Solid Mechanics (Anisotropic Hyperelasticity)
    PhysicsFeature solid = comp1.physics().create("solid", "SolidMechanics", "geom1");
    solid.selection().set(new int[]{2}); // Ventricular muscular tissue wall indexing
    
    PhysicsFeature mat1 = solid.feature().create("hmm1", "HyperelasticMaterial", 3);
    mat1.set("MaterialModel", "HolzapfelOgden");
    mat1.set("a", "0.496[kPa]");
    mat1.set("b", "7.24");
    mat1.set("a_f", "2.23[kPa]");
    mat1.set("b_f", "11.43");

    // Domain Interface C: Electric Currents (Monodomain Cardiac Electrophysiology)
    PhysicsFeature ec = comp1.physics().create("ec", "ElectricCurrents", "geom1");
    ec.selection().set(new int[]{2}); 
    ec.feature("mnd1").set("AnisotropicConductivityType", "FiberAligned");

    // Kinematic Mesh Interface: Bidirectional Arbitrary Lagrangian-Eulerian Coupling
    MultiphysicsFeature fsi = comp1.multiphysics().create("fsi1", "FluidStructureInteraction", 2);
    fsi.selection().set(new int[]{4}); // Shared fluid-endocardial interface boundary patch
    fsi.set("FluidPhysics", "spf");
    fsi.set("SolidPhysics", "solid");

    // =========================================================================
    // 4. PRODUCTION SPACE DISCRETIZATION (Mesh M4 Setup)
    // =========================================================================
    MeshFeature mesh1 = comp1.mesh().create("mesh1");
    mesh1.feature().create("ftri1", "FreeTetrahedral");
    mesh1.feature("ftri1").feature().create("size1", "Size");
    mesh1.feature("ftri1").feature("size1").set("hmax", "1.5[mm]"); 
    mesh1.feature("ftri1").feature("size1").set("hmin", "0.4[mm]");
    mesh1.run();

    // =========================================================================
    // 5. TRANSIENT HPC PARALLELIZED SOLVER SEQUENCING
    // =========================================================================
    StudyFeature std1 = model.study().create("std1");
    TransientStage step1 = std1.createStage("time", "Transient");
    step1.set("tlist", "range(0,0.001,1.0)"); // 1 heartbeat evaluated at 1ms increments
    
    SolutionFeature sol1 = model.sol().create("sol1");
    sol1.study("std1");
    sol1.feature().create("st1", "StudyStep");
    sol1.feature().create("v1", "Variables");
    
    SolutionFeature s1 = sol1.feature().create("s1", "Stationary");
    s1.feature().create("p1", "PARDISO"); // Bind multi-threaded PARDISO solver matrix
    
    System.out.println("[COMPILATION] COMSOL C-SMDT Architecture Pipeline Generated Successfully.");
    return model;
  }

  public static void main(String[] args) {
    run();
  }
}
