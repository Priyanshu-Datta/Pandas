import pandas as pd

data ={
    "Name":["Ajay","Kishan","Priyanshu"],
    "Age":[28,34,22],
    "Salary":[10000,30000,20000]
}

# sort in one column 
df = pd.DataFrame(data)
print("display in descending order")
df.sort_values(by="Age",ascending=False,inplace=True)
print(df)

print("display in ascending order")
df.sort_values(by="Age",ascending=True,inplace=True)
print(df)
