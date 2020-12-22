from model import Model
from DBConnector import DBConnect


class AbsenNgaji(Model):

    def __init__(self):
        super().__init__("absen_mengaji", ["tgl_absen", "santri_id",
                                           "ustad_id", "kitab_id"])

    # def cariID(self, email):
    #     connection = DBConnect()
    #     query = "SELECT * from "+self.table + " WHERE email= '%s'" % (email)
    #     result = connection.executeRead(query)
    #     return result[0][0]
