from Model import Model


class Pengurus(Model):

    def __init__(self):
        super().__init__("pengurus", [
            "nama", "email", "password", "alamat", "no_hp", "jabatan"])
