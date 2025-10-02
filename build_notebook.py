import nbformat as nbf
import os

# Create a new notebook
nb = nbf.v4.new_notebook()
cells = []

def add_markdown_from_file(filepath, title=None):
    if os.path.exists(filepath):
        if title:
            cells.append(nbf.v4.new_markdown_cell(f"# {title}"))
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
        cells.append(nbf.v4.new_markdown_cell(text))

def add_image_cell(image_path, title=None):
    if os.path.exists(image_path):
        md = ""
        if title:
            md += f"### {title}\n"
        md += f"![{os.path.basename(image_path)}]({image_path})"
        cells.append(nbf.v4.new_markdown_cell(md))

# Problem 1
add_markdown_from_file("reports/problem1_understanding.md", "Problem 1 – Understanding")

# Problem 2
add_markdown_from_file("reports/problem2_summary.md", "Problem 2 – Data Overview")
cells.append(nbf.v4.new_code_cell("import src.problem2_data_overview as p2"))
add_image_cell("plots/problem2_target_distribution.png", "Target Distribution")

# Problem 3
add_markdown_from_file("reports/problem3_define_issues.md", "Problem 3 – Defining Issues")
add_markdown_from_file("reports/problem3_questions.csv")

# Problem 4
add_markdown_from_file("reports/problem4_findings.md", "Problem 4 – Data Exploration")
cells.append(nbf.v4.new_code_cell("import src.problem4_data_exploration as p4"))
add_image_cell("plots/problem4_age_vs_default.png", "Age vs Default")
add_image_cell("plots/problem4_income_vs_target.png", "Income vs Target")
add_image_cell("plots/problem4_contract_vs_default.png", "Contract Type vs Default")
add_image_cell("plots/problem4_corr_heatmap.png", "Correlation Heatmap")
add_image_cell("plots/problem4_credit_vs_target.png", "Credit Amount vs Target")

# Problem 5
add_markdown_from_file("reports/problem5_reflection.md", "Problem 5 – Reflection")

cells.append(nbf.v4.new_markdown_cell(
    "This notebook combines reports, code, and plots from the Credit Information Analysis project."
))

# Assign cells
nb['cells'] = cells

# Ensure UTF-8 write
os.makedirs("notebooks", exist_ok=True)
with open("notebooks/credit_eda.ipynb", "w", encoding="utf-8") as f:
    nbf.write(nb, f)

print("✅ Notebook created at notebooks/credit_eda.ipynb (UTF-8 encoded).")
