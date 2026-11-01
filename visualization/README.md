# Visualization Scripts & Multi-Physics Render Post-Processing

This folder contains the visualization tools and scripts required to reproduce the primary figures presented in the manuscript.

* **`paraview_state.pvsm`**: An XML pipeline state file for ParaView v5.12.0. It automatically configures color mappings and tracking bounds to visualize 3D myocardial mechanical strain maps and fluid velocity streamlines without manual color window tracking adjustments.
* **`plots_generator.py`**: A python script that reads your processed numerical values to output journal-grade vector subplots displaying pressure-volume loop constraints alongside long-duration Global Longitudinal Strain (GLS) variations.
