#!/usr/bin/python
import csv
import json
import pandas as pd 

filename = 'file/path/directory'

def XLSX_TO_CSV(filename): 
    # SECTION TO CONVERT XLSX TO CSV
    xlsxName = filename.split('.')
    csvFile = "{0}.csv".format(xlsxName[0])
    read_file = pd.read_excel(filename, skiprows=1)
    read_file.to_csv(csvFile, index=None, header=True)
    print('File xlsx renamed to {0}'.format(csvFile))

    # SECTION TO CONVERT CSV TO JSON
    f = open('ATMS.csv', encoding="utf8")
    ids = (csv.reader(f)).__next__()
    reader = csv.DictReader(f, fieldnames=(ids))
    out = json.dumps([row for row in reader])
    print("json parsed")
    f = open('ATMS.json', 'w')
    f.write(out)
    print('json saved!')

XLSX_TO_CSV(filename)