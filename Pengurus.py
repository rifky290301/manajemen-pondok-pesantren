from Model import Model
from Santri import Santri
from Transaksi import Transaksi


class Pengurus(Model):

    def __init__(self):
        super().__init__("pengurus", [
            "nama", "email", "password", "alamat", "no_hp", "jabatan"])

    def readSantri(self):
        model = Santri()
        model.read()

    def readTransaksi(self):
        model = Transaksi()
        model.read()

    def createSantri(self):
        model = Santri()
        # model.create(nama, email, password, alamat,
        #              perguruan_tinggi, prodi, no_hp)


madol = Pengurus()
# madol.create(["martha", "martha@gmail.com", "123",
#               "sempu, karangsari", "082140091385", "ketua"])

# madol.readSantri()
