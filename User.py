from model import Model
from DBConnector import DBConnect


class User(Model):
    cookie = []

    def __init__(self, getTable, getColumn):
        super().__init__(getTable, getColumn)

    def login(self, email, password):
        connection = DBConnect()
        query = "SELECT * from "+self.table+" WHERE email="+email+" and "+"password ="password
        result = connection.executeRead(query)
<<<<<<< HEAD
        cookie = result
        # print(cookie[0][0])
        if not result:
=======
        coki = result
        if result == None:
>>>>>>> parent of 043e054... mbenakne login
            return True
        else:
            return False

    # def printCoba(self):
    #     print(self.column)
    #     print(self.table)
