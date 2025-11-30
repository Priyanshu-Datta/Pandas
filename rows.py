import pandas as pd 

df = pd.read_csv('sales_data_sample.csv',encoding="latin1")

print("display first 5 rows")
print(df.head())

print("display last 5 rows")
print(df.tail())

print("display first 3 rows")
print(df.head(3))

print("display last 3 rows")
print(df.tail(3))
