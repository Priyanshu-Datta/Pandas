import pandas as pd

data ={
    "Name":["Ajay","Kishan","Priyanshu","Aman"],
    "Age":[28,34,22,34],
    "Salary":[10000,30000,20000,25000]
}

# sort in multiple column 
df = pd.DataFrame(data)
print("display in descending order")
df.sort_values(by=["Age","Salary"],ascending=[False,True],inplace=True)
print(df)