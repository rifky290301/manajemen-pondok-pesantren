from model import Model
from User import User


class Santri(User):
    coke = []

    def __init__(self):
        super().__init__("santri", [
            "nama", "email", "password", "alamat", "no_hp", "perguruan_tinggi", "prodi"])

    def getPassword():
        connection = DBConnect()
        query = "UPDATE "+self.table+" SET password="+passInput
        connection.execute(query)

    def setPassword(self, passInput):
        connection = DBConnect()
        query = "UPDATE "+self.table+" SET password="+passInput
        connection.execute(query)

    def aggotaKamar():
        pass

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
# santri1.create(["ani", "ani@gmail.com", "852",
#                 "jember sumbersari", "082140091356", "tk", "nol kecil"])

# santri1 = Santri()
# santri1.search("rifky")
# santri1 = Santri()
# santri1.order("santri", "nama", 2)
# santri1 = Santri()
# santri1.printCoba()
