from model import Model
from DBConnector import DBConnect


class JagaPos(Model):

    def __init__(self):
        super().__init__("jaga_pos", ["tgl_piket", "kamar_id"])

    # penggunaan __call__
    def __call__(self, email):
        connection = DBConnect()
        query = "SELECT * from santri WHERE email= '%s'" % (email)
        result = connection.executeRead(query)
        print("Kamar dengan ID", str(
            result[0][8]), "Telah Melakukan Absen JagaPost")

    def getID(self, email):
        connection = DBConnect()
        query = "SELECT * from santri WHERE email= '%s'" % (email)
        result = connection.executeRead(query)
        return str(result[0][8])
