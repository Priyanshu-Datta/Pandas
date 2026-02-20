import pandas as pd
s = pd.Series([10, 60, 30, 80, 45, 29, 50, 103, 49])

s[s > 50] = 50
print(s)