data={
    "Name":["sarab","awais","saqib","haseeb","haris","ali"],
    "Age":[23,21,24,25,26,28],
    "Salary":[2300,3456,3246,8765,2345,6765],
    "Experience":[3,4,5,6,7,8]
}

import pandas as pd

df=pd.DataFrame(data)

print(df)

#ADD column 
df["Performance"] = ["Good","slightly Good","Bad","Very Good","Excellent","Good"]

print(df)

#Add columnby insertion method

df.insert(0,"ID",[23,32,43,23,22,32])
print(df)