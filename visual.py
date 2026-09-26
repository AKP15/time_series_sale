import matplotlib.pyplot as plt

plt.figure(figsize=(12,5))
plt.plot(df['Date'], df['Sales'], alpha=0.4, label='Daily Sales')
plt.plot(df['Date'], df['Sales_MA7'], color='red', label='7-Day MA')
plt.legend()
plt.title('Sales vs 7-Day Moving Average')
plt.show()

total_sales=df['Sales'].sum().round(2)
average_sales=df['Sales'].mean().round(2)
total_orders=df['Orders'].sum()
total_returns=df['Returns'].sum()

month_order = ['January','February','March','April','May','June','July','August','September','October','November','December']
df['Month'] = pd.Categorical(df['Date'].dt.month_name(),categories=month_order, ordered=True)
df['Year'] = df['Date'].dt.to_period('Y')
month_summary=df.groupby(['Year','Month']).agg(
                Total_Sale=('Sales','sum')).reset_index()
month_pivot=df.pivot_table(index='Month',columns='Year',values='Sales',aggfunc='sum')
month_pivot.columns = month_pivot.columns.astype(str)
print(month_summary.columns)
print(month_pivot.columns.tolist())
print(month_pivot.dtypes)

month_pivot['Avg_Sales']=(month_pivot['2023']+month_pivot['2024']+month_pivot['2025']/3).round(2)
month_pivot.columns = month_pivot.columns.astype(str)

month_summary['MoM_Growth_%'] = month_summary['Total_Sale'].pct_change() * 100
month_summary['MoM_Growth_%'] = month_summary['MoM_Growth_%'].round(2)
print(month_summary.columns)
month_summary['Month_Year'] = df['Date'].dt.strftime('%b-%Y')

fig, axes = plt.subplots(2, 3, figsize=(28, 16))
fig.suptitle(
            "Time Series Analysis",
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

add_kpi_text(fig, 0.08, 0.90, "Total Sales", total_sales, kpi_style, fontsize=25)
add_kpi_text(fig, 0.30, 0.90, "Average Daily Sales", average_sales, kpi_style, fontsize=25)
add_kpi_text(fig, 0.60, 0.90, "Total Orders", total_orders, kpi_style, fontsize=25)
add_kpi_text(fig, 0.98, 0.90, "Total Returns", total_returns, kpi_style, fontsize=25)

        # Row 0, Col 0
axes[0, 0].plot(df['Date'], df['Sales'])
axes[0, 0].plot(df['Date'], df['Sales_MA7'])
axes[0, 0].set_title("Sales Trend & 7-Day Moving Average")
axes[0, 0].set_xlabel("Time")
axes[0, 0].set_ylabel("Sales")

        # Row 0, Col 1
axes[0, 1].plot(month_pivot.index, month_pivot['2023'].values)
axes[0, 1].plot(month_pivot.index, month_pivot['2024'].values)
axes[0, 1].plot(month_pivot.index, month_pivot['2025'].values)
axes[0, 1].set_title("Monthly Sales Trend by Year")
axes[0, 1].set_xlabel("Month")
axes[0, 1].set_ylabel("Sales")

        # Row 0, Col 2
axes[0, 2].bar(month_pivot.index, month_pivot['Avg_Sales'].values)
axes[0, 2].set_title("Average Sales by Month — Seasonal Pattern")
axes[0, 2].set_xlabel("Month")
axes[0, 2].set_ylabel("Sales")

month_summary.columns=month_summary.columns.astype(str)
axes[1, 0].plot(month_summary['Month_Year'],month_summary['MoM_Growth_%'].values)
axes[1, 0].set_title("Monthly Sales Growth (MoM)")
axes[1, 0].set_xlabel("Month Year")
axes[1, 0].set_ylabel("MOM Growth")

        #Row 1, Col 1
axes[1, 1].plot(df['Date'], df['Sales'])
axes[1, 1].plot(df['Date'], df['Forecast_1D_Ahead'],color='red')
axes[1, 1].set_title("Actual Sales vs 1-Day-Ahead Forecast")
axes[1, 1].set_xlabel("Time")
axes[1, 1].set_ylabel("Sales")

plt.tight_layout(rect=[0, 0, 1, 0.84])
plt.show()

