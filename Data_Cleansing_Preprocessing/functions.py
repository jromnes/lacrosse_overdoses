import pandas as pd
from collections import Counter

def find_columns_with_ones(df):
    # Initialize an empty dictionary to store the results
    result = {}
    
    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Find the columns with a value of 1
        columns_with_one = tuple(sorted([col for col in df.columns if row[col] == 1.0]))
        
        # Store the result in the dictionary with ID as key
        result[index] = columns_with_one
    
    return result

def categorize_age(age):
    if age < 18:
        return 'Adolescent/Teenager'
    elif 18 <= age < 75:
        return 'Adult'
    else:
        return 'Senior'