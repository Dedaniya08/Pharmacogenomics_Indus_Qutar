import pandas as pd
from sqlalchemy import create_engine, MetaData
import os
import sqlalchemy
from urllib.parse import quote
import json


os.chdir('Z:\PgX\Drug_content_csv')   #directory to be changed
files_in_folder = os.listdir()
txt_files = filter(lambda x: x[-4:] == '.csv', files_in_folder)
col_name = ['Barcode Id','Member id','Beneficiary Name','AGE',
           'SEX','Beneficiary ID','QC Status','Batch no','Recipts',
           'Recipts status','HRA Status','EHR ID','VISIT ID',
           'GSA Status GSA (Pass=>97%/Fail=<97%)','ContactNo',
           'Email ID','Language','Product_Details','DATE']
engine = create_engine("postgresql://ECOM:%s@localhost/MEDNAWISE" % quote('Ecom#Indus123'))
metadata = sqlalchemy.MetaData()
connection = engine.connect()
census = sqlalchemy.Table('mednawise_ind_info', metadata, autoload=True, autoload_with=engine)
print(metadata)
print(census)
query = sqlalchemy.select([census])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet[:3])
