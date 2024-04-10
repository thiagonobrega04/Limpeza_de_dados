# Real-World Implications
# In the real world, missing values are expected. Whether it's a company's financial data or a hospital's patient medical records, missing values exist and must be appropriately addressed, as they significantly influence the results of our analysis. A common way to fill in missing values is to use mean value. Let's consider a simple example where some values of the age column are missing:

import pandas as pd
import numpy as np

# Creating a simple dataframe
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, np.nan, 35, np.nan, 45]
})

# Filling missing values with mean
mean_age = df['age'].mean()  # 35
df = df['age'].fillna(mean_age)

print(df)
'''Output:
0    25.0
1    35.0
2    35.0
3    35.0
4    45.0
'''

# In the above example, we first create a dataframe with names and ages, where some age values are missing (represented as np.nan in the dataframe). To fill the missing age values with the mean age, we use the fillna() function with df['age'].mean() as the argument. Luckily, df['age'].mean() doesn't consider missing values – hence, it works correctly without any workarounds.

# When we print out the resulting dataframe, we see that missing values are replaced with 35 – the mean age.