from model import Model
from DBConnector import DBConnect
from Ustad import Ustad


class JadwalNgaji(Model):
    def __init__(self):
        super().__init__("jadwal", ["hari", "waktu", "ustad_id", "kitab_id"])

    def jadwalDewe(self, ustad_id):
        connection = DBConnect()
        query = "SELECT * from "+self.table + \
            " WHERE ustad_id= '%s'" % (ustad_id)
        result = connection.executeRead(query)
        print(result)
        # print(query)
