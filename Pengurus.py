from User import User


class Pengurus(User):
    def __init__(self, inputNama, inputAlamat, inputNo_hp, inputEmail, inputPassword, inputStatus, inputInstansi, inputAngkatan, inputJabatan):
        super().__init__(self, inputNama, inputAlamat,
                         inputNo_hp, inputEmail, inputPassword, inputStatus)
    self.instansi = inputInstansi
    self.angkatan = inputAngkatan
    self.jabatan = inputJabatan

    def tampilkanDataSPP():
        pass

    def tampilkanDataJagaPost():
        pass

    def tampilkanDataUser():
        pass

    def registerUstad():
        pass

    def registerSantri():
        pass

    def hapusData():
        pass
