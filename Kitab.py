from model import Model
from DBConnector import DBConnect


class Kitab(Model):

    def __init__(self):
        super().__init__("kitab", ["judul", "pengarang",
                                   "penulis", "tahun_terbit", "nama_penerbit"])

    @staticmethod
    def getID(judul):
        connection = DBConnect()
        query = "SELECT * from kitab WHERE judul= '%s'" % (judul)
        result = connection.executeRead(query)
        return result[0][0]
