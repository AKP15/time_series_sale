import numpy as np
import pandas as pd
df=pd.read_csv('data/cleaned.csv')
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


