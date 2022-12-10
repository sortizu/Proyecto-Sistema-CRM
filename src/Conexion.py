#import mariadb
from datetime import date
import mysql.connector

#Realiza la conexion con la base de datos

class conexion():
    def __init__(self, host, user, passwd, database) -> None:
        self._host=host
        self._user=user
        self._passwd=passwd
        self._database=database
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="DB_CRM_services_v3"
        )
    mycursor = mydb.cursor()