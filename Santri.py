from model import Model
from User import User
from DBConnector import DBConnect


class Santri(User):

    def __init__(self):
        super().__init__("santri", [
            "nama", "email", "password", "alamat", "no_hp", "perguruan_tinggi", "prodi", "kamar_id"])

    def getPassword(self, email):
        connection = DBConnect()
        query = "SELECT password FROM " + \
            self.table+" WHERE email='%s'" % (email)
        result = connection.executeRead(query)
        # print(query)
        print("Password anda: ", result[0][0])

    def setPassword(self, email, passInput):
        connection = DBConnect()
        query = "UPDATE "+self.table + \
            " SET password= '%s' WHERE email = '%s'" % (passInput, email)
        connection.execute(query)

    def getID(self, email):
        connection = DBConnect()
        query = "SELECT * from "+self.table + " WHERE email= '%s'" % (email)
        result = connection.executeRead(query)
        return result[0][0]

    def bayarSPP(self, tglBayar, nominal, email):
        connection = DBConnect()
        santri = Santri()
        query = "INSERT INTO transaksi (tgl_pembayaran, nominal, jenis_transaksi, santri_id) VALUES ('now()', %s, 'spp', %s)" % (
            nominal, self.getID(email))
        connection.execute(query)
        print("===Bayar SPP Berhasil===")
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
#                 "852", "tk", "nol kecil", "082140091356", '2'])

# santri1 = Santri()
# santri1.search("rifky")
# santri1 = Santri()
# santri1.order("santri", "nama", 2)

# santri1 = Santri()
# santri1.printCoba()

# santri = Santri()
# santri.cariID('a')
