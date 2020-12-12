from Model import Model


class Santri(Model):

    def __init__(self):
        super().__init__("santri", [
            "nama", "email", "password", "alamat", "perguruan_tinggi", "prodi", "no_hp"])


# santri1 = Santri()
# santri1.delete(3)

# santri1 = Santri()
# santri1.update(["budi", "budi@gmail.com", "jember sumbersari",
#                 "852", "tk", "nol kecil", "082140091356"], 2)
