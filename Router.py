from Santri import Santri
from Pengurus import Pengurus
from Ustad import Ustad
from Transaksi import Transaksi
from Kamar import Kamar
from Kitab import Kitab
from Pengumuman import Pengumuman
from JagaPos import JagaPos
from AbsenNgaji import AbsenNgaji
import datetime


class Router:
    tgl = datetime.date.today().strftime('%Y-%m-%d')

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
        santri1 = Santri()
        jaga = JagaPos()
        absen = AbsenNgaji()
        kitab = Kitab()
        ustad = Ustad()
        if self.x == 1:
            santri1.bayarSPP(Router.tgl, input("nominal"), input('email'))
        elif self.x == 2:
            jaga.create([Router.tgl, jaga.getID(
                input("masukkan email: "))])
        elif self.x == 3:
            idUstad = santri1.getID(input("masukkan email: "))
            idKitab = kitab.getID(input("masukkan judul kitab:"))
            absen.create([Router.tgl, idUstad, idKitab])

    def viewUstadz(self):
        pass

# santri1.bayarSPP(Router.tgl, input("nominal: "), input('email: '))
# jaga = JagaPos()
# jaga.create([Router.tgl, '1'])
