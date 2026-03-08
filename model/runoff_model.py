import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../data/rainfall.csv")

soil_storage = 50
max_storage = 100

runoff = []
storage_list = []

for rain in data["rainfall_mm"]:

    soil_storage += rain

    if soil_storage > max_storage:
        excess = soil_storage - max_storage
        runoff.append(excess)
        soil_storage = max_storage
    else:
        runoff.append(0)

    storage_list.append(soil_storage)

data["runoff_mm"] = runoff
data["soil_storage"] = storage_list

data.to_csv("../output/runoff_results.csv", index=False)

plt.plot(data["rainfall_mm"], label="Rainfall")
plt.plot(data["runoff_mm"], label="Runoff")

plt.legend()
plt.show()