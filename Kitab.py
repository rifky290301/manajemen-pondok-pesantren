from model import Model


class Kitab(Model):

    def __init__(self):
        super().__init__("kitab", ["judul", "pengarang",
                                   "penulis", "tahun_terbit", "nama_penerbit"])
