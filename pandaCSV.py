# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:07:20 2023

@author: grom_
"""

import pandas as pd
import datetime

# variablo donde vamos a guardar la fecha del dia de hoy 
fecha_actual = datetime.datetime.now()

# La fecha la agregamos con el formato en "ddmmaa"
fecha_formateada = fecha_actual.strftime("%d%m%y")

# Imprime la fecha formateada
print(fecha_formateada)


#//////////////////////////////////////////////////////////////////////////////

# Nombre del archivo de Excel de entrada
nombre_archivo_excel = 'Archivo_Excel/update_'+fecha_formateada+'.xlsx'  

# Nombre del archivo CSV de salida
nombre_archivo_csv = 'Archivo_Csv/update_'+fecha_formateada+'.csv'  

# Leer el archivo Excel
df = pd.read_excel(nombre_archivo_excel)

# Guardar el DataFrame como un archivo CSV UTF-8
df.to_csv(nombre_archivo_csv, index=False, encoding='utf-8')

print(f'Se ha convertido {nombre_archivo_excel} a {nombre_archivo_csv} en formato UTF-8.')