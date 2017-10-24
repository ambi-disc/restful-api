import mysql.connector

def connect_to_db():
    return mysql.connector.connect(user='',
                                   password='',
                                   host='',
                                   port=3306,
                                   database='')