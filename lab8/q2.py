import pandas as pd 

s = pd.Series(range(1, 11))

even_numbers = s[s % 2 == 0]
print(even_numbers)