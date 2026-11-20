import pandas as pd
df=pd.read_csv("xyz.csv",na_values=["N/A", "NULL", "null"])

print("orginal Dataset:")
print(df.head())

df["Customer"]=df["Customer"].str.strip().str.title()
df["Customer"]=df["Customer"].replace("",pd.NA)

df["City"] = df["City"].str.strip().str.title()

df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

df.loc[df["Age"] < 18, "Age"] = pd.NA

df["Age"] = df["Age"].fillna(df["Age"].median())

df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df.loc[df["Quantity"] < 1, "Quantity"] = pd.NA
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())

df["Product"]=df["Product"].str.strip().str.title()

df["Category"]=df["Category"].str.strip().str.title()

df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce")
df["Discount"] = df["Discount"].fillna(0)

df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
df["Rating"] = df["Rating"].fillna(df["Rating"].median())

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"], errors="coerce"
)

print("\nCleaned Dataset:")
print(df)

print(df)

df.to_csv("cleaned_orders.csv", index=False)

print("\nCleaned dataset saved successfully!")

