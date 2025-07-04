# Electric Vehicles Efficiency Analysis with Power BI
## Project Goal
The purpose of this project was to analyze a dataset of electric vehicle (EV) specifications to:
- Identify the most efficient EV model based on energy consumption.
- Determine the most efficient car body type in terms of range and battery capacity.
- Uncover actionable insights and performance patterns through interactive data visualizations.
## Dataset
- Source: CSV file containing detailed EV specifications.
- Features include: Brand, Model, Top speed, Battery Capacity, Battery Type, Number of Cells, Torque, Efficiency, Range, Acceleration,
  Fast Charging Power, Fast Charge Port, Towing Capacity, Cargo Volume, Seats, Drivetrain, Segment, Length, Width, Height, Car Body Type, Source.
## Tools & Technologies
- Power BI — for data modeling and visualization
- Power Query (M) — for data transformation and cleaning
- DAX — for custom calculations and metrics
- Python — used for predicting missing values (see below)
- CSV file — as the primary data source
##  Data preprocessing
A comprehensive cleanup was performed:
- Renamed and formatted columns for clarity.
- Converted data types for accurate aggregation and filtering.
- Removed rows with excessive missing values and eliminated duplicate records.
- Cleaned string fields to remove unwanted characters (e.g. from units or sources).
### Handling Missing Data
The column Towing Capacity (kg) was missing in approximately 28% of records.
To preserve valuable data, a Python script was used to predict missing values using a linear model trained on:
- Length, Width, Height
- Drivetrain
- Torque
The result was the prediction of missing values based on machine learning.
## Key Calculations
### DAX Measures:
- Avg Efficiency — average energy consumption (Wh/km) for all vehicles
- Max Efficiency — worst energy performance (highest Wh/km)
- Min Efficiency — best energy performance (lowest Wh/km)
- Top Brand & Model by Efficiency Index — most efficient model by custom index
- Top Car Body Type by Efficiency per Battery — most optimized car body type
- NoModelMessage — a dynamic message when no model matches user slicers
### Calculated Columns:
- Efficiency Index = Range / Efficiency (custom metric for overall effectiveness)
- Efficiency per Battery = Range / Battery (optimization metric for battery use)
## Visualizations
### The Report page contains a wide range of interactive visuals, including:
- **Top-10 most efficient EV models** (bar chart)
- **Efficiency by car body type** (column chart)
- **Scatter plot** of Range vs. Efficiency with bubble size representing battery size, grouped by body type
- **Slicers** for brand, body type, range, and battery capacity
### The Insights page:
- **Most efficient model**:
> Tesla Model 3 Long Range RWD (Highland) — best Efficiency Index.
- **Most efficient car body type**:
> Sedan — top performer in terms of efficiency and range-to-battery ratio.
- **Top-10 best EV models by Efficient Index and Efficiency per Battery** (column chart)
- **Efficiency Index and Efficiency per Battery by car body type** (bar chart)
- ## Insights & Recommendations
- Sedans offer the best efficiency-to-range ratio among all body types
- Tesla Model 3 Long Range RWD (Highland) offers the best total range to efficiency ratio
- The Efficiency Index provides a more practical way to evaluate EVs than raw energy consumption alone
- Leveraging Python for data imputation allowed a cleaner dataset and more robust analytics
