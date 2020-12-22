from model import Model


class Kamar(Model):

    def __init__(self):
        super().__init__("kamar", ["jumlah_kasur"])
