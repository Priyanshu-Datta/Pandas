import pandas as pd
df = pd.read_csv("students.csv")

print("First 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns)

print("\nLast 3 rows:")
print(df.tail(3))

print("\nShape of DataFrame:")
print(df.shape)

print("\nData types:")
print(df.dtypes)