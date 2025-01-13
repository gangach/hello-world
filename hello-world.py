import pandas as pd

print("hello world")
# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Select a value from an index in the DataFrame
value = df.loc[1, 'Name']
print(value)