import pandas as pd
import matplotlib.pyplot as plt

# Load rainfall data
data = pd.read_csv("../data/rainfall_noaa.csv")

# Watershed parameters
curve_number = 75
watershed_area_km2 = 50

# Calculate potential retention
S = (25400 / curve_number) - 254

runoff = []

for P in data["rainfall_mm"]:

    if P > 0.2 * S:
        Q = ((P - 0.2*S)**2) / (P + 0.8*S)
    else:
        Q = 0

    runoff.append(Q)

data["runoff_mm"] = runoff

# Convert runoff depth to discharge (m3/s approx)
area_m2 = watershed_area_km2 * 1e6
runoff_m = data["runoff_mm"] / 1000

data["discharge_m3"] = runoff_m * area_m2

# Plot hydrograph
plt.figure(figsize=(8,5))

plt.plot(data["date"], data["rainfall_mm"], label="Rainfall (mm)")
plt.plot(data["date"], data["runoff_mm"], label="Runoff (mm)")

plt.xlabel("Date")
plt.ylabel("Water Depth (mm)")
plt.title("Watershed Rainfall–Runoff Hydrograph")

plt.xticks(rotation=45)

plt.legend()
plt.tight_layout()

plt.savefig("../output/hydrograph.png")

plt.show()

# Save results
data.to_csv("../output/runoff_results.csv", index=False)

print("Simulation complete.")