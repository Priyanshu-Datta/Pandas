import pandas as pd

data ={
    "Name":["Ajay","Kishan","Priyanshu"],
    "Age":[28,34,22],
    "Salary":[10000,30000,20000]
}

# using aggregate mehods 
df = pd.DataFrame(data)
print("mean of Salary: ",df["Salary"].mean())
print("sum of Salary: ",df["Salary"].sum())
print("min of Salary: ",df["Salary"].min())
print("max of Salary: ",df["Salary"].max())