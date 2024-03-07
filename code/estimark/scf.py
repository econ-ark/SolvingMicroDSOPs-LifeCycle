"""Sets up the SCF data for use in the EstimatingMicroDSOPs estimation.
"""

from pathlib import Path

import pandas as pd

from estimark.parameters import final_age_data, initial_age, remove_ages_from_scf

# Get the directory containing the current file and construct the full path to the CSV file
csv_file_path = Path(__file__).resolve().parent / ".." / "data" / "SCFdata.csv"

# Define the variables to keep
keep_vars = ["age", "age_group", "wealth_income_ratio", "weight"]

# Read the CSV file and filter data in one step
scf_data = pd.read_csv(csv_file_path)
scf_data = scf_data.loc[
    (scf_data.norminc > 0.0)
    & (scf_data.age > initial_age)
    & (scf_data.age <= final_age_data)
    & (~scf_data.age.isin(remove_ages_from_scf)),
    keep_vars,
]
