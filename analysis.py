import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

# show first rows
print(df.head())

# total sales
print("\nTotal Sales:")
print(df["Sales"].sum())

# sales by category
category_sales = df.groupby("Category")["Sales"].sum()
print("\nSales by Category:")
print(category_sales)

# sales by region
region_sales = df.groupby("Region")["Sales"].sum()
print("\nSales by Region:")
print(region_sales)

# convert date
df["Order Date"] = pd.to_datetime(df["Order Date"])

# sales by year
df["Year"] = df["Order Date"].dt.year
year_sales = df.groupby("Year")["Sales"].sum()
print("\nSales by Year:")
print(year_sales)

# chart 1: sales by category
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_by_category_python.png")
plt.show()

# chart 2: sales by year
year_sales.plot(kind="line", marker="o")
plt.title("Sales by Year")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_by_year_python.png")
plt.show()