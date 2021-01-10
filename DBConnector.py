import mysql.connector
from mysql.connector import Error


class DBConnect:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="127.0.0.1",
            database="manajemen-pondok-pesantren",
            username="root",
            password=""
        )

    def execute(self, query):
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute(query)
                self.connection.commit()
        except Error as e:
            print(e)

    def executeRead(self, query):
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute(query)
                record = cursor.fetchall()
                return record
        except Error as e:
            print(e)
