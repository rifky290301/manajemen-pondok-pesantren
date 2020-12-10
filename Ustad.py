from Model import Model


class Ustad(Model):

    def __init__(self):
        super().__init__("ustad", [
            "nama", "email", "password", "alamat", "no_hp"])
