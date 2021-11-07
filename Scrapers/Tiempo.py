import requests
import pandas as pd

#Create list of dates from 20210901 to 20211031 in format YYYYMMDD using pandas
dates = pd.date_range('20210801', periods=61, freq='D')
#Fomat dates YYYYMMDD
dates = dates.strftime('%Y%m%d')


#Cambiar PATH del excel con la lista de los PDF hash	
#df = pd.read_excel('C:/Users/ilici/OneDrive - Facultad de Cs Económicas - UBA/Facultad/Tesis/Tiempo.xls')
#link = df['STR'].tolist()
#Nombre = df['STR'].tolist()

for i in dates:
        
        server_endpoint = "https://ssl.smn.gob.ar/dpd/descarga_opendata.php?file=observaciones/datohorario"+str(i)+".txt"
        #PATH de guardado
        local_file_path = "C:/Users/ilici/OneDrive - Facultad de Cs Económicas - UBA/Facultad/Tesis/"+str(i)+".csv"
        
        def download_file_from_server_endpoint(server_endpoint, local_file_path):

            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36", "Referer" :"https://www.boletinoficial.gob.ar/seccion/tercera"}
        # Send HTTP GET request to server and attempt to receive a response
            response = requests.get(url=server_endpoint, headers=headers)

        # If the HTTP GET request can be served
            if response.status_code == 200:

            # Write the file contents in the response to a file specified by local_file_path
                with open(local_file_path, 'wb') as local_file:
                   for chunk in response.iter_content(chunk_size=128):
                        local_file.write(chunk)

        download_file_from_server_endpoint(server_endpoint, local_file_path)