# Anand Patel (23anandpatel23@gmail.com)
# Purpose: Importing CIR Items to DB
import sys, os, time
import re
from datetime import datetime
import pyodbc
import csv

def filterCompanyName(companyName):
    """ Searches through given argument string of a file path and searches for
    terms that are not to be included within database
    Args:
        companyName (str): CompanyNmae
    """
    # uppercasing given path
    if companyName == None:
        return companyName
    if companyName != None:
        companyName = companyName.upper()

    # if there isn't a match with any filter, it's a valid item to add
    match = False
    for itemFilter in filters:
        if re.search(itemFilter, companyName, re.IGNORECASE):
            match = True
            break
    if not match:
        acceptedPath = companyName
        return acceptedPath

def DriveOutputToCSV(filename):
    print 'Path to add: ' + filename
    cursor = conn.cursor()
    cursor.execute( """
                    SELECT * FROM CIR.DriveItem
                    """)
    with open(filename, 'wb') as fout:
        writer = csv.writer(fout)
        writer.writerows(cursor.fetchall())
    print "All items added successfully to " + filename

def save_items_in_db(items, LoadId):
    """ Store list of items into a table
    Args:
        items (list): List of items to store.  Each item is a dictionary.
        LoadId (str): Id of parent COnfigItemLoad record

    """
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM CIR.DriveItem")
        for item in items:
            if filterPath(item['filepath']) == None:
                continue
            if filterCopyrightName(item['copyright']) == None:
                continue
            if filterCompanyName(item['companyName']) == None:
                continue
            cur.execute("""INSERT INTO
                        CIR.DriveItem
                        (DriveSource, DriveFileName, Component_Name, Filepath, FileDate, DriveVersion, Company_Name, Copyright, LoadId)
                        VALUES
                        (?, ?, ?, ?, ?, ?, ?, ?, ?)""", "KDrive", item['filename'], item['componentName'], item['filepath'], item['fileDate'],item['version'], item['companyName'],item['copyright'], LoadId)
        print
        cur.commit()
    except:
        con.close()
        print "Closed connection. There has been an error in save_items_in_db, cmdb_krive.py"

def main():
    pass

if __name__ == '__main__':
    main()
