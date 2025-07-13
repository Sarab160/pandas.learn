import pandas as pd 

data={
    "Name":["sarab","Awais","Umer"],
    "Age":[23,34,21],
    "School":["Public","private school","Republic"]
}

df=pd.DataFrame(data)

df.to_csv("output.csv",index=False)
df.to_excel("output.xlsx",index=False)
df.to_json("output.json",index=False)


print("done")