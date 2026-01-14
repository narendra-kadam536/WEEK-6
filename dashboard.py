import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import os

# Create folder
os.makedirs("visualizations", exist_ok=True)

# Load data
df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

sns.set_theme(style="whitegrid", palette="Set2")

# 1️⃣ Sales Trend (Line Plot)
daily_sales = df.groupby("Date")["Total_Sales"].sum().reset_index()

plt.figure(figsize=(8,5))
sns.lineplot(data=daily_sales, x="Date", y="Total_Sales", marker="o")
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.savefig("visualizations/sales_trend.png", dpi=300)
plt.close()

# 2️⃣ Product Performance (Bar Plot)
plt.figure(figsize=(8,5))
sns.barplot(x="Product", y="Total_Sales", data=df, estimator=sum)
plt.title("Total Sales by Product")
plt.savefig("visualizations/product_sales.png", dpi=300)
plt.close()

# 3️⃣ Regional Sales Distribution (Box Plot)
plt.figure(figsize=(8,5))
sns.boxplot(x="Region", y="Total_Sales", data=df)
plt.title("Sales Distribution by Region")
plt.savefig("visualizations/region_boxplot.png", dpi=300)
plt.close()

# 4️⃣ Correlation Heatmap
plt.figure(figsize=(6,5))
corr = df[["Quantity", "Price", "Total_Sales"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("visualizations/correlation_heatmap.png", dpi=300)
plt.close()

# 5️⃣ Interactive Plot (Plotly)
fig = px.scatter(
    df,
    x="Price",
    y="Total_Sales",
    color="Product",
    size="Quantity",
    hover_data=["Region", "Customer_ID"],
    title="Interactive Product Sales Analysis"
)
fig.show()
