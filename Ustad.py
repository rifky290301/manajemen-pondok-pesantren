from model import Model
from DBConnector import DBConnect
from User import User


class Ustad(User):

    def __init__(self):
        super().__init__("ustad", [
            "nama", "email", "password", "alamat", "no_hp"])

    def getID(self, nama):
        connection = DBConnect()
        query = "SELECT * from "+self.table + " WHERE nama= '%s'" % (nama)
        result = connection.executeRead(query)
        return result[0][0]
