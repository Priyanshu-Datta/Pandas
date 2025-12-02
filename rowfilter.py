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

# single row filtering 
high_salary = df[df["Salary"]>50000]

print("High salary employees")
print(high_salary)

# multiple row filtering 

age_salary = df[(df["Age"]>30) & (df["Salary"]>50000)]
print("Display whos salary is greater than 50000 and age is greater than 30")
print(age_salary)

# using or condition 

or_filter = df[(df["Age"]>30) | (df["performance Score"]>80)]
print("Display whos performance Score is greater than 80 and age is greater than 30")
print(or_filter)