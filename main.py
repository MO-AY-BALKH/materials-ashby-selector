import numpy as np
import matplotlib.pyplot as plt

# 1. Definition of materials as a list
materials = [ # Name, ρ (kg/m3), σ (MPa), performance index, Price (€/kg), Conductivity (W/m·K), Carbon footprint (kg CO2/kg)
    ["Stainless steel (304)", 8000, 210,0, 3.5, 15, 6.2],
    ["Stainless steel (316)", 8000, 205,0, 4.2, 15, 6.5],
    ["Anodized aluminum", 2700, 150,0, 2.8, 205, 8.2],
    ["Polypropylene (PP)", 900, 25,0, 1.2, 0.22, 1.9],
    ["Polycarbonate (PC)", 1200, 60,0, 2.5, 0.2, 6.5],
    ["High-density polyethylene (HDPE)", 950, 300,0, 1.1, 0.45, 1.8],
    ["Low-density polyethylene (LDPE)", 910, 20,0, 1.0, 0.33, 1.7],
    ["Polymethyl methacrylate (PMMA - Plexiglas)", 1180, 70,0, 3.0, 0.19, 5.8],
    ["Food-grade silicone", 970, 3,0, 8.5, 0.2, 4.2],
    ["Tempered glass", 2500, 50,0, 1.8, 1.0, 1.2],
    ["Bamboo", 700, 80,0, 0.8, 0.15, 0.3],
    ["Beech", 720, 110,0, 1.5, 0.16, 0.4],
    ["Oak", 750, 90,0, 2.2, 0.17, 0.5],
    ["Mahogany", 650, 100,0, 3.5, 0.15, 0.6],
    ["Teak", 980, 140,0, 4.8, 0.14, 0.7]
]

# 2. Calculation of the performance index: I = ρ / sqrt(σe)
type_criterion = str(input("choose an index type: structural, thermal, economic, carbon_footprint: "))

if type_criterion == 'structural':
    print("performance index calculated for the structural criterion i.e. for lightness and strength")
    for mat in materials:
        rho, sigma = mat[1], mat[2]
        performance_index = rho / np.sqrt(sigma)
        mat[3] = performance_index

elif type_criterion == 'thermal':
    print("performance index calculated for the thermal criterion i.e. for the performance/thermal insulation ratio")
    for mat in materials:
        rho, sigma, conductivity = mat[1], mat[2], mat[5]
        performance_index = (rho / np.sqrt(sigma)) * (1 / conductivity)
        mat[3] = performance_index

elif type_criterion == 'economic':
    print("performance index calculated for the economic criterion i.e. for the performance/price ratio")
    for mat in materials:
        rho, sigma, price = mat[1], mat[2], mat[4]
        performance_index = rho / (np.sqrt(sigma) * price)
        mat[3] = performance_index

elif type_criterion == 'carbon_footprint':
    print("performance index calculated for the carbon footprint criterion i.e. the carbon footprint")
    for mat in materials:
        rho, sigma, carbon_footprint = mat[1], mat[2], mat[6]
        performance_index = rho / (np.sqrt(sigma) * carbon_footprint)
        mat[3] = performance_index

# 3. Filter materials above the line (σe > k * ρ²)
k = 10**-5  # Constant for the performance line
materials_above_line = [mat for mat in materials if mat[2] > k * mat[1]**2]

# 4. Selection of the 5 best materials according to the performance index
top_5 = sorted(materials_above_line, key=lambda x: x[3], reverse=True)[:5]

# 5. Display of the 5 best materials
print("\nTop 5 materials located above the performance line:\n")
for mat in top_5:
    print(f"{mat[0]} - Performance index: {mat[3]:.2f} - Density: {mat[1]} kg/m³ - Elastic strength: {mat[2]} MPa ")

# 6. Creation of the graph
plt.figure(figsize=(10, 6))

# Generate colors for each material
colors = plt.cm.viridis(np.linspace(0, 1, len(materials)))

# Dictionary to store unique labels for the legend
legend_handles = {}

# Plot each material with a unique color and add to the legend
for i, mat in enumerate(materials):
    rho, sigma = mat[1], mat[2]
    is_top_5 = mat in top_5
    color = 'red' if is_top_5 else colors[i]  # Highlight the best materials in red
    scatter = plt.scatter(rho, sigma, s=80, color=color, edgecolors='k')
    # Add to the legend (avoids duplicates)
    if mat[0] not in legend_handles:
        legend_handles[mat[0]] = scatter
    # Display names only for red materials
    if is_top_5:
        plt.text(rho * 1.05, sigma, mat[0], fontsize=9)

# Plot the performance line: σe = k * ρ^2
rho_range = np.logspace(2, 4, 100)  # Density between 100 and 10 000 kg/m^3
sigma_range = k * rho_range**2
plt.plot(rho_range, sigma_range, 'r-', linewidth=2, label="Performance line (slope = 2)")

# Graph formatting
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Density (kg/m^3)")
plt.ylabel("Elastic strength (MPa)")
plt.title("Ashby diagram: Materials for food trays")
plt.grid(True, which="both", linestyle="-", linewidth=0.5)

# Add the legend outside the graph
plt.legend(handles=legend_handles.values(),
           labels=legend_handles.keys(), loc="upper left", bbox_to_anchor=(1, 1), fontsize=8)

# Adjust the layout to leave room for the legend
plt.tight_layout(rect=[0, 0, 0.8, 1])

# Save and display the graph
plt.savefig("ashby_diagram_food_trays_indices.png", bbox_inches="tight")
plt.show()