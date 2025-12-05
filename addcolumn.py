import pandas as pd 

data ={
    "Name":["Ram","Shyam","jadu","madhu","Rahul","Ranit","Priyanshu","sanchari"],
    "Age": [28,31,32,56,45,34,21,20],
    "Salary":[30000,40000,50000,34000,45000,53000,70000,60000],
    "performance Score":[85,87,91,78,80,88,95,96]
}

df = pd.DataFrame(data)
print("Sample Dtaframe")
print(df)

# add new bonus column 
df["Bonus"] = df["Salary"] * 0.1 
print("new data")
print(df)

# using insert() method 
df.insert(0,"Employee Id", [100,700,300,400,500,600,200,800])
print(df)
