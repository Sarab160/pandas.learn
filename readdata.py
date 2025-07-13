
import pandas as pd

#pd.set_option("display.max_columns", None)
df =pd.read_csv("sales_data_sample.csv",encoding="latin1")

print(df)

print("json data")

df1=pd.read_json("sample_Data.json")
print(df1)

print("Excel data")

df3=pd.read_excel("SampleSuperstore.xlsx")
print(df3)