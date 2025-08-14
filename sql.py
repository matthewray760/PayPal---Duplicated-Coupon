import pyodbc as py
import pandas as pd
import datetime
import tkinter as tk


def execute_query(date):
        # Set up the database connection parameters
        server = 'PROD-SQL-RO'
        database = 'LM'
        username = 'ARBFUND\matthewray'
        password = 'Uhglbk547895207!!'
        driver = '{ODBC Driver 17 for SQL Server}'
        

        # Create the connection string
        conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};Trusted_Connection=yes;TrustServerCertificate=yes;MultiSubnetFailover=yes'

        # Connect to the database
        conn = py.connect(conn_str)

        # Create a cursor object to execute the SQL statements
        cursor = conn.cursor()

        cursor.execute('SET QUERY_GOVERNOR_COST_LIMIT 300')

        # Execute a SQL query
        query = f'''
        DECLARE @Date DATE = '{date}';

        select t.isactive, SM.cusip, t.username, t.origTransactionid, t.transactionID, t.AccountID, t.EntryDate,t.SettleDate,t.PostDate,t.TransactionTypeAbbreviation, CashEntryAmount from transactioninfo t
        JOIN securitymaster sm ON t.securityid = sm.ID
        WHERE 1=1
            --and AccountID IN (select accountID FROM Aggregates where aggregateID = 352922)
            and AccountID IN ('352906','352907','352913','352918','352914','352902','352909','352919')
            and isactive = 1
            and t.EntryDate >= @Date
            and transactiontypeabbreviation = 'CPN'


        order by t.EntryDate DESC
        '''

        cursor.execute(query)

        # Fetch all the rows from the query result
        cursor.fetchall()
        df = pd.read_sql(query,conn)

        # Close the cursor and the connection
        cursor.close()
        conn.close()
  

        return df, print("SQL executed within the timeout period")
    
