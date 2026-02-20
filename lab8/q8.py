import pandas as pd

df = pd.read_csv("students.csv")

df.to_excel("students.xlsx", index=False)

df.to_json("students.json", orient='records')

print("CSV converted to Excel and JSON successfully")