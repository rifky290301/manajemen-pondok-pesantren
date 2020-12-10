import mysql.connector
from mysql.connector import Error


class DBConnect:
    def __init__(self):
        self.connection = None

    def executeCreate(self, query):
        try:
            self.connection = mysql.connector.connect(
                host="sql12.freemysqlhosting.net", database="sql12380242", username="sql12380242", password="xcF3ZyFsnR")
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute(query)
                self.connection.commit()
                print("success")
        except Error as e:
            print(e)

    def executeRead(self, query):
        try:
            self.connection = mysql.connector.connect(
                host="sql12.freemysqlhosting.net", database="sql12380242", username="sql12380242", password="xcF3ZyFsnR")
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute(query)
                record = cursor.fetchall()
                print("success")
                return record
        except Error as e:
            print(e)

    def executeUpdate(self, query):
        try:
            self.connection = mysql.connector.connect(
                host="sql12.freemysqlhosting.net", database="sql12380242", username="sql12380242", password="xcF3ZyFsnR")
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute(query)
                self.connection.commit()
                print("success")
                return record
        except Error as e:
            print(e)

    def executeDelete(self, query):
        try:
            self.connection = mysql.connector.connect(
                host="sql12.freemysqlhosting.net", database="sql12380242", username="sql12380242", password="xcF3ZyFsnR")
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute(query)
                self.connection.commit()
                print("success")
                return record
        except Error as e:
            print(e)
