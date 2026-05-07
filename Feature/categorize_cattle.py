import pandas as pd

# Load dataset
df = pd.read_csv(r"D:\cow-image-dataset\dataset.csv")

# Correct category ranges (matching your desired output)
def weight_category(weight):
    if weight < 200:
        return "VERY_LIGHT (< 200 kg)"
    elif 200 <= weight <= 229:
        return "LIGHT (200–229 kg)"
    elif 230 <= weight <= 259:
        return "MEDIUM (230–259 kg)"
    elif 260 <= weight <= 289:
        return "HEAVY (260–289 kg)"
    else:
        return "VERY_HEAVY (≥ 290 kg)"

# Apply category
df["weight_category"] = df["weight_in_kg"].apply(weight_category)

# Count categories
counts = df["weight_category"].value_counts()

# Define order
order = [
    "VERY_LIGHT (< 200 kg)",
    "LIGHT (200–229 kg)",
    "MEDIUM (230–259 kg)",
    "HEAVY (260–289 kg)",
    "VERY_HEAVY (≥ 290 kg)"
]

# Print in your desired format
print("\nWeight Category Distribution:\n")
for category in order:
    print(f"{category}: {counts.get(category, 0)}")

# Save file
df.to_csv("categorized_data.csv", index=False)