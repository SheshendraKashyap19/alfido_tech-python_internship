import pandas as pd

# Load CSV file
df = pd.read_csv(r"task 3 data analysis/employees.csv")

print("----- Dataset -----")
print(df)

print("\n----- First 5 Rows -----")
print(df.head())

print("\n----- Missing Values -----")
print(df.isnull().sum())

print("\n----- Employees with Salary > 50000 -----")
print(df[df["Salary"] > 50000])

print("\n----- Average Salary by Department -----")
print(df.groupby("Department")["Salary"].mean())