from model import Model
from User import User
from Santri import Santri
from Transaksi import Transaksi
from DBConnector import DBConnect


class Pengurus(User):

    def __init__(self):
        super().__init__("pengurus", [
            "nama", "email", "password", "alamat", "no_hp", "jabatan"])

    # def readSantri(self):
    #     model = Santri()
    #     model.read()

    # def readTransaksi(self):
    #     model = Transaksi()
    #     model.read()

    # def createSantri(self):
    #     model = Santri()

    def login(self, nama, email, password):
        connection = DBConnect()
        query = "SELECT * from "+self.table + \
            " WHERE nama= '%s' and email= '%s' and password = '%s'" % (
                nama, email, password)
        result = connection.executeRead(query)
        # coki = result
        if not result:
            return True
        else:
            return False
        # model.create(nama, email, password, alamat,
        #              perguruan_tinggi, prodi, no_hp)

    def getID(self, email):
        connection = DBConnect()
        query = "SELECT * from "+self.table + " WHERE email= '%s'" % (email)
        result = connection.executeRead(query)
        return result[0][0]

# madol = Pengurus()
# madol.create(["martha", "martha@gmail.com", "123",
#               "sempu, karangsari", "082140091385", "ketua"])

# madol.readSantri()
