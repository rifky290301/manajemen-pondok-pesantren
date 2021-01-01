from model import Model
from DBConnector import DBConnect


class AbsenNgaji(Model):

    def __init__(self):
        super().__init__("absen_mengaji", ["tgl_absen", "santri_id",
                                           "ustad_id", "kitab_id"])
