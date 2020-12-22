from Santri import Santri
from Pengurus import Pengurus
from Ustad import Ustad
from Transaksi import Transaksi
from Kamar import Kamar
from Kitab import Kitab
from Pengumuman import Pengumuman
from JagaPos import JagaPos
import datetime


class Router:
    tgl = datetime.date.today().strftime('%d-%m-%Y')

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
        else:
            nama = input("Nama:")
            email = input("Email")
            password = input("Password:")
            alamat = input("Alamat:")
            no_hp = input("Nomer HP:")
            perguruan = input("Perguruan TInggi:")
            prodi = input("Prodi")
            santri1.create(
                [nama, email, password, alamat, no_hp, perguruan, prodi])

    def ustadz(self):
        ustadz1 = Ustad()
        if self.x == 1:
            ustadz1.read()
        elif self.x == 2:
            ustadz1.update()
        elif self.x == 3:
            inptIdUstadz = int(input("Masukkan Id Ustadz: "))
            ustadz1.delete(inptIdUstadz)
        else:
            nama = input("Nama:")
            email = input("Email")
            password = input("Password:")
            alamat = input("Alamat:")
            no_hp = input("Nomer HP:")
            ustadz1.create([nama, email, password, alamat, no_hp])

    def jagapost(self):
        jagapost1 = JagaPos()
        if self.x == 1:
            jagapost1.read()
        elif self.x == 2:
            jagapost1.update()
        elif self.x == 3:
            inptIdJagapost = int(input("Masukkan Id JagaPost: "))
            jagapost1.delete(inptIdJagapost)
        else:
            # today = datetime.date.today()
            # tgl = today.strftime('%d-%m-%Y')
            # tgl = datetime.date.today().strftime('%d-%m-%Y')
            kamar = input("ID kamar:")
            jagapost1.create([Router.tgl, kamar])

    def pengumuman(self):
        if self.x == 1:
            Pengumuman.read()
        elif self.x == 2:
            Pengumuman.update()
        elif self.x == 3:
            inptIdJagapost = int(input("Masukkan Id JagaPost: "))
            Pengumuman.delete(inptIdJagapost)
        else:
            isi = input("isi pengumuman")
            idPengurus = input("id pengurus")
            Pengumuman.create([isi, idPengurus])

    def viewSantri(self):
        santri1 = Santri
        if self.x == 1:
            santri1.coba()
            # Santri.bayarSPP(Router.tgl, input("nominal"), "tes")
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
