from Model import Model
from User import User


class Santri(Model):

    def __init__(self):
        super().__init__("santri", [
            "nama", "email", "password", "alamat", "no_hp", "perguruan_tinggi", "prodi"])

    def getAlamat():
        pass

    def setAlamat():
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
# santri1.create(["budi", "budi@gmail.com", "jember sumbersari",
#                 "852", "tk", "nol kecil", "082140091356"])

# santri1 = Santri()
# santri1.search("rifky")

# santri1 = Santri()
# santri1.order("santri", "nama", 2)
