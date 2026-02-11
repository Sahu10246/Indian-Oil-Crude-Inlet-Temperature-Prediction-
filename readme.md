# Indian Oil Crude Inlet Temperature Prediction

## Overview
This project develops a Polynomial Regression model to predict crude inlet temperature 
based on crude oil composition parameters.

## Dataset
- ~500+ historical crude oil composition records
- Target: Crude Inlet Temperature (°C)

## Features Used
- Density
- API
- SUL. Wt%
- KV, cSt @ 40C
- CCR, wt%
- K
- As

## Model
- Polynomial Regression (Degree = 2)
- Train-Test Split (80-20)
- Evaluation Metrics:
  - Mean Absolute Error (MAE)
  - R² Score

## Results
MAE ≈ 1.8–2.2°C on validation data.

## Business Impact
Improved process control and reduced crude wastage per batch.

## How to Run
```bash
pip install -r requirements.txt
python main.py
# Indian Oil – Crude Inlet Temperature Prediction

##  Project Overview

This project develops a **Polynomial Regression Machine Learning model** to predict **Crude Inlet Temperature (°C)** using crude oil composition and physical properties.

The objective is to enable **data-driven refinery process control**, improve thermal stability before distillation, and reduce crude wastage.

---

##  Dataset Overview

The dataset contains ~500+ historical crude oil samples including compositional and operational parameters.

###  Target Variable
- **Crude Inlet Temperature (°C)**

###  Input Features
- Density (kg/m³ @ 15°C)
- API Gravity
- Sulfur Content (SUL. Wt%)
- Kinematic Viscosity @ 40°C (cSt)
- Conradson Carbon Residue (CCR, wt%)
- Arsenic (As, ppm)

---

# Domain Understanding

##  Density

Density classifies crude oil type and impacts refining difficulty.

| Crude Type        | Density (kg/m³ @ 15°C) | Remarks |
|-------------------|------------------------|---------|
| Light Crude       | < 850                  | High API (>31.1°), more valuable |
| Medium Crude      | 850 – 900              | Moderate refining effort |
| Heavy Crude       | > 900                  | Harder to refine |
| Extra Heavy Crude | > 1000                 | Tar-like, requires upgrading |

---

##  API Gravity

Measures how light or heavy crude is relative to water.

Higher API → Lighter crude → Higher refining value.

| API Gravity | Crude Type | Remarks |
|------------|------------|---------|
| > 45       | Extra Light | High naphtha yield |
| 35 – 45    | Light | Ideal refining range |
| 22.3 – 35  | Medium | Requires more processing |
| < 22.3     | Heavy | High residue content |
| < 10       | Extra Heavy | Difficult to refine |

**Most valuable API range: 35–45**

---

##  Sulfur Content (SUL. Wt%)

Determines whether crude is "sweet" or "sour".

| SUL. Wt% | Classification | Remarks |
|----------|----------------|---------|
| < 0.1% | Ultra Sweet | Premium |
| 0.1 – 0.5% | Sweet |  Preferred by refiners |
| 0.5 – 2.0% | Sour | Higher processing cost |
| > 2.0% | Very Sour | Expensive to process |

Ideal condition:
- API: 35–45
- Sulfur: < 0.5%

---

##  Kinematic Viscosity @ 40°C

Indicates crude thickness and pumpability.

| KV @ 40°C (cSt) | Crude Type | Remarks |
|-----------------|------------|---------|
| < 10 | Very Light | Flows easily |
| 10 – 20 | Light |  Ideal |
| 20 – 50 | Medium | Needs heating |
| > 50 | Heavy | Difficult to pump |

---

##  CCR (Conradson Carbon Residue)

Measures coke-forming tendency during processing.

- High CCR → More fouling and coke formation  
- Low CCR → Cleaner refining  

---

##  Arsenic (As)

Trace contaminant that poisons refinery catalysts.

| Crude Type | Arsenic (ppm) |
|------------|--------------|
| Light Sweet | < 0.1 |
| Heavy/Sour | 0.1 – 5 |
| High Contaminant | > 5 |

---

#  Operational Variables

## Crude Inlet Temperature

Temperature of crude entering refinery units:

| Unit | Typical Inlet Temp (°C) | Purpose |
|------|------------------------|---------|
| Desalter | 100 – 150 | Removes salts & water |
| Preheat Train | 150 – 300 | Heat recovery |
| Furnace | 280 – 360 | Final heating before distillation |

Example:
- Crude Inlet = 120°C  
- Crude Outlet = 310°C  
- ΔT = 190°C  

---

## Crude Outlet Temperature

Temperature before atmospheric distillation column.

| Stage | Outlet Temp (°C) |
|-------|------------------|
| Desalter | 120 – 150 |
| Preheat Train | 250 – 330 |
| Furnace | 320 – 370 |

---

## ΔT (Temperature Difference)

| Stage | Expected ΔT (°C) |
|--------|----------------|
| Desalter | 10 – 40 |
| Heat Exchanger Train | 100 – 200 |
| Furnace | 50 – 100 |
| Total ΔT | 200 – 250 |

---

## Crude Flow Rate

### By Refinery Size

| Size | Flow (BPD) | Flow (m³/h) |
|------|------------|------------|
| Small | 5,000 – 30,000 | 30 – 200 |
| Medium | 50,000 – 150,000 | 300 – 900 |
| Large | 200,000 – 400,000+ | 1200 – 2500+ |

### By Unit

| Unit | Flow (m³/h) |
|------|------------|
| Desalter | 50 – 1000 |
| Furnace Feed | 100 – 1200 |
| Blending | 5 – 100 |
| Pilot Plant | 1 – 5 |

---

#  Model Development

### Model Used
Polynomial Regression (Degree = 2)

### Why Polynomial Regression?
- Captures nonlinear interactions between crude properties
- Interpretable model
- Suitable for moderate-sized dataset (~500 samples)

### Train/Test Split
80% Training  
20% Validation  

### Evaluation Metrics
- Mean Absolute Error (MAE)
- R² Score

### Validation Performance
MAE ≈ **1.8 – 2.2 °C**

---

#  Business Impact

- Improved thermal stability before distillation
- Better energy utilization
- Estimated ~5% reduction in crude wastage per batch
- Supports data-driven refinery optimization

---

#  How to Run

```bash
pip install -r requirements.txt
python main.py
```

---

#  Future Enhancements

- Cross-validation
- Outlier detection (Z-score/IQR)
- Feature scaling
- MLflow experiment tracking
- API deployment using Flask
- Real-time refinery integration

---

