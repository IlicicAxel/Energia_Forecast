import pandas as pd

#Import "C:\Users\ilici\Documents\GitHub\SMN_forecast.xlsx" as dataframe replacing \ with /
df = pd.read_excel('C:/Users/ilici/Documents/GitHub/SMN_forecast.xlsx', sheet_name='Sheet1')
df.head()