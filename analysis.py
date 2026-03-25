import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

# convert date
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Year"] = df["Order Date"].dt.year

# total sales and profit
print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nTotal Profit:")
print(df["Profit"].sum())

# sales by category
category_sales = df.groupby("Category")["Sales"].sum()
print("\nSales by Category:")
print(category_sales)

# profit by category
category_profit = df.groupby("Category")["Profit"].sum()
print("\nProfit by Category:")
print(category_profit)

# sales by region
region_sales = df.groupby("Region")["Sales"].sum()
print("\nSales by Region:")
print(region_sales)

# profit by region
region_profit = df.groupby("Region")["Profit"].sum()
print("\nProfit by Region:")
print(region_profit)

# sales by year
year_sales = df.groupby("Year")["Sales"].sum()
print("\nSales by Year:")
print(year_sales)

# top 10 loss-making products
print("\nTop 10 Loss-Making Products:")
print(df.groupby("Product Name")["Profit"].sum().sort_values().head(10))

# average profit by discount
print("\nAverage Profit by Discount:")
print(df.groupby("Discount")["Profit"].mean())

# chart 1: sales by category
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_by_category_python.png")
plt.show()

# chart 2: profit by category
category_profit.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("profit_by_category_python.png")
plt.show()

# chart 3: sales by year
year_sales.plot(kind="line", marker="o")
plt.title("Sales by Year")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_by_year_python.png")
plt.show()

# chart 4: discount vs average profit
discount_profit = df.groupby("Discount")["Profit"].mean()
discount_profit.plot(kind="line", marker="o")
plt.title("Discount vs Average Profit")
plt.xlabel("Discount")
plt.ylabel("Average Profit")
plt.tight_layout()
plt.savefig("discount_vs_profit_python.png")
plt.show()
