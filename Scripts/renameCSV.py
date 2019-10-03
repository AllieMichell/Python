#!/usr/bin/python

import os
import sys
import openpyxl
from xlsx2csv import Xlsx2csv

"""
NOTA EN LA VARIABLE DONDE DICE directory PONES LA RUTA EN DONDE SE ENCUENTRAN LOS 
EXCELES 
"""
directory = 'C:/Users/user/Documents/Projects/Python/Files'
def convertXLSXtoCSV(directory):
    """
    ES UNA FUNCIÓN QUE SIRVE PARA CONVERTIR EXCELES EN ARCHIVOS CSV
    PARAMETROS:
    -----------
        directory: Ruta de los archivos a convertir
    """
    os.chdir(directory)
    files = os.listdir()
    for i in range(len(files)):
        nameFile = files[i]
        nameF = nameFile.split('.xlsx')
        name = nameF[0]
        Xlsx2csv(nameFile, outputencoding="utf-8").convert('{0}.csv'.format(name))
        """
        NOTA SI QUIERES QUE SE ELIMINEN LOS ARCHIVOS XLSX DESPUES DE CONVERTIRLOS A 
        CSV QUITALE EL # AL RENGON DE ABAJO os.remove(files[i])
        """
        #os.remove(files[i])

"""
PARA EJECUTAR LA FUNCIÓN QUE SE CREO ALLÁ ARRIBA ESCRIBES EL NOMBRE QUE SE LE ASIGNO 
EN ESTE CASO ES convertXLSXtoCSV(directory) Y EN LOS PARENTESIS COLOCAS LA BARIABLE QUE
TIENE LA RUTA EN DONDE ESTAN LOS ARCHIVOS A CAMBIAR
"""        
convertXLSXtoCSV(directory)