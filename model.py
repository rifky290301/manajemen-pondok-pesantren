from DBConnector import DBConnect
from prettytable import PrettyTable


class Model:

    def __init__(self, table, column):
        self.table = table
        self.column = column

    def create(self, values):
        connection = DBConnect()
        query = """INSERT INTO """+self.table+" ("
        for column in self.column:
            query += column+","
        query = query[:-1]
        query += ") VALUES ("
        for value in values:
            if value == None:
                query += "NULL,"
            else:
                query += "'"+value+"',"
        query = query[:-1]
        query += ")"
        # print(query)
        result = connection.execute(query)
        print("===Berhasil DiTambakan===")

    def read(self, role=None):
        connection = DBConnect()
        query = "SELECT * from "+self.table
        result = connection.executeRead(query)
        p = PrettyTable()
        x = []
        if role == None:
            x.append('id')
        for column in self.column:
            x.append(column)
        p.field_names = x
        for row in result:
            listRow = list(row)
            listRow.pop(len(listRow)-1)
            listRow.pop(len(listRow)-1)
            if role != None:
                listRow.pop(0)
            p.add_row(listRow)
        print(p)
        # print(len(listRow))
        # print(x)

    def update(self, values, idInput):
        connection = DBConnect()
        query = """UPDATE """+self.table+" SET "
        for i in range(len(self.column)):
            query += self.column[i]+"="
            if values[i] == None:
                query += "NULL,"
            else:
                query += "'"+values[i]+"',"
        query = query[:-1]
        query += " WHERE id ='%d'" % (idInput)
        # print(query)
        connection.execute(query)
        print("===Berhasil DiUpdate===")

    def delete(self, idInput):
        connection = DBConnect()
        query = """DELETE FROM """+self.table+" WHERE id = '%d'" % (idInput)
        connection.execute(query)
        # print(query)

    def search(self, value):
        connection = DBConnect()
        query = "SELECT * from "+self.table+" WHERE "
        for i in range(len(self.column)):
            query += self.column[i]+" LIKE "+"'"+"%"+value+"%"+"'"+" OR "
        query = query[:-3]
        # print(query)
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

    def order(self, table, col, urutan):
        if urutan == 1:
            x = 'ASC'
        else:
            x = 'DESC'
        connection = DBConnect()
        query = "SELECT * from "+table+" ORDER BY "+col + ' '+x
        # print(query)
        result = connection.executeRead(query)
        print(result)
