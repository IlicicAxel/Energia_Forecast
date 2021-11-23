### Pronóstico de consumo de energía eléctrica utilizando métodos automatizados de Machine Learning, el caso argentino.
Este repositorio de GitHub es presentado en conjunto con la tesis de grado, posee el código utilizado para el análisis y la construcción de los modelos.

Se desarrolla de la siguiente manera:

Utilizando el archivo "BASE.csv" y la notebook denominada "Energia_EDA.ipynb" se realiza un análisis de las series a utilizar, limpiando las mismas de outliers y datos nulos, dando como resultado el archivo llamado "BASEo.csv" que contiene la información relativa hasta septiembre 2021 y el archivo "oct.xlsx" que contiene la información de octubre 2021.

A continuación, se agregan los regresores analizados dando como resultado el archivo "BASEi.xlsx". Este archivo es utilizado como input para los modelos dentro de la carpeta "Modelos", para finalmente comparar el rendimiento de estos con la información dentro de "oct.xlsx" y los forecast de CAMMESA que se encuentran en "Forecast CAMMESA.csv".

Por último, se construyen dos archivos nuevos "Pronostico GBA.csv" y "Pronostico PBA.csv", junto con la notebook "Pronostico.ipynb", para comparar los pronósticos con los datos reales calculando los errores y elaborando visualizaciones.

Se incluyen también los códigos que fueron utilizados para obtener la información de la página de CAMMESA y del Servicio Meteorológico Nacional.

