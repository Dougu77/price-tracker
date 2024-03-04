# Imports
import mysql.connector
import pyodbc
from utils.messages import *

# Function
def set_connection(sql_type):
    '''
    Set the connection with the Database, according to the server used (MySQL or SQL Server)

    Args:
        sql_type (str): Type of server used

    Returns:
        Database Connection (changes based on the server type): Connection with Database
    '''
    if sql_type == 'mysql':   
        return mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'password',
            database = 'price_tracker')
    elif sql_type == 'sqlserver':
        return pyodbc.connect('DRIVER={SQL Server};SERVER=server;DATABASE=price_tracker;UID=user;PWD=password')

# Variables
sql_type = 'mysql'
connection = set_connection(sql_type)

# Function
def insert_info(table, price, date, time):
    '''
    Insert the data in the Database

    Args:
        table (str): Table to insert the data
        price (str): Price of the product
        date (str): Date of the search
        time (str): Time of the search
    '''
    try:
        cursor = connection.cursor()
        if sql_type == 'mysql': query = f'INSERT INTO `{table}` (price, date, time) VALUES (%s, %s, %s)'
        elif sql_type == 'sqlserver': query = f'INSERT INTO [{table}] (price, date, time) VALUES (%s, %s, %s)'
        values = (price, date, time)
        cursor.execute(query, values)
        connection.commit()
    except:
        print(get_message('error_insert'))
