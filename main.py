"""
Main runner script for Credit Information Analysis assignment.
Executes coding tasks from src/ in sequence.
"""

import runpy
import os

def run_script(script_name):
    print(f"\n--- Running {script_name} ---")
    script_path = os.path.join("src", script_name)
    try:
        runpy.run_path(script_path, run_name="__main__")
    except Exception as e:
        print(f"Error while running {script_name}: {e}")

if __name__ == "__main__":
    # List of scripts to execute in order
    scripts = [
        "problem2_data_overview.py",
        "problem4_data_exploration.py"
    ]

    for script in scripts:
        run_script(script)

    print("\n All scripts executed successfully.")
