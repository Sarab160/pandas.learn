data={
    "Name":["sarab",None,"awais","saqib","haseeb","haris","ali"],
    "Age":[23,None,21,24,25,26,28],
    "Salary":[2300,None,3456,3246,8765,2345,6765],
    "Experience":[3,None,4,5,6,7,8]
}
import pandas as pd

df=pd.DataFrame(data)
df.fillna({"Name": "Rafique"}, inplace=True)
df.fillna({"Age":21},inplace=True)
df.fillna({"Salary":3450},inplace=True)
df.fillna({"Experience":3},inplace=True)
print(df)