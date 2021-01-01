from model import Model
from DBConnector import DBConnect


class AbsenNgaji(Model):

    def __init__(self):
        super().__init__("absen_mengaji", ["tgl_absen", "santri_id",
                                           "ustad_id", "kitab_id"])

    @staticmethod
    def absenUstad(ustad, kitab):
        connection = DBConnect()
        query = "INSERT INTO absen_mengaji (tgl_absen, ustad_id, kitab_id) VALUES ('getdate()', %s, %s)" % (
            ustad, kitab)
        connection.execute(query)
        print("===Absen berhasil===")
