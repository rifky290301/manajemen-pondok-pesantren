import mysql.connector


class Model:
    def connect():
        global mydb

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="manajemen-pondok-pesantren"
        )

    def getData(tabel, id):
        Model.connect()
        mycursor = mydb.cursor()

        if id == 0:
            query = F"SELECT * FROM {tabel}"
        else:
            query = F"SELECT * FROM {tabel} WHERE id = {id}"

        mycursor.execute(query)
        result = mycursor.fetchall()

        return result

    def createData(tabel, value):
        Model.connect()
        mycursor = mydb.cursor()

        if tabel == "santri":
            query = F"INSERT INTO {tabel} (nama, email, password, alamat, perguruan_tinggi, prodi, no_hp) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        elif tabel == "pengurus":
            query = F"INSERT INTO {tabel} (nama, email, password, alamat, no_hp, jabatan) VALUES (%s, %s, %s, %s, %s, %s)"
        elif tabel == "ustad":
            query = F"INSERT INTO {tabel} (nama, email, password, alamat, no_hp) VALUES (%s, %s, %s, %s, %s)"

        mycursor.execute(query, value)
        mydb.commit()
        print("Data berhasil ditambahkan")

    def deleteData(tabel, id):
        Model.connect()
        mycursor = mydb.cursor()

        query = F"DELETE FROM {tabel} WHERE id = {id}"
        mycursor.execute(query)
        mydb.commit()

        print("Data dari tabel {0} yang memiliki {1} telah dihapus",
              format(tabel, str(id)))

    def updateData(tabel, colom, value, id):
        Model.connect()
        mycursor = mydb.cursor()

        query = F"UPDATE {tabel} SET {colom} = {value} WHERE id = {id}"
        mycursor.execute(query)
        mydb.commit()

        print("Data berhasil diupdate")


santri = Model.getData("santri", 0)
for i in santri:
    print(i)


# value = ("sukirman", "sukirman@gmail.com", "123458",
#          "sempu, banyuwangi", "Jember", "Informatika", "082140091385")

# santri = Model.createData("santri", value)

# santri = Model.deleteData("santri", 7)

# santri = Model.updateData("santri", "email", "firmana@gmail.com", 8)
