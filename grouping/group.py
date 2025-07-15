import pandas as pd

data={
    "Name":["sarab","awais","saqib","haseeb","haris","ali"],
    "Age":[23,26,24,25,26,25],
    "Salary":[2300,3456,3246,8765,2345,6765],
    "Experience":[3,4,3,6,3,4]
}

df=pd.DataFrame(data)
print("Grouping with respect to the age")
group=df.groupby(["Age"])["Salary"].sum()
print(group)

print("Grouping for multiple on basis")
mul_group=df.groupby(["Age","Experience"])["Salary"].min()

print(mul_group)