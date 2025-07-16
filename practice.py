import pandas as pd

df=pd.read_excel("SampleSuperstore.xlsx")

print(df)

print(df.head(5))
print(df.tail(5))

print(df.info())

print(df.describe())

print(df.shape)
print(df.columns)

print(df[["Order ID","Row ID"]])

discount=df[df["Discount"]>0.20]
print(discount)

discount_2=df[(df["Sales"]<71)&(df["Discount"]<0.42)]
print(discount_2)
print(discount_2.shape)

