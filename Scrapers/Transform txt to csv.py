import pandas as pd
import numpy as np

#Create list of dates from 20210901 to 20211031 in format YYYYMMDD using pandas
dates = pd.date_range('20210901', periods=61, freq='D')
#Fomat dates YYYYMMDD
dates = dates.strftime('%Y%m%d')

#Create empty pandas dataframe
MSN = pd.DataFrame()

for i in dates:
    #Read txt in "C:\Users\ilici\Documents\GitHub\SMN_forecast_20210901.txt" replacind \ with /
    df = pd.read_csv("C:/Users/ilici/Documents/GitHub/SMN_forecast_"+i+".txt", sep='\t', header=None)
    #tabulation
    df = df.drop(df.index[0:9])
    #export df as csv and replace if exists
    df.to_csv("C:/Users/ilici/Documents/GitHub/SMN_forecast_"+i+".csv", sep=' ', index=False)
    #read csv
    df = pd.read_csv("C:/Users/ilici/Documents/GitHub/SMN_forecast_"+i+".csv", sep=' ', header=None)
    df = df[0].str.split('  ', expand=True)
    df = df.drop(df.columns[[1,2,3]], axis=1)
    df = df.drop(df.columns[2:], axis=1)
    df = df.drop(df.index[9:])
    df1 = df[0].str.split(' ', expand=True)
    df = df.drop(df.index[0])
    df.columns = ['Date', 'SMN']
    df.Date = df.Date.str.replace('Hs.', '')
    #Concatenate to MSN
    MSN = pd.concat([MSN, df], axis=0)

#export MSN as excel and replace if exists
MSN.to_excel("C:/Users/ilici/Documents/GitHub/SMN_forecast.xlsx", index=False)





