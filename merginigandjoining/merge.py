import pandas as pd

data1={
    "Customer_ID":[1,2,3,4],
    "Name":["Aasm","Haider","Ali","Awias"]
}

data2={
    "Customer_ID":[1,2,5],
    "Sales":[2,3,4]
}

df=pd.DataFrame(data1)
df1=pd.DataFrame(data2)
print("Inner joint")
merge=pd.merge(df,df1,on="Customer_ID",how="inner")
print(merge)
print("Outer  joint")
merge1=pd.merge(df,df1,on="Customer_ID",how="outer")
print(merge1)
print("left joint")
merge2=pd.merge(df,df1,on="Customer_ID",how="left")
print(merge2)
print("Right joint")
merge3=pd.merge(df,df1,on="Customer_ID",how="right")
print(merge3)
print("Cross joint")
merge4=pd.merge(df,df1,how="cross")
print(merge4)