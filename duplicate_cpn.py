import pandas as pd
from sql import execute_duplicated_cpns
import pyodbc as py
import datetime
import tkinter
from message import show_popup,get_input




def duplicated_cpn(use_sql,date):
    if use_sql == True:
        df = execute_duplicated_cpns(date)[0]

    else:
        filename = 'PayPal - Duplicated Coupon Chk (3)'
        file_path = fr'C:\Users\matthewray\OneDrive - Clearwater\Desktop\Python\PayPal - Duplicated Coupon\Insert\{filename}.csv'  # Update this with the path to your CSV file
        df = pd.read_csv(file_path)


    # Display the DataFrame to ensure it's loaded correctly
    print("Dataframe loaded successfully:")


    # Define the columns to check for duplicates
    if use_sql == True:
        duplicate_columns = ['AccountID', 'cusip']
    else:
        duplicate_columns = ['Account ID', 'Identifier'] 


    # Identify duplicated rows based on the defined columns
    duplicates = df[df.duplicated(subset=duplicate_columns, keep=False)]

    output_filename = f'duplicated_coupon_check_{date}'

    # If duplicates exist, display them
    if not duplicates.empty:
        show_popup("There are Duplicated Coupon Payments - please see the output file")
        #duplicates.to_csv(fr'C:\Users\matthewray\OneDrive - Clearwater\Desktop\Python\PayPal - Duplicated Coupon\Output\{output_filename}.csv', index=False)

    else:
        show_popup("There are no Duplicated Coupon Payments")

    return duplicates
