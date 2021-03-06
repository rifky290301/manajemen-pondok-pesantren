import os
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

# instasi variabel global
transaksi1 = Transaksi()
pengurus1 = Pengurus()
# santri1 = Santri("b")
jaga1 = JagaPos()
absen1 = AbsenNgaji()
kitab1 = Kitab()
jadwalngaji1 = JadwalNgaji()
pengumuman1 = Pengumuman()
ustadz1 = Ustad()
kamar1 = Kamar()

os.system('cls')


class Router:
    tgl = datetime.date.today().strftime('%Y-%m-%d')

    def __init__(self, x):
        self.x = x

    def transaksi(self):
        os.system('cls')
        if self.x == 1:
            transaksi1.read()
        elif self.x == 2:
            idperubahan = int(input("Id Transaksi yang dirubah: "))
            tgl_pembayaran = Router.tgl
            nominal = input("Masukkan Nomila: ")
            jenis_transaksi = input("Jenis Transaksi: ")
            santri_id = None
            pengurus_id = str(pengurus1.getID(input("masukkan email: ")))
            ustad_id = None
            transaksi1.update([tgl_pembayaran, nominal, jenis_transaksi,
                               santri_id, pengurus_id, ustad_id], idperubahan)
        elif self.x == 3:
            inptIdTransaksi = int(input("Masukkan id Transaksi: "))
            transaksi1.delete(inptIdTransaksi)
        elif self.x == 4:
            tgl_pembayaran = Router.tgl
            nominal = input("Masukkan Nomila        : ")
            jenis_transaksi = input("Jenis Transaksi        : ")
            santri_id = None
            pengurus_id = str(pengurus1.getID(
                input("Masukkan Email Anda    : ")))
            ustad_id = None
            transaksi1.create([tgl_pembayaran, nominal, jenis_transaksi,
                               santri_id, pengurus_id, ustad_id])
        else:
            print("Pencarian data tidak bisa")

    def santri(self):
        os.system('cls')
        santri1 = Santri()
        if self.x == 1:
            santri1.read()
        elif self.x == 2:
            idperubahan = int(input("Masukkan id perubahan  : "))
            nama = input("Nama                   : ")
            email = input("Email                  : ")
            password = input("Password               : ")
            alamat = input("Alamat                 : ")
            no_hp = input("Nomer HP               : ")
            perguruan = input("Perguruan TInggi       : ")
            prodi = input("Prodi                  : ")
            kamar_id = input("Masukkan id Kamar      : ")
            santri1.update(
                [nama, email, password, alamat, no_hp, perguruan, prodi, kamar_id], idperubahan)
        elif self.x == 3:
            inptIdSantri = int(input("Masukkan Id Santri: "))
            santri1.delete(inptIdSantri)
        elif self.x == 4:
            nama = input("Nama             : ")
            email = input("Email            : ")
            password = input("Password         : ")
            alamat = input("Alamat           : ")
            no_hp = input("Nomer HP         : ")
            perguruan = input("Perguruan TInggi : ")
            prodi = input("Prodi            : ")
            kamar_id = input("Masukkan id Kamar: ")
            santri1.create(
                [nama, email, password, alamat, no_hp, perguruan, prodi, kamar_id])
        else:
            inputt = input(
                "Masukkan Nama atau Email atau Alamat atau Nomer HP: ")
            santri1.search(inputt)

    def ustadz(self):
        os.system('cls')
        if self.x == 1:
            ustadz1.read()
        elif self.x == 2:
            idperubahan = int(input("Masukkan id Ustadz yang dirubah: "))
            nama = input("Nama                               : ")
            email = input("Email                              : ")
            password = input("Password                           : ")
            alamat = input("Alamat                             : ")
            no_hp = input("Nomer HP                           : ")
            ustadz1.update([nama, email, password, alamat, no_hp], idperubahan)
        elif self.x == 3:
            inptIdUstadz = int(input("Masukkan Id Ustadz: "))
            ustadz1.delete(inptIdUstadz)
        elif self.x == 4:
            nama = input("Nama      : ")
            email = input("Email     : ")
            password = input("Password  : ")
            alamat = input("Alamat    : ")
            no_hp = input("Nomer HP  : ")
            ustadz1.create([nama, email, password, alamat, no_hp])
        else:
            inputt = input(
                "Masukkan Nama atau Email atau Alamat atau Nomer HP: ")
            ustadz1.search(inputt)

    def jagapost(self):
        os.system('cls')
        if self.x == 1:
            jaga1.read()
        elif self.x == 2:
            idperubahan = int(input("Masukkan id JagaPost yang dirubah: "))
            kamar = input("ID kamar                         :")
            jaga1.update([Router.tgl, kamar], idperubahan)
        elif self.x == 3:
            inptIdJagapost = int(input("Masukkan Id JagaPost: "))
            jaga1.delete(inptIdJagapost)
        elif self.x == 4:
            kamar = input("ID kamar: ")
            jaga1.create([Router.tgl, kamar])
        else:
            print("Pencarian data tidak bisa")

    def pengurus(self):
        os.system('cls')
        if self.x == 1:
            pengurus1.read()
        elif self.x == 2:
            idperubahan = int(input("Masukkan id JagaPost yang dirubah: "))
            nama = input("Nama                             : ")
            email = input("Email                            : ")
            password = input("Password                         : ")
            alamat = input("Alamat                           : ")
            no_hp = input("Nomer HP                         : ")
            jabatan = input("Jabatan                          : ")
            pengurus1.update([nama, email, password, alamat,
                              no_hp, jabatan], idperubahan)
        elif self.x == 3:
            idPengurus = int(input("Masukkan Id Pengurus: "))
            pengurus1.delete(idPengurus)
        elif self.x == 4:
            nama = input("Nama         : ")
            email = input("Email        : ")
            password = input("Password     : ")
            alamat = input("Alamat       : ")
            no_hp = input("Nomer HP     : ")
            jabatan = input("Jabatan       :")
            pengurus1.create([nama, email, password, alamat, no_hp, jabatan])
        else:
            inputt = input(
                "Masukkan Nama atau Email atau Alamat atau Nomer HP: ")
            pengurus1.search(inputt)

    def absen(self):
        os.system('cls')
        if self.x == 1:
            absen1.read()
        elif self.x == 2:
            print("Tidak bisa update data")
        elif self.x == 3:
            idAbsensi = int(input("Masukkan Id Absensi: "))
            absen1.delete(idAbsensi)
        elif self.x == 4:
            print("Tidak bisa create data")
        else:
            print("Pencarian data tidak bisa")

    def kamar(self):
        os.system('cls')
        if self.x == 1:
            kamar1.read()
        elif self.x == 2:
            idPerubahan = int(input("Masukkan id kamar yang akan diubah: "))
            jumlahKasur = int(input("Masukkan jumlah kasur             :"))
            kamar1.update([jumlahKasur], idPerubahan)
        elif self.x == 3:
            idKamar = int(input("Masukkan Id Kamar: "))
            kamar1.delete(idKamar)
        elif self.x == 4:
            jumlahKasur = int(input("Masukkan jumlah kasur: "))
            kamar1.create([jumlahKasur])
        else:
            print("Pencarian data tidak bisa")

    def kitab(self):
        os.system('cls')
        if self.x == 1:
            kitab1.read()
        elif self.x == 2:
            idPerubahan = int(input("Masukkan id kitab yang akan diubah: "))
            judul = input("Judul kitab                        :")
            pengarang = input("Pengarang kitab                    :")
            penulis = input("Penulis                            :")
            thn = input("Tahun terbit                       :")
            kitab1.update([judul, pengarang, penulis, thn], idPerubahan)
        elif self.x == 3:
            idKitab = int(input("Masukkan Id Kitab: "))
            kitab1.delete(idKitab)
        elif self.x == 4:
            judul = input("Judul kitab      :")
            pengarang = input("Pengarang kitab  :")
            penulis = input("Penulis          :")
            thn = input("Tahun terbit     :")
            kitab1.update([judul, pengarang, penulis, thn])
        else:
            inputt = input(
                "Masukkan Judul atau Pengarang atau Alamat atau Penulis: ")
            kitab1.search(inputt)

    def pengumuman(self):
        os.system('cls')
        if self.x == 1:
            pengumuman1.read()
        elif self.x == 2:
            pengumuman1.update()
        elif self.x == 3:
            inptIdJagapost = int(input("Masukkan Id JagaPost: "))
            pengumuman1.delete(inptIdJagapost)
        elif self.x == 4:
            isi = input("Masukkan Isi Pengumuman : ")
            idPengurus = input("Masukkan Pengurus Id    : ")
            pengumuman1.create([isi, idPengurus])
        else:
            print("Pencarian data tidak bisa")

    def viewSantri(self):
        os.system('cls')
        if self.x == 1:
            tanggal = Router.tgl
            inputEmail = input("Masukkan Email Anda : ")
            santri1 = Santri(inputEmail)
            santri1.bayarSPP(input("Nominal Pembayaran  : "), inputEmail)
            santri1(inputEmail)
        elif self.x == 2:
            inputEmail = (input("Masukkan Email Anda: "))
            jaga1.create([Router.tgl, jaga1.getID(inputEmail)])
            jaga1(inputEmail)
        elif self.x == 3:
            inputEmail = input("Masukkan Email Anda: ")
            santri1 = Santri(inputEmail)
            idSantri = santri1.getID()
            idKitab = kitab1.getID(input("Masukkan Judul Kitab : "))
            idUstad = ustadz1.getID(input("Masukkan Email Ustad :"))
            absen1.create([Router.tgl, str(idSantri),
                           str(idUstad), str(idKitab)])
        elif self.x == 4:
            inputEmail = input("Masukkan Email Anda     : ")
            santri1 = Santri(inputEmail)
            print("Password Anda Adalah    : ", santri1.getPassword())
        elif self.x == 5:
            inputEmail = input("Masukkan Email Anda     : ")
            santri1 = Santri(inputEmail)
            password = input("Massukkan Password Baru : ")
            print("Password Lama           : ", santri1.getPassword())
            santri1.setPassword(password)
            print("Password Baru           : ", santri1.getPassword())
        elif self.x == 6:
            jadwalngaji1.read(["rolee"])
        elif self.x == 7:
            pengumuman1.read(["rolee"])

    def viewUstadz(self):
        os.system('cls')
        if self.x == 1:
            ustad = ustadz1.getID(input("Masukkan Email : "))
            kitab = kitab1.getID(input("Nama Kitab     : "))
            absen1.absenUstad(ustad, kitab)
        elif self.x == 2:
            pengumuman1.read(["ustad"])
        elif self.x == 3:
            idustadz = ustadz1.getID(input("Masukkan Email Anda: "))
            jadwalngaji1.jadwalDewe(idustadz)
        elif self.x == 4:
            jadwalngaji1.read("ustad")
