# Anand Patel (23ananadpatel23@gmail.com)
# Purpose: Test for tables from MS SQL using pyodbc module
import csv
import pyodbc
import sys
import os
import re

def main():

    # Connect to CMDB from serverName
    serverName = raw_input("Server Name: ")
    databaseName = raw_input("Database Name: ")
    conn = pyodbc.connect('Trusted_Connection=yes', driver='{SQL Server}', server=serverName, database=databaseName)
    cur = conn.cursor()

    tables = ["tableOne", "tableTwo", "tableThree", "tableFour", "tableFive"]

    for table in tables:
        if cur.tables(table=table).fetchone():
            print table + " exists"
        else:
            print table + " does not exist"

if __name__ == '__main__':
    main()
