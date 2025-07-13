import pandas as pd

data={
    "Name":["sarab","awais","saqib","haseeb","haris","ali"],
    "Age":[23,21,24,25,26,28],
    "Salary":[2300,3456,3246,8765,2345,6765],
    "Experience":[3,4,5,6,7,8]
}

df=pd.DataFrame(data)
print(df)

print("single column............")
print(df["Name"])
print("Multiple columns..............")

print(df[["Name","Age"]])


print("row operations")
print("single condtion..............")
high_sal=df[df["Salary"]>3500]
print(high_sal)

print("Multiple condition...............")

multuplecondyion=df[(df["Salary"]>3500)&(df["Experience"]>5)]
print(multuplecondyion)