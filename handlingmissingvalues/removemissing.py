import pandas as pd

data={
    "Name":["sarab",None,"awais","saqib","haseeb","haris","ali"],
    "Age":[23,None,21,24,25,26,28],
    "Salary":[2300,None,3456,3246,8765,2345,6765],
    "Experience":[3,None,4,5,6,7,8]
}
df=pd.DataFrame(data)
print("Befor delete")
print(df)
print("After delete")
df.dropna(inplace=True)

print(df)