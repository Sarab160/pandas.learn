import pandas as pd

data={
    "Name":["sarab","awais","saqib","haseeb","haris","ali"],
    "Age":[23,21,24,25,26,28],
    "Salary":[2300,3456,3246,8765,2345,6765],
    "Experience":[3,4,5,6,7,8]
}

df = pd.DataFrame(data)

print(df.shape)
print(df.columns)
print(type(df))