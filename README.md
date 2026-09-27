# Time Series Sales Analysis & Forecasting

## Project Overview

This project analyzes daily retail sales data to identify sales trends, seasonal patterns, monthly growth, volatility, and short-term forecasting performance.

The project follows a real-world business scenario where management wants to understand historical sales behavior and improve short-term sales planning.

## Business Objective

The main objectives were:

- Understand how sales change over time
- Identify long-term sales trends
- Detect recurring seasonal patterns
- Measure month-over-month growth
- Measure short-term sales volatility
- Build a simple sales forecasting baseline
- Evaluate forecast accuracy
- Identify the causes of large forecast errors
- Present findings through a business dashboard

## Dataset

The dataset contains 1,099 daily records covering January 2023 to December 2025.

### Columns

| Column | Description |
|---|---|
| Date | Daily sales date |
| Sales | Daily sales amount |
| Orders | Number of daily orders |
| Customers | Daily customer activity |
| Marketing_Spend | Daily marketing expenditure |
| Returns | Number of returns |

## Data Cleaning

The dataset contained several intentional data-quality issues.

I:

- Converted Date to datetime.
- Investigated apparent duplicate records.
- Confirmed that duplicate-looking records represented different dates and were retained.
- Investigated negative sales values.
- Retained negative sales because they represented return/refund activity.
- Identified 5 missing Marketing_Spend values.
- Used interpolation to fill missing Marketing Spend because the dataset is time-series data.
- Verified that the final dataset contained no missing values.

## Key KPIs

| KPI | Result |
|---|---:|
| Total Sales | $3,678,321.54 |
| Average Daily Sales | $3,346.97 |
| Total Orders | 39,081 |
| Total Returns | 1,738 |

## Analysis

### 1. Sales Trend

I analyzed daily sales and created a 7-day moving average to smooth daily fluctuations.

Sales showed an overall upward trend from 2023 to 2025, although daily sales had considerable volatility.

### 2. Seasonality

I aggregated sales by month across the three-year period to identify recurring seasonal patterns.

Key findings:

- December was the strongest seasonal month.
- December's average sales were approximately 32.5% above the overall monthly average.
- September was the weakest month.
- September's average sales were approximately 17.5% below the overall monthly average.

This indicates a recurring seasonal sales pattern.

### 3. Month-over-Month Growth

I calculated monthly sales growth to measure how quickly sales changed from one month to the next.

Examples:

- March 2023: +23.50%
- July 2023: -9.78%

This helped identify periods of rapid growth and decline.

### 4. Rolling Volatility

I calculated a 7-day rolling standard deviation to understand short-term sales volatility.

Higher rolling standard deviation indicates greater variation in recent daily sales, while lower values indicate more stable sales.

## Forecasting

I used a 7-day moving average as a one-day-ahead baseline forecast.

I also tested a 30-day moving-average baseline for comparison.

The goal was to establish a simple benchmark before considering more advanced forecasting methods.

## Forecast Accuracy

I evaluated the forecasts using:

- MAE — Mean Absolute Error
- RMSE — Root Mean Squared Error

| Forecast | MAE | RMSE |
|---|---:|---:|
| 7-Day Moving Average | $214.29 | $322.42 |
| 30-Day Moving Average | $215.54 | $324.58 |

The 7-day baseline produced slightly lower MAE and RMSE on this dataset.

## Forecast Error Analysis

I investigated the largest absolute forecast errors to understand why the forecast was inaccurate.

The largest errors included:

| Date | Actual Sales | Forecast | Absolute Error |
|---|---:|---:|---:|
| 2025-04-30 | -$750.00 | $3,966.48 | $4,743.86 |
| 2023-10-28 | -$500.00 | $2,631.61 | $3,262.55 |
| 2025-01-01 | $3,006.33 | $4,372.09 | $1,490.10 |
| 2025-01-03 | $2,659.12 | $4,278.63 | $1,431.15 |

### Interpretation

The largest errors came from:

- unusual refund/negative-sales events
- sudden changes in sales
- seasonal transitions around the beginning of January

This shows that a simple moving-average forecast can provide a useful baseline but cannot anticipate unexpected events or adapt immediately to changing seasonal behavior.

## Dashboard

The final dashboard contains:

### KPI Cards

- Total Sales
- Average Daily Sales
- Total Orders
- Total Returns

### Visualizations

1. Sales Trend & 7-Day Moving Average
2. Monthly Sales Trend by Year
3. Average Sales by Month — Seasonal Pattern
4. Monthly Sales Growth (MoM)
5. Actual Sales vs 1-Day-Ahead Forecast

## Business Insights

### Sales Growth

The business demonstrated an overall upward sales trend between 2023 and 2025.

### Seasonal Planning

December showed substantially stronger sales performance, while September was comparatively weaker. This information could support inventory, staffing, and promotional planning.

### Forecasting

The 7-day moving-average baseline produced slightly lower forecasting errors than the 30-day baseline.

### Forecast Limitations

The largest errors occurred during unusual refund events and seasonal transitions, demonstrating that moving averages cannot anticipate sudden changes.

### Future Improvement

A more advanced forecasting approach could incorporate:

- trend
- seasonality
- holidays
- promotions
- marketing spend
- returns
- other external factors

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Google Colab

## Skills Demonstrated

- Data cleaning
- Time-series data preparation
- Exploratory Data Analysis
- KPI development
- Trend analysis
- Seasonality analysis
- Month-over-month analysis
- Moving averages
- Rolling statistics
- Baseline forecasting
- Forecast evaluation
- MAE
- RMSE
- Forecast error analysis
- Data visualization
- Dashboard development
- Business insights

## Interview Summary

I analyzed three years of daily retail sales data to understand sales trends, seasonality, growth, and volatility. I cleaned and prepared the time-series data, created moving averages and rolling statistics, and developed simple one-day-ahead forecasting baselines using 7-day and 30-day moving averages. I evaluated the forecasts using MAE and RMSE and investigated the largest forecast errors. The analysis showed an overall upward trend, strong seasonality with December as the strongest month, and larger forecast errors during unusual refund events and seasonal transitions. Finally, I built a dashboard to communicate the findings and support business planning.

## Project Outcome

This project demonstrates an end-to-end time-series data analytics workflow:

Data Cleaning → KPI Analysis → Trend → Seasonality → Growth → Volatility → Forecasting → Forecast Evaluation → Business Insights → Dashboard
