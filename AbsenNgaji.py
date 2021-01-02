from model import Model
from DBConnector import DBConnect
import datetime


class AbsenNgaji(Model):
    tgl = datetime.date.today().strftime('%Y-%m-%d')

    def __init__(self):
        super().__init__("absen_mengaji", ["tgl_absen", "santri_id",
                                           "ustad_id", "kitab_id"])

    @staticmethod
    def absenUstad(ustad, kitab):
        connection = DBConnect()
        query = "INSERT INTO absen_mengaji (tgl_absen, ustad_id, kitab_id) VALUES ('%s', %s, %s)" % (
            AbsenNgaji.tgl, ustad, kitab)
        connection.execute(query)
        print("===Absen berhasil===")
