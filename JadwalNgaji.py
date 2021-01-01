from model import Model
from DBConnector import DBConnect
from Ustad import Ustad


class JadwalNgaji(Model):
    def __init__(self):
        super().__init__("jadwal", ["hari", "waktu", "ustad_id", "kitab_id"])

    @classmethod
    def jadwalDewe(cls, ustad_id):
        connection = DBConnect()
        query = "SELECT * from " + "jadwal" + \
            " WHERE ustad_id= '%s'" % (ustad_id)
        result = connection.executeRead(query)
        p = PrettyTable()
        x = []
        x.append('id')
        for column in self.column:
            x.append(column)
        p.field_names = x
        for row in result:
            listRow = list(row)
            listRow.pop(len(listRow)-1)
            listRow.pop(len(listRow)-1)
            p.add_row(listRow)
        print(p)
