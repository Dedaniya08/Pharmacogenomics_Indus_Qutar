import sys
import os
sys.path.append('Z:\\python3.8\\Lib\\site-packages')
import pandas as pd
pd.options.mode.chained_assignment = None
import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"Z:\python3.8\Support_files\instantclient_19_8")
import cx_Oracle
from sqlalchemy import types, Table, create_engine, Column, String, MetaData
from sqlalchemy.types import Integer, String
from sqlalchemy.dialects.oracle import NUMBER, VARCHAR2, DATE
import sqlalchemy as sa



def Oracle_pdf(drug_info):
    CONN_INFO = {
        'host': '172.16.1.2',
        'port': 1521,
        'user': 'indus',
        'psw': 'sudni',
        'service': 'indus',
    }
def orcle_create_table():

    os.chdir(r'Z:/PgX/Individual_raw')
    files_in_folder = os.listdir()
    files_in_folder = files_in_folder[0]
    individual_pheno = pd.read_excel(files_in_folder)
    # orcle_create_table(individual_pheno)
    file_pd = individual_pheno
    file_pd = file_pd.astype(str)
    file_pd["Barcode Id"] = file_pd['Barcode Id'].str.replace(" ", "")
    file_pd = file_pd[["Barcode Id", "Beneficiary Name", "Beneficiary ID", "EHR ID", "ContactNo", "Email ID"]]
    file_pd.rename(columns={
        "Barcode Id" : "BARCODE",
        "Beneficiary Name" : "NAME",
        "Beneficiary ID": "BENEFICARY_ID",
        "EHR ID" :  "EHR_ID",
        "ContactNo" : "CONTACT_NO",
        "Email ID": "EMAIL_ID",
    }, inplace=True)
    file_pd[['DATE_OF_ACCEPT_REJECT', 'COMMENTS', 'REPORT_ACCEPT_REJECT', 'UPDATED_BY', 'SMS_STATUS', 'EMAIL_STATUS']] = ""
    file_pd['REPORT_LOC'] = "//172.16.1.252/Genetic_SFTP/MEDNAWISEREPORTS/" + file_pd['BARCODE'] + ".pdf"
    oracle_dtypes = {
        'BARCODE': VARCHAR2(250),
        'NAME': VARCHAR2(250),
        'BENEFICARY_ID': VARCHAR2(250),
        'EHR_ID': VARCHAR2(500),
        'CONTACT_NO': VARCHAR2(500),
        'EMAIL_ID':VARCHAR2(500),
        'REPORT_LOC':VARCHAR2(750),
        'DATE_OF_ACCEPT_REJECT': VARCHAR2(250),
        'COMMENTS' : VARCHAR2(750),
        'REPORT_ACCEPT_REJECT': VARCHAR2(250),
        'UPDATED_BY': VARCHAR2(250),
        'SMS_STATUS': VARCHAR2(250),
        'EMAIL_STATUS': VARCHAR2(250),
    }
    DIALECT = 'oracle'
    SQL_DRIVER = 'cx_oracle'
    USERNAME = 'indus'
    PASSWORD = 'sudni'
    HOST = '172.16.1.2'
    PORT = 1521
    SERVICE = 'indus'
    ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD + '@' + HOST + ':' + str(
        PORT) + '/?service_name=' + SERVICE
    engine = create_engine(ENGINE_PATH_WIN_AUTH)
    metadata = MetaData
    file_pd.to_sql('ihp_mednawise_report', engine, if_exists='append', index=False, schema='indus', dtype=oracle_dtypes)

#
# orcle_create_table()