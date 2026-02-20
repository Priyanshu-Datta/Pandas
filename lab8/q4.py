import pandas as pd
data = {
    'Name': ['Amit', 'Riya', 'John'],
    'Age': [20, 21, 19],
    'Marks': [85, 90, 88]
}

df = pd.DataFrame(data)

print("First two rows:")
print(df.head(2))

print("\nLast row:")
print(df.tail(1))