from Model import Model


class User(Model):

    def __init__(self, table):
        super().__init__(table, [
            "nama", "email", "password", "alamat", "no_hp"])
