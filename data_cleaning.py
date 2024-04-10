import pandas as pd

data = {'A':[2, 4, None, 8],
        'B':[5, None, 7, 9],
        'C':[12, 13, 14, None]}
df = pd.DataFrame(data)

# Spot missing values
print(df.isnull())

'''Output:
       A      B      C
0  False  False  False
1  False   True  False
2   True  False  False
3  False  False   True
'''

# Fill missing values with 0
print(df.fillna(0)) 
'''Output:
     A    B     C
0  2.0  5.0  12.0
1  4.0  0.0  13.0
2  0.0  7.0  14.0
3  8.0  9.0   0.0
'''

# Remove rows with missing values
print(df.dropna()) 
'''Output:
     A    B     C
0  2.0  5.0  12.0
'''
# In the last example, all rows with None values were deleted, leaving us just one row. Note that both functions return a new DataFrame. If you want to update the original df, you'll need to re-assign it:

df = df.fillna(0)

# Handling Missing Values in One Column
# The df.fillna function applies to the whole dataset, which might not be the best strategy. Most of the time, you want to handle missing values in certain columns separately. It's simple! As DataFrame acts like a dictionary, we could access and re-assign separate columns using the key:

# Fill missing values of the "A" column with 0
df["A"] = df["A"].fillna(0)
print(df)
'''Output:
     A    B     C
0  2.0  5.0  12.0
1  4.0  NaN  13.0
2  0.0  7.0  14.0
3  8.0  9.0   NaN
'''