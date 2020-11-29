from User import User


class Santri(User):
    def __init__(self, inputNama, inputAlamat, inputNo_hp, inputEmail, inputPassword, inputStatus, inputNoKamar, inputAngkatan, inputInstansi):
        super().__init__(self, inputNama, inputAlamat,
                         inputNo_hp, inputEmail, inputPassword, inputStatus)
        self.no_kamar = inputNoKamar
        self.angkatan = inputAngkatan
        self.instansi = inputinstansi

    def tampilkanData():
        pass

    def absenMengaji():
        pass

    def absenJagapos():
        pass
