import pandas as pd

data = {
    'Name': ['Amit', 'Riya', 'John'],
    'Age': [20, 21, 19],
    'Marks': [85, 90, 88]
}

df = pd.DataFrame(data)


def grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    else:
        return 'C'


df['Grade'] = df['Marks'].apply(grade)

print(df[['Name', 'Marks', 'Grade']])