import numpy as np
import pandas as pd
df=pd.read_csv('data/time_clean.csv')
df['Date']=pd.to_datetime(df['Date'])
c=['Date', 'Sales', 'Orders', 'Customers', 'Marketing_Spend', 'Returns']
min_day = df['Date'].min()
max_day = df['Date'].max()
num_of_days = max_day - min_day
print(f"minimum{min_day} maximum {max_day} number {num_of_days}")

#Basic KPI 
total_sales=df['Sales'].sum().round(2)
average_sales=df['Sales'].mean().round(2)
total_orders=df['Orders'].sum()
total_customers=df['Customers'].sum()
average_customers=df['Customers'].mean().round(2)
maximum_customers=df['Customers'].max()
total_returns=df['Returns'].sum()
print(f"Total Sales = {total_sales}$")
print(f"Avg Sales = {average_sales}$")
print(f"Total Orders = {total_orders}")
print(f"Total Customers = {total_customers}")
print(f"Average Daily Customers = {average_customers}")
print(f"Maximum Daily Customers = {maximum_customers}")
print(f"Total Return = {total_returns}")

#df['Month'] = df['Date'].dt.to_period('M')
#df['Month'] = df['Date'].dt.month_name()#.str[:3]
month_order = ['January','February','March','April','May','June',               'July','August','September','October',
               'November','December']
df['Month'] = pd.Categorical(df['Date'].dt.month_name(), categories=month_order, ordered=True)
df['Year'] = df['Date'].dt.to_period('Y')
#print(df[['Date','Month','Year']])
#Monthly Sales 
month_summary=df.groupby(['Year','Month']).agg(
        Total_Sale=('Sales','sum'))
#print(month_summary)

#compare the same month across years
month_pivot=df.pivot_table(index='Month',columns='Year',values='Sales',aggfunc='sum')
month_pivot['Avg_Sales']=(month_pivot['2023']+month_pivot['2024']+month_pivot['2025']/3).round(2)
#print(month_pivot)

#Step 3 - Calculate Seasonal Index 
overall_monthly_average=month_pivot['Avg_Sales'].mean()
month_pivot['Seasonal_Index']=month_pivot['Avg_Sales']/overall_monthly_average
#print(month_pivot[['Avg_Sales','Seasonal_Index']])

#Step 4 — 7 days Moving Average 
df['Sales_MA7'] = df['Sales'].rolling(window=7).mean()
df['Sales_MA7']=df['Sales_MA7'].round(2)
#print(df[['Date','Sales','Sales_MA7']].head(10))

#Monthly Sales Table with MoM Growth %
month_summary['MoM_Growth_%'] = month_summary['Total_Sale'].pct_change() * 100
month_summary['MoM_Growth_%'] = month_summary['MoM_Growth_%'].round(2)
#print(month_summary)

#Create a 7-day rolling standard deviation for Sales
df['Sales_STD7'] = df['Sales'].rolling(window=7).std()
#print(df[['Date','Sales','Sales_MA7','Sales_STD7']].head(10))

#Forecast future sales based on historical patterns.
#Time-Series Forecasting with a simple baseline.

#Create a 1-day-ahead baseline forecast using your 7-day moving average.
df['Forecast_1D_Ahead'] = df['Sales_MA7'].shift(1)
df['Forecast_1D_Ahead']=df['Forecast_1D_Ahead'].round(2)
#print(df[['Date','Sales_MA7','Forecast_1D_Ahead']].head(10))

#Forecast Error = Actual Sales − Forecast
df['Forecast_Error']=df['Sales']-df['Forecast_1D_Ahead']
#print(df[['Date','Sales','Forecast_1D_Ahead','Forecast_Error']].head(10))


#calculate:MAE&RMSE
eval_df = df.dropna(subset=['Sales', 'Forecast_1D_Ahead'])
errors = eval_df['Sales'] - eval_df['Forecast_1D_Ahead']
mae = errors.abs().mean()
rmse = np.sqrt((errors ** 2).mean())
#print(f"MAE:  {mae:.2f}")
#print(f"RMSE: {rmse:.2f}")


df['Sales_MA30'] = df['Sales'].rolling(window=30).mean()
df['Forecast_1D_Ahead_30'] = df['Sales_MA30'].shift(1)
comp_df = df.dropna(subset=['Sales', 'Forecast_1D_Ahead_30'])
errors = comp_df['Sales'] - comp_df['Forecast_1D_Ahead']
mae = errors.abs().mean()
rmse = np.sqrt((errors ** 2).mean())
#print(f"30 days MAE:  {mae:.2f}")
#print(f"30 days RMSE: {rmse:.2f}")

df['Abs_Error']=df['Forecast_Error'].abs()
print(df.sort_values('Abs_Error',ascending=False).head(10))

fig, axes = plt.subplots(2, 2, figsize=(12,8))

fig.suptitle(
        "Marketing Campaign Conversion",
        fontsize=20,
        fontweight="bold"
                                        )
kpi_style = {
        "boxstyle": "round,pad=0.8",
        "edgecolor": "gray",
        "facecolor": "white"
                                        }
def add_kpi_text(fig, x, y, label, value, kpi_style, fontsize=10):
    fig.text(
            x, y,
            f"{label}\n{value:,}",
            ha="center",
            va="center",
            fontsize=fontsize,
            fontweight="bold",
            bbox=kpi_style
            )

add_kpi_text(fig, 0.5, 0.9, "Total Sales", 125000, kpi_style)
add_kpi_text(fig, 0.5, 0.7, "Active Users", 8342, kpi_style, fontsize=12)

