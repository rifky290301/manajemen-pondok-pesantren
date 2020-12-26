from model import Model
from DBConnector import DBConnect
from User import User


class Ustad(User):

    def __init__(self):
        super().__init__("ustad", [
            "nama", "email", "password", "alamat", "no_hp"])

    def getID(self, email):
        connection = DBConnect()
        query = "SELECT * from "+self.table + " WHERE email= '%s'" % (email)
        result = connection.executeRead(query)
        return result[0][0]

    # def jadwalDewe(self, email):
    #     connection = DBConnect()
    #     query = "SELECT * from "+self.table + " WHERE email= '%s'" % (email)
    #     result = connection.executeRead(query)
    #     print(result)
    #     # print(query)
