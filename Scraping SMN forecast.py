#Import requests, pandas
import requests
import pandas as pd

#https://ssl.smn.gob.ar/dpd/descarga_opendata.php?file=pron5d/pron20211031.txt
#https://ssl.smn.gob.ar/dpd/descarga_opendata.php?file=pron5d/pron20211023.txt

#Create list of dates from 20210901 to 20211031 in format YYYYMMDD using pandas
dates = pd.date_range('20210901', periods=61, freq='D')
#Fomat dates YYYYMMDD
dates = dates.strftime('%Y%m%d')
#show dates
print(dates)


#request data from SMN
for date in dates:
    #Create URL
    url = 'https://ssl.smn.gob.ar/dpd/descarga_opendata.php?file=pron5d/pron' + date + '.txt'
    #print(url)
    #Request data from URL
    response = requests.get(url)
    #Save data to file
    with open('SMN_forecast_' + date + '.txt', 'wb') as f:
        f.write(response.content)

