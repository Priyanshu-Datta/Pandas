import pandas as pd

data ={
    "Name":["Ajay","Kishan","Priyanshu","Om","Aman"],
    "Age":[28,34,22,34,28],
    "Salary":[15000,40000,25000,35000,50000]
}

df = pd.DataFrame(data)

grouped = df.groupby("Age")["Salary"].sum()
print(grouped)