# Rainfall–Runoff Hydrologic Modeling using the SCS Curve Number Method

## Overview

This project demonstrates a simple hydrologic modeling workflow for simulating
watershed runoff response to rainfall events.

The model uses the **SCS Curve Number method**, a widely used approach in
hydrology for estimating runoff based on rainfall, soil type, and land use.

The project illustrates how rainfall data can be converted into runoff estimates
and visualized using a flood hydrograph.

## Features

- NOAA-style rainfall dataset
- Watershed parameter configuration
- SCS Curve Number runoff calculation
- Flood hydrograph visualization
- Python-based environmental modeling

## Project Structure
rainfall-runoff-model
│
├── data
│ └── rainfall_noaa.csv

├── model
│ ├── runoff_model.py
│ └── scs_runoff_model.py

├── output
│ ├── hydrograph.png
│ └── runoff_results.csv

└── README.md

## Hydrologic Method

Runoff is calculated using the **SCS Curve Number equation**:

Q = (P − 0.2S)² / (P + 0.8S)

Where:

- **P** = rainfall depth
- **S** = potential maximum retention
- **CN** = curve number parameter based on watershed characteristics

Retention is calculated as:

S = (25400 / CN) − 254

## Example Watershed Parameters

| Parameter | Value |
|----------|-------|
Watershed Area | 50 km² |
Curve Number | 75 |
Soil Storage | estimated from CN |

These values simulate a small mixed-use watershed.

## How to Run the Model

1. Install required Python libraries
pip install pandas matplotlib
2. Navigate to the model folder
cd rainfall-runoff-model/model
3. Run the model
python scs_runoff_model.py
## Output

The model produces:
- **Hydrograph plot**
output/hydrograph.png
- **Runoff simulation dataset**
output/runoff_results.csv
The hydrograph shows the watershed runoff response to rainfall events.

## Applications

This type of modeling is used in:

- flood prediction
- watershed hydrology
- stormwater management
- environmental modeling

## Tools Used

- Python
- Pandas
- Matplotlib

## Future Improvements

Possible extensions include:

- integrating real NOAA rainfall datasets
- watershed GIS analysis
- streamflow prediction models
- flood peak estimation

## Author

A sample hydrologic modeling project developed for environmental data science and
water resources modeling practice.
