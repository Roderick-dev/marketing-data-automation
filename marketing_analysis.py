"""
Marketing Data Automation Tool
Author: Your Name
Description:
    This script loads marketing campaign data from a CSV file,
    cleans it, analyzes ROI by channel, and creates a visualization.
    It also saves a summary report for further use.
"""

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load Data
# -----------------------------
try:
    data = pd.read_csv("marketing_data.csv")
    print("✅ Data loaded successfully!")
except FileNotFoundError:
    print("❌ Error: marketing_data.csv not found. Please place it in the same folder.")
    exit()

# -----------------------------
# 2. Basic Cleaning
# -----------------------------
# Drop rows with missing values
data.dropna(inplace=True)

# Convert date column (if exists)
if "Date" in data.columns:
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")

print(f"✅ Cleaned dataset contains {len(data)} rows.")

# -----------------------------
# 3. Calculate ROI
# -----------------------------
# ROI = (Revenue - Spend) / Spend
data["ROI"] = (data["Revenue"] - data["Spend"]) / data["Spend"]

# -----------------------------
# 4. Group by Channel
# -----------------------------
summary = data.groupby("Channel").agg({
    "Spend": "sum",
    "Revenue": "sum",
    "Clicks": "sum",
    "ROI": "mean"
}).reset_index()

print("\n📊 Marketing Summary by Channel:")
print(summary)

# -----------------------------
# 5. Visualization
# -----------------------------
plt.figure(figsize=(8,5))
plt.bar(summary["Channel"], summary["ROI"], color="skyblue")
plt.title("Average ROI by Marketing Channel")
plt.xlabel("Channel")
plt.ylabel("ROI")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("roi_by_channel.png")
plt.show()

print("✅ Visualization saved as roi_by_channel.png")

# -----------------------------
# 6. Save Summary
# -----------------------------
summary.to_csv("marketing_summary.csv", index=False)
print("✅ Summary exported to marketing_summary.csv")
