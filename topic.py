import pandas as pd 

data ={
    "Name":["Ram","Shyam","jadu","madhu","Rahul","Ranit","Priyanshu","sanchari"],
    "Age": [28,31,32,56,45,34,21,20],
    "Salary":[30000,40000,50000,34000,45000,53000,70000,60000],
    "performance Score":[85,87,91,78,80,88,95,96]
}

df = pd.DataFrame(data)

print(df)
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns}")