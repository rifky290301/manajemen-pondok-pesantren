from Model import Model


class Santri(Model):

    def __init__(self):
        super().__init__("santri", [
            "nama", "email", "password", "alamat", "perguruan_tinggi", "prodi", "no_hp"])
