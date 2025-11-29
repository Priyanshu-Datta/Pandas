import pandas as pd

data = {
    "mane":['ram','shyam','jadu'],
    "age": [10,20,30],
    "city":['kolkata','mumbai','delhi']
}

df = pd.DataFrame(data)
print(df)

df.to_csv("output.csv" , index=False)
df.to_excel("output2.xlsx" , index=False)
df.to_json("output2.json" , index=False)
