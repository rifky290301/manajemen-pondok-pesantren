from DBConnector import DBConnect


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
            query += "'"+value+"',"
        query = query[:-1]
        query += ")"
        print(query)
        result = connection.executeCreate(query)

    def read(self):
        connection = DBConnect()
        query = "SELECT * from "+self.table
        result = connection.executeRead(query)
        print(result)

    def update(self, values, idInput):
        connection = DBConnect()
        query = """UPDATE """+self.table+" SET ("
        for i in range(len(self.column)):
            query += self.column[i]+"="
            query += values[i]+", "
        query = query[:-1]
        query += ") WHERE id ='%d'" % (idInput)
        print(query)
        # connection.executeUpdate(query)
        # print(result)

    def delete(self, idInput):
        connection = DBConnect()
        query = """DELETE FROM """+self.table+" WHERE id = '%d'" % (idInput)
        # result = connection.executeDelete(query)
        print(query)
