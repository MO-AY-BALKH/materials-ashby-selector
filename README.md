# Material Ashby Selector – Tray optimisation for a serving robot

A Python tool for selecting optimal materials for a **lightweight tray** (thin plate under bending) used on a hospital robot.  
It ranks materials according to performance indices and generates Ashby diagrams.

## Theoretical background

The full derivation of the performance indices (structural, thermal, economic, carbon) is available in [`theory.pdf`](theory.pdf).

## Features

- **4 selection criteria**: structural, thermal, economic, carbon_footprint
- **Structural filtering** – performance line \(\sigma > k\rho^2\) eliminates weak materials
- **Top‑5 ranking** – materials with smallest index are best
- **Interactive CLI** – choose criterion by name
- **Ashby plots** – log‑log graphs saved as `ashby_diagram_food_trays_indices.png`

## Material database

Includes 15 materials (stainless steels, aluminium, polymers, woods, glass, silicone). Extensible.

