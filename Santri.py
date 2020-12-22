from model import Model
from User import User
from DBConnector import DBConnect


class Santri(User):

    def __init__(self):
        super().__init__("santri", [
            "nama", "email", "password", "alamat", "no_hp", "perguruan_tinggi", "prodi"])

<<<<<<< HEAD
    def getPassword(self):
        connection = DBConnect()
        query = "UPDATE "+self.table+" SET password="+passInput
        connection.execute(query)
=======
    def getPassword():
        # super().search
        pass
>>>>>>> parent of 043e054... mbenakne login

    def setPassword(self, passInput):
        connection = DBConnect()
        query = "UPDATE "+self.table+" SET password="+passInput
        connection.execute(query)

<<<<<<< HEAD
    def cariID(self, email):
        query = "SELECT * from "+self.table + " WHERE email= '%s'" % (email)
        result = connection.executeRead(query)
        return result[0]
=======
    def setAlamat():
        pass
>>>>>>> parent of 043e054... mbenakne login

    def coba(self):
        print("coba")

    def coba2():
        coba()

    def bayarSPP(self, tglBayar, nominal):
        # connection = DBConnect()
        # user = User("santri", [
        #     "nama", "email", "password", "alamat", "no_hp", "perguruan_tinggi", "prodi"])
        # print(user.cookie)
        self.coba()
        # query = "INSERT INTO transaksi (tgl_pembayaran, nominal, jenis_transaksi) VALUES (%s, %d, 'spp', %i)" % (
        #     tglBayar, nominal, self.cookie[0][0])
        # connection.execute(query)
        # print(query)

    # def jumlahSPP():
    #     sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    # def read():
    #     pass
# santri1 = Santri()
# santri1.search("budi")


# santri1 = Santri()
# santri1.delete(2)
# santri1.read()


# santri1 = Santri()
# santri1.update(["budi", "budi@gmail.com", "852", "jember sumbersari",
#                 "082140091356", "ibrahimi", "si"], 2)

# santri1 = Santri()
# santri1.create(["budi", "budi@gmail.com", "jember sumbersari",
#                 "852", "tk", "nol kecil", "082140091356"])

# santri1 = Santri()
# santri1.search("rifky")
# santri1 = Santri()
# santri1.order("santri", "nama", 2)
<<<<<<< HEAD
# santri1 = Santri()
# santri1.printCoba()

Santri.read()
=======
santri1 = Santri()
santri1.printCoba()
>>>>>>> parent of 043e054... mbenakne login
