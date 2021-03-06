from model import Model
from User import User
from DBConnector import DBConnect
import datetime


class Santri(User):
    tgl = datetime.date.today().strftime('%Y-%m-%d')

    def __init__(self, inputEmail=None):
        super().__init__("santri", [
            "nama", "email", "password", "alamat", "no_hp", "perguruan_tinggi", "prodi", "kamar_id"])

        # variable privet
        if inputEmail == None:
            pass
        else:
            self.__email = inputEmail
            connection = DBConnect()
            query = "SELECT password FROM " + self.table + \
                " WHERE email='%s'" % (self.__email)
            result = connection.executeRead(query)
            self.__password = result[0][0]

    # penggunaan __call__
    def __call__(self, email):
        print("Trimakasih Kang", email,
              "Telah melakukan Pembayaran SPP :)")

    def getPassword(self):
        return self.__password

    def setPassword(self, passwordBaru):
        self.__password = passwordBaru
        connection = DBConnect()
        query = "UPDATE "+self.table + \
            " SET password= '%s' WHERE email = '%s'" % (
                self.__password, self.__email)
        connection.execute(query)
        print("===Password Berhasil Dirubah===")

    def getID(self):
        connection = DBConnect()
        query = "SELECT * from "+self.table + \
            " WHERE email= '%s'" % (self.__email)
        hasil = connection.executeRead(query)
        return hasil[0][0]

    def bayarSPP(self, nominal, email):
        connection = DBConnect()
        query = "INSERT INTO transaksi (tgl_pembayaran, nominal, jenis_transaksi, santri_id) VALUES ('%s',%s,'spp', %s)" % (
            Santri.tgl, nominal, self.getID())
        connection.execute(query)
        print("===Bayar SPP Berhasil===")


# santri1 = Santri("b")
# # santri1.getPassword()
# print(santri1.getPassword())
# santri1.setPassword("d")
# print(santri1.getPassword())
