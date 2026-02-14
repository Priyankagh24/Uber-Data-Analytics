import pandas as pd

# Load CSV file
df = pd.read_csv("data/uber_data.csv")

print("Original shape:", df.shape)

# Remove null rows
df = df.dropna()

print("After cleaning:", df.shape)

# Create total_amount column if missing
if "total_amount" not in df.columns:
    if "fare_amount" in df.columns and "tip_amount" in df.columns:
        df["total_amount"] = df["fare_amount"] + df["tip_amount"]

# Save cleaned file
df.to_csv("cleaned_uber_data.csv", index=False)

print("✅ Cleaned file created successfully.")