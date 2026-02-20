import pandas as pd
data = {
    'Name': ['Aman', 'Bhavya', 'Chamline', 'Drishti'],
    'Math': [80, 75, 90, 85],
    'Science': [70, 88, 92, 60]
}

df = pd.DataFrame(data)

df['Total'] = df['Math'] + df['Science']

df_sorted = df.sort_values(by='Math', ascending=False)
print("Sorted by Math marks:")
print(df_sorted)

filtered_df = df[df['Science'] > 80]
print("\nStudents with Science marks > 80:")
print(filtered_df)