import pandas as pd

df=pd.read_excel("SampleSuperstore.xlsx")

print("First 10 rows")

print(df.head(10))

print("last 10 rows")

print(df.tail(10))