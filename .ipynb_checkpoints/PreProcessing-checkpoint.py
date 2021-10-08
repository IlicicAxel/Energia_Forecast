# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 20:39:34 2021

@author: ilici
"""

import pandas as pd
series = pd.read_csv("C:/Users/ilici/OneDrive - Facultad de Cs Económicas - UBA/Facultad/Tesis/Bases/BSAS.csv", header = 0, parse_dates = [0], names = ['Fecha','Tipo dia', 'Consumo', 'Temperatura'], index_col = 0)

editedser = series.interpolate(method="linear", limit_direction ='forward')

editedser.to_csv("C:/Users/ilici/OneDrive - Facultad de Cs Económicas - UBA/Facultad/Tesis/Bases/BSASok.csv")