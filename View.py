from Santri import Santri
from Pengurus import Pengurus
from Ustad import Ustad
from Transaksi import Transaksi
from Kamar import Kamar
from Kitab import Kitab
from Pengumuman import Pengumuman
from JagaPos import JagaPos


class View:
    def __init__(self, x):
        self.x = x

    def spp(self):
        spp1 = Transaksi()
        if self.x == 1:
            spp1.read()
        elif self.x == 2:
            spp1.update()
        elif self.x == 3:
            inptIdTransaksi = int(input("Masukkan id Transaksi: "))
            spp1.delete(inptIdTransaksi)

    def santri(self):
        santri1 = Santri()
        if self.x == 1:
            santri1.read()
        elif self.x == 2:
            santri1.update()
        elif self.x == 3:
            inptIdSantri = int(input("Masukkan Id Santri: "))
            santri1.delete(inptIdSantri)

    def ustadz(self):
        ustadz1 = Ustad()
        if self.x == 1:
            ustadz1.read()
        elif self.x == 2:
            ustadz1.update()
        elif self.x == 3:
            inptIdUstadz = int(input("Masukkan Id Ustadz: "))
            ustadz1.delete(inptIdUstadz)

    def jagapost(self):
        jagapost1 = JagaPos()
        if self.x == 1:
            jagapost1.read()
        elif self.x == 2:
            jagapost1.update()
        elif self.x == 3:
            inptIdJagapost = int(input("Masukkan Id JagaPost: "))
            jagapost1.delete(inptIdJagapost)

    # def pengurus(self):
    #     pengurus1 = Pengurus()
    #     santri1 = Santri()
    #     jagapost1 = JagaPos()
    #     ustad1 = Ustad()
    #     if self.x == 1:
    #         santri1.read()
    #         print("sukses santri")
    #     elif self.x == 2:
    #         jagapost1.read()
    #         print("sukses jagapost")
    #     elif self.x == 3:
    #         pengurus1.read()
    #         print("sukseks pengurus")
    #     elif self.x == 4:
    #         ustad1.read()
    #         print("sukses ustadz")
