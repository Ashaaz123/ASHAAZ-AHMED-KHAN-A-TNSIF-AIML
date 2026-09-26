import pandas as pd

data = {
    "Product Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Accessories"],
    "Price": [50000, 800, 1500, 12000, 2000],
    "Quantity Sold": [10, 75, 60, 25, 55]
}

df = pd.DataFrame(data)

df["Total Sales"] = df["Price"] * df["Quantity Sold"]

print("Product Data:")
print(df)

print("\nProduct with highest sales:")
print(df.loc[df["Total Sales"].idxmax()])

print("\nAverage product price:")
print(df["Price"].mean())
print("\nProducts with quantity sold greater than 50:")
print(df[df["Quantity Sold"] > 50])

print("\nProducts sorted based on total sales:")
print(df.sort_values("Total Sales", ascending=False))