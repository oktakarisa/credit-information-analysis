import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import io

# Load dataset
df = pd.read_csv("data/application_train.csv")

# Peek at data
head_data = df.head().to_markdown()

# Capture df.info() output
buffer = io.StringIO()
df.info(buf=buffer)
info_text = buffer.getvalue()

# Describe data
describe_data = df.describe().to_markdown()

# Missing values
missing_values = df.isnull().sum().reset_index()
missing_values.columns = ["Column", "MissingCount"]
missing_values.to_csv("reports/problem2_missing_values.csv", index=False)

# Target distribution
target_counts = df["TARGET"].value_counts(normalize=True) * 100
plt.figure(figsize=(6,4))
target_counts.plot(kind="bar")
plt.title("Target Variable Distribution (0 = No Default, 1 = Default)")
plt.ylabel("Percentage")
plt.savefig("plots/problem2_target_distribution.png", bbox_inches="tight")

# Write markdown report
with open("reports/problem2_summary.md", "w") as f:
    f.write("# Problem 2 – Data Overview\n\n")

    f.write("## Head of Data\n")
    f.write(head_data + "\n\n")

    f.write("## Info\n")
    f.write("```\n" + info_text + "\n```\n\n")

    f.write("## Describe\n")
    f.write(describe_data + "\n\n")

    f.write("## Missing Values\n")
    f.write("See: `reports/problem2_missing_values.csv`\n\n")

    f.write("## Target Distribution\n")
    f.write("![Target Distribution](../plots/problem2_target_distribution.png)\n\n")

    f.write("### Interpretation\n")
    f.write("- **Head**: Shows first 5 rows, useful for sanity-checking columns.\n")
    f.write("- **Info**: Reveals number of non-null values and datatypes.\n")
    f.write("- **Describe**: Provides summary stats for numeric columns.\n")
    f.write("- **Missing Values**: Highlights columns requiring cleaning/imputation.\n")
    f.write("- **Target Distribution**: The dataset is imbalanced (far more 0 than 1).\n")

print(" Problem 2 report saved to: reports/problem2_summary.md")
print(" Plot saved to: plots/problem2_target_distribution.png")
