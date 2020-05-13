import pandas as pd

customer = pd.read_csv(r'..\Data\CustomerFile4.csv')
# print(customer)
# Simple Sum
output = customer['Spend'].sum()
# print(output)

# Overall Min and Max
customer['group'] = '0'
output = customer.groupby('group').agg({'JoinDate':['min','max']})

# count
output = customer['Spend'].count()

# Group By
output = customer.City.unique()
#       or
output = customer.groupby('City')\
    .agg({'group':'count'})\
    .reset_index()\
    .drop('group', axis=1)

# Group By and Count
output = customer.groupby('City')\
    .agg({'group':'count'}) \
    .reset_index() \
    .rename({'group':'Count'}, axis=1)

# Concatenate
#       need info here

# Basic Math
output = customer.groupby(['State','City'])\
    .agg({'Visits':'mean','Spend':'sum'}) \
    .reset_index() \
    .rename({'Visits':'Median_Visits','Spend':'Sum_Spend'}, axis=1)

# Spatial Summarizing
#       need info here

# First and Last in a column
#       need info here

# Advanced Math
output = customer.groupby('group').agg({'Spend':['mean','median','std','var']})
# not sure of mode here...

# String Summarizing
#       need info here

print(output)
# print(customer)