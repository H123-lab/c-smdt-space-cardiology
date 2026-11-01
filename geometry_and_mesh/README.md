# Geometry & Mesh Specification

### 1. `baseline_lv_geometry.stl`
* **Format**: ASCII StereoLithography (STL)
* **Dimensions**: Bounded bounding-box dimensions ($X: 68.4\text{ mm}$, $Y: 72.1\text{ mm}$, $Z: 114.5\text{ mm}$)
* **Anatomical Bounds**: Includes endocardial and epicardial wall surfaces spanning from the base (mitral/aortic valve rings) down to the ventricular apex.
* **Source Dataset**: Anonymized reconstruction derived from the NASA Open Science Data Repository (Spaceflight-analog control cohorts).

### 2. `fiber_orientation_atlas.vtk`
* **Format**: VTK Legacy DataFile (ASCII VECTORS and SCALARS)
* **Resolution**: $64 \times 64 \times 64$ voxel grid interpolation field
* **Biophysical Mapping**: Contains continuous structural field tensors defining local myofiber vectors. The helical angle scales natively across the ventricular wall thickness from $+60^\circ$ (inner endocardial boundary layer) shifting down to $-60^\circ$ (outer epicardial layer) to drive anisotropic finite-strain computation loops accurately.

### 3. `mesh_convergence_report.md`
* **Format**: Markdown Verification Documentation (Convertible to PDF via standard markdown parsers)
* **Mathematical Scope**: Documents grid-independence validation. It lists structural element variations, system degrees of freedom, and convergence error thresholds proving stability during the bidirectional FSEI sub-cycling loops. This file directly addresses standard reproducibility criteria required by Q1 editorial review boards.

* ### 4. `mesh_quality_metrics.csv`
* **Format**: Comma-Separated Values (CSV) database matrix
* **Verification Scope**: Lists specific geometric element quality benchmarks (skewness distributions, element angles, aspect ratios) for the target fine mesh framework to verify structural stability before compute execution.

### 5. `co_registration_rigid_transform.json`
* **Format**: Structured Javascript Object Notation (JSON) translation profile
* **Anatomical Alignment**: Preserves the exact rigid rotation arrays, isometric scaling parameters, and 3D translation coordinates used to standardize external anatomical source coordinates into the global COMSOL spatial mechanics workspace boundaries.

