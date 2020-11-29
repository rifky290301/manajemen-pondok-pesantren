from User import User


class Ustad(User):
    def __init__(self, inputNama, inputAlamat, inputNo_hp, inputEmail, inputPassword, inputStatus, inputTglMulaimengajar, inputTglAkhirmengajar):
        super().__init__(self, inputNama, inputAlamat,
                         inputNo_hp, inputEmail, inputPassword, inputStatus)
    self.TglMulaimengajar = inputTglMulaimengajar
    self.TglAkhirmengajar = inputTglAkhirmengajar

    def absenMengajar():
        pass

    def absenKhotbah():
        pass

    def lihatJadwal():
        pass
