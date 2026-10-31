import pandas as pd

# Load the raw sales dataset
df = pd.read_csv("Task_02_Raw_Sales_Dataset.csv")

# Standardize text fields
for col in ["Region", "Category", "Sub-Category"]:
    df[col] = df[col].astype("string").str.strip().str.title()

# Convert columns to correct data types
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
for col in ["Sales", "Profit", "Quantity", "Discount"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove exact duplicate records
df = df.drop_duplicates()

# Handle missing values
df["Region"] = df["Region"].fillna(df["Region"].mode().iloc[0])
df["Sales"] = df["Sales"].fillna(df["Sales"].median())
df["Profit"] = df["Profit"].fillna(df["Profit"].median())
df["Discount"] = df["Discount"].fillna(df["Discount"].median())

# Remove records with invalid essential fields
df = df.dropna(subset=["Order Date", "Category", "Sub-Category", "Quantity"])

# Save cleaned dataset
df.to_csv("Task_02_Cleaned_Sales_Dataset.csv", index=False)

print("Rows after cleaning:", len(df))
print("Missing values remaining:", int(df.isna().sum().sum()))
print("Cleaned file saved successfully.")
