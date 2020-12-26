from Santri import Santri
from Pengurus import Pengurus
from Ustad import Ustad
from Transaksi import Transaksi
from Kamar import Kamar
from Kitab import Kitab
from Pengumuman import Pengumuman
from JagaPos import JagaPos
from AbsenNgaji import AbsenNgaji
from JadwalNgaji import JadwalNgaji
import datetime


class Router:
    tgl = datetime.date.today().strftime('%Y-%m-%d')

    def __init__(self, x):
        self.x = x

    def transaksi(self):
        transaksi1 = Transaksi()
        pengurus1 = Pengurus()
        if self.x == 1:
            transaksi1.read()
        elif self.x == 2:
            idperubahan = int(input("Masukkan id Transaksi yang dirubah: "))
            tgl_pembayaran = Router.tgl
            nominal = input("Masukkan Nomila: ")
            jenis_transaksi = input("Jenis Transaksi: ")
            santri_id = input("Masukkan id Santri: ")
            pengurus_id = str(pengurus1.getID(input("masukkan email: ")))
            ustad_id = input("Masukkan id Ustadz: ")
            transaksi1.update([tgl_pembayaran, nominal, jenis_transaksi,
                               santri_id, pengurus_id, ustad_id], idperubahan)
        elif self.x == 3:
            inptIdTransaksi = int(input("Masukkan id Transaksi: "))
            transaksi1.delete(inptIdTransaksi)
        else:
            tgl_pembayaran = Router.tgl
            nominal = input("Masukkan Nomila: ")
            jenis_transaksi = input("Jenis Transaksi: ")
            santri_id = input("Masukkan id Santri: ")
            pengurus_id = str(pengurus1.getID(input("Masukkan Email Anda: ")))
            ustad_id = input("Masukkan id Ustadz: ")
            transaksi1.create([tgl_pembayaran, nominal, jenis_transaksi,
                               santri_id, pengurus_id, ustad_id])

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
            nama = input("Nama: ")
            email = input("Email: ")
            password = input("Password: ")
            alamat = input("Alamat: ")
            no_hp = input("Nomer HP: ")
            perguruan = input("Perguruan TInggi: ")
            prodi = input("Prodi: ")
            kamar_id = input("Masukkan id Kamar: ")
            santri1.create(
                [nama, email, password, alamat, no_hp, perguruan, prodi, kamar_id])

    def ustadz(self):
        ustadz1 = Ustad()
        if self.x == 1:
            ustadz1.read()
        elif self.x == 2:
            idperubahan = int(input("Masukkan id Ustadz yang dirubah: "))
            nama = input("Nama: ")
            email = input("Email: ")
            password = input("Password: ")
            alamat = input("Alamat: ")
            no_hp = input("Nomer HP: ")
            ustadz1.update([nama, email, password, alamat, no_hp], idperubahan)
        elif self.x == 3:
            inptIdUstadz = int(input("Masukkan Id Ustadz: "))
            ustadz1.delete(inptIdUstadz)
        else:
            nama = input("Nama: ")
            email = input("Email: ")
            password = input("Password: ")
            alamat = input("Alamat: ")
            no_hp = input("Nomer HP: ")
            ustadz1.create([nama, email, password, alamat, no_hp])

    def jagapost(self):
        jagapost1 = JagaPos()
        if self.x == 1:
            jagapost1.read()
        elif self.x == 2:
            idperubahan = int(input("Masukkan id JagaPost yang dirubah: "))
            kamar = input("ID kamar:")
            jagapost1.update([Router.tgl, kamar], idperubahan)
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
        jadwal = JadwalNgaji()
        pengumuman = Pengumuman()
        if self.x == 1:
            tanggal = Router.tgl
            santri1.bayarSPP(tanggal, input("Nominal: "), input('Email: '))
            print(tanggal)
        elif self.x == 2:
            jaga.create([Router.tgl, jaga.getID(
                input("masukkan email: "))])
        elif self.x == 3:
            idUstad = santri1.getID(input("masukkan email: "))
            idKitab = kitab.getID(input("masukkan judul kitab: "))
            absen.create([Router.tgl, idUstad, idKitab])
        elif self.x == 4:
            santri1.getPassword(input("masukkan email anda: "))
        elif self.x == 5:
            email = input("Masukkan email:")
            password = input("Massukkan password:")
            santri1.setPassword(email, password)
        elif self.x == 6:
            jadwal.read(["rolee"])
        elif self.x == 7:
            pengumuman.read(["rolee"])

    def viewUstadz(self):
        ustadz1 = Ustad()
        pengumuman1 = Pengumuman()

        if self.x == 1:
            pass
        elif self.x == 2:
            pengumuman1.read()
        elif self.x == 3:
            pass
        elif self.x == 4:
            pass
        elif self.x == 5:
            pass
        else:
            exit()


# santri1.bayarSPP(Router.tgl, input("nominal: "), input('email: '))
# jaga = JagaPos()
# jaga.create([Router.tgl, '1'])
# print(Router.tgl)
