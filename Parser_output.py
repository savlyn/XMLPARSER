
import numpy as np
import pandas as pd
import xml.etree.cElementTree as et
import os
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows

script_path = os.path.abspath(__file__) 
print(script_path)
script_dir = os.path.split(script_path)[0] 
rel_path = "data/003.xml"
abs_file_path = os.path.join(script_dir, rel_path)


## writing to excel
def savetoexcel(df, filename, sheet):
    if os.path.exists(filename):
        workbook=openpyxl.load_workbook(filename)
        if sheet in workbook.sheetnames:
            active_sheet=workbook[sheet]
            for row in dataframe_to_rows(df,header=False, index=False):
                active_sheet.append(row)
        else:

            workbook.create_sheet(sheet)
            active_sheet=workbook[sheet]

            for row in dataframe_to_rows(df, index=False):
                active_sheet.append(row)
        
        workbook.save(filename)
    
    
        print('DataFrame is written successfully to Excel File.')

    else:
        with pd.ExcelWriter(filename, engine='openpyxl',mode='w') as writer:
            
            
            # write dataframe to excel
            df.to_excel(writer,sheet_name=sheet, index=False) 
            # save the excel
            writer.save()
            
            print('DataFrame is written successfully to Excel File.')


## Parsing through the tree node to get data objects

datalist=['./DataExtract900jer/Messages','./DataExtract900jer/Rules','./Nuula/Errors']
tree=et.parse( abs_file_path)
root=tree.getroot()
count=1
for i in datalist:
    
    for item in root.findall(i):
        
        new={}
        l1=[]
        df1 =pd.DataFrame()
        for child in item:      
        
            l1.append(child.attrib)
            
        df1=pd.DataFrame(l1)

        if len(df1.columns) > 0:
            ## Output to Excel for each data object
            savetoexcel(df1,'Output.xlsx','Table {}'.format(count))
        
    count=count+1
    



