from model import Model
from DBConnector import DBConnect


class User(Model):
    cookie = []

    def __init__(self, getTable, getColumn):
        super().__init__(getTable, getColumn)

    def login(self, email, password):
        connection = DBConnect()
        query = "SELECT * from "+self.table + \
            " WHERE email= '%s' and password = '%s'" % (email, password)
        result = connection.executeRead(query)
        cookie = result
        # print(cookie[0][0])
        if not result:
            return True
        else:
            return False

    # def printCoba(self):
    #     print(self.column)
    #     print(self.table)
