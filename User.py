from model import Model
from DBConnector import DBConnect


class User(Model):
    coki = None

    def __init__(self, getTable, getColumn):
        super().__init__(getTable, getColumn)

    def login(self, email, password):
        connection = DBConnect()
        query = "SELECT * from "+self.table+" WHERE email="+email+" and "+"password ="password
        result = connection.executeRead(query)
        coki = result
        if result == None:
            return True
        else:
            return False

    # def printCoba(self):
    #     print(self.column)
    #     print(self.table)
