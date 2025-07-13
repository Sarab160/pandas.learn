import pandas as pd

print("Information about the data")

df=pd.read_excel("SampleSuperstore.xlsx")

print(df.info())

print("describe function which give the descriptive statistics of data ")

data={
    "Name":["sarab","awais","saqib","haseeb","haris","ali"],
    "Age":[23,21,24,25,26,28],
    "Salary":[2300,3456,3246,8765,2345,6765],
    "Experience":[3,4,5,6,7,8]
}

df1=pd.DataFrame(data)
print(df1)
print(df1.describe())