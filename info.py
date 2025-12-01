import pandas as pd 

# df = pd.read_excel("SampleSuperstore.xlsx")
df = pd.read_json("sample_Data.json")


print("display the info of the dataset")
print(df.info())