
import numpy as np
import pandas as pd
import xml.etree.cElementTree as et
import os



tree=et.parse( r'C:\Users\savkaur\OneDrive - Capgemini\Desktop\assignment\data\001.xml')
root=tree.getroot()
m=[]

for item in root.findall('./DataExtract900jer/Messages'):
    new={}
    l1=[]
    df1 =pd.DataFrame()
    for child in item:      
      
        l1.append(child.attrib)
        
    df1=pd.DataFrame(l1)
    print(df1)


for item in root.findall('./DataExtract900jer/Rules'):
    new={}
    l2=[]
    df2 =pd.DataFrame()
    for child in item:      
      
        l2.append(child.attrib)
        
    df2=pd.DataFrame(l2)
    print(df2)

for item in root.findall('./Nuula/Errors'):
    new={}
    l3=[]
    df3 =pd.DataFrame()
    for child in item:      
      
        l3.append(child.attrib)
        
    df3=pd.DataFrame(l3)
    print(df3)

