# Data Provenance and Ancestry Map

This document establishes the origin and ancestry lines of all primary structural and physical inputs used to construct the virtual heart mesh geometries.


| Repository Asset ID | Primary Source Origin Pool | Accession / Version Tracker | Role in C-SMDT Framework |
| :--- | :--- | :--- | :--- |
| **Anatomical Mesh Base** | NASA Open Science Data Repository (OSDR) | Cohort Control ID: BR-00214 | Births the base 3D left ventricular surface geometry boundaries tree |
| **Fiber Vector Atlas** | OpenNeuro Matrix Database | Dataset ID: ds004152-v1.0.4 | Provides the Diffusion Tensor MRI voxel array used to algorithmically map the helical myocardial fiber tracks |
| **Hyperelastic Tensors**| Living Heart Project Open Archives | Constants V2024.1.2 | Served as the structural validation baseline for the constitutive Holzapfel-Ogden mathematical formulations |
| **Windkessel Controls**  | SimVascular Open Preload Registry | Release v2025-04 | Provided the initial lumped-parameter circuit resistance and compliance bounding equations |
