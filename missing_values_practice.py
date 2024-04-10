import pandas as pd

# Clients' personal information of a company
data = {
    'Client Names': ['John', 'Emma', 'Lucas', 'Rachel', 'Chris', None],
    'Age': [24, None, 32, None, 41, 38],
    'Subscription Days': [365, 730, None, 1460, None, 200]
}
df = pd.DataFrame(data)

# Replacing the missing 'Age' values with their mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Replacing the missing 'Subscription Days' with 0
df['Subscription Days'] = df['Subscription Days'].fillna(0)

# Dropping any unfilled missing values, which are values with missing client names
df = df.dropna()

print(df)

client_info = {'Name': ['Alice', 'Bob', 'Chris', 'David'], 
               'Age': [30, None, 40, None],
               'Address': ['Street 1', 'Street 2', None, 'Street 4']}

data = pd.DataFrame(client_info)

# Fill missing values of Age column with median and missing values of Address column with "Unknown"
data['Age'] = data['Age'].fillna(data['Age'].median())
data['Address'] = data['Address'].fillna('Unknown')

print(data)

# Assume a client database where some client's age and job are missing.
clients = pd.DataFrame({
    'Name': ['John', 'Linda', 'Sam', 'Laura', 'Tom'],
    'Job': ['Engineer', 'Doctor', None, 'Lawyer', None],
    'Age': [30, None, 35, None, 50]
})

# TODO: Use the appropriate function to fill the missing values in the 'Age' column with the mean age.
clients['Age'] = clients['Age'].fillna(clients['Age'].mean())

# TODO: Similarly, use the appropriate function to fill the missing values in the 'Job' column with 'Unknown'.
clients['Job'] = clients['Job'].fillna('Unknown')

print(clients)

# A database of client details with some missing values
client_data = {
    'client_id': [1, 2, 3, None, 5],
    'age': [36, 22, None, 45, 31],
    'income': [45000, None, 60000, 75000, None]
}

# TODO: Convert the dictionary into a dataframe
df = pd.DataFrame(client_data)

# TODO: Identify the rows with missing values and print the result
print(df.isnull())

# TODO: Fill the missing values in 'age' with the mean age
df['age'] = df['age'].fillna(df['age'].mean())

# TODO: Fill the missing values in 'income' column with 0 
df['income'] = df['income'].fillna(0)

print(df)

# TODO: Drop any rows where any missing values remain after the previous steps
df = df.dropna()

# TODO: Print the updated dataframe
print(df)