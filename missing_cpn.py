import pandas as pd
from sql import execute_duplicated_cpns, execute_uncleared_cpns
import pyodbc as py
import datetime
import tkinter
from message import show_popup,get_input




def uncleared_cpns(recon_date,begin_date):

    df = execute_uncleared_cpns(recon_date=recon_date,begin_date=begin_date)


    return df
