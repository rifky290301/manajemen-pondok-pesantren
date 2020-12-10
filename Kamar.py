from Model import Model


class Kamar(Model):

    def __init__(self):
        super().__init__("kamar", ["jumlah_kasur", "santri_id"])
