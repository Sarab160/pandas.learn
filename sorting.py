data={
    "Name":["sarab","awais","saqib","haseeb","haris","ali"],
    "Age":[23,21,24,25,26,28],
    "Salary":[2300,3456,3246,8765,2345,6765],
    "Experience":[3,4,5,6,7,8]
}
import pandas as pd
df=pd.DataFrame(data)
print("Before")
print(df)
df.sort_values(by="Age",ascending=True,inplace=True)
print("After")
print(df)