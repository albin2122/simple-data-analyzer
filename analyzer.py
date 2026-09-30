import pandas as pd

data = pd.read_csv("students.csv")

print("Number of students:", len(data))
print("Average mark:", data["mark"].mean())
print("Highest mark:", data["mark"].max())
print("Lowest mark:", data["mark"].min())

passed = (data["mark"] >= 40).sum()
failed = (data["mark"] < 40).sum()

print("Passed:", passed)
print("Failed:", failed)


print("Student Data Analysis")