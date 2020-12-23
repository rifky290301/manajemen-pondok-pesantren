from Router import Router
from Santri import Santri
from Pengurus import Pengurus
from Ustad import Ustad


def main():
    def MenuLogin():
        print("===SELAMAT DATANG DI PONDOK.In===")
        print("""
    \tLOGIN Pondok.In
    \t1. Pengurus
    \t2. Santri
    \t3. Ustadz
    \t4. Keluar
        """)
        inputSbgUser = int(input("Masukkan angka untuk LOGIN sebagai user : "))
        if inputSbgUser == 1:
            while(Pengurus().login(input("\tNama     : "), input("\tEmail    : "), input("\tPassword : "))):
                print("Inputan Not Found!!!")
            viewPengurus()
        elif inputSbgUser == 2:
            while(Santri().login(input("\tEmail    : "), input("\tPassword : "))):
                print("Inputan Not Found!!!")
            viewSantri()
        elif inputSbgUser == 3:
            while(Santri().login(input("\tEmail    : "), input("\tPassword : "))):
                print("Inputan Not Found!!!")
            viewUstadz()
        elif inputSbgUser == 4:
            exit()
        else:
            print("===Akses User tidak ada / Input Salah!!!===")
            print(" ")

    while True:
        MenuLogin()


def template():
    print("""
        1. Tampilkan Data
        2. Updata Data
        3. Hapus Data
        4. Tambah Data
        5. Kembali Akses Data
    """)
    inputAksesFitur = int(input("Masukkan angka Akses Fitur: "))
    return inputAksesFitur
    if inputAksesFitur == 5:
        viewPengurus()


def viewPengurus():

    def dataTransaksi():
        print("""====AKSES FITUR TRANSAKSI====""")
        fitur = template()
        view1 = Router(fitur)
        if 1 <= fitur <= 4:
            view1.transaksi()
            dataTransaksi()
        else:
            print("Akses Fitur Tidak Ditemukan!!!")

    def dataSantri():
        print("====AKSES FITUR SANTRI====")
        fitur = template()
        view1 = Router(fitur)
        if 1 <= fitur <= 4:
            view1.santri()
            dataSantri()
        else:
            print("Akses Fitur Tidak Ditemukan!!!")

    def dataUstadz():
        print("====AKSES FITUR USTADZ====")
        fitur = template()
        view1 = Router(fitur)
        if 1 <= fitur <= 4:
            view1.ustadz()
            dataUstadz()
        else:
            print("Akses Fitur Ti dak Ditemukan!!!")

    def dataJagaPos():
        print("====AKSES FITUR JAGAPOST====")
        fitur = template()
        view1 = Router(fitur)
        if 1 <= fitur <= 4:
            view1.jagapost()
            dataJagaPos()
        else:
            print("Akses Fitur Tidak Ditemukan!!!")

    def MenuPengurus():
        print(""" =====AKSES DATA=====

    1. Akses Data Transaksi
    2. Askes Data Santri
    3. Akses Data Ustadz
    4. Akses Data Jaga Pos
    5. Kembali Ke Login
        """)
        inputAkses = int(input("Masukkan Angka Akses Data Pilihan: "))
        if inputAkses == 1:
            dataTransaksi()
        elif inputAkses == 2:
            dataSantri()
        elif inputAkses == 3:
            dataUstadz()
        elif inputAkses == 4:
            dataJagaPos()
        elif inputAkses == 5:
            main()
        else:
            print("Akses Data Tidak Ditemukan!!!")
            MenuPengurus()
    while True:
        MenuPengurus()


def viewSantri():
    while(True):
        print("""
        1. Bayar SPP
        2. Absen Jaga Pos
        3. Absen Ngaji
        4. Lihat data diri
        5. Ganti Password
        6. Lihat jadwal mengaji
        """)
        inputFitur = int(input("Masukkan Angka Akses Data Pilihan: "))
        router = Router(inputFitur)
        if 1 <= inputFitur <= 6:
            router.viewSantri()
        else:
            print("Akses Data Tidak Ditemukan!!!")
            exit()


def viewUstadz():
    print("""
    1. Absen mengajar
    2. Absen khotbah
    3. Lihat Jadwal Sendiri
    4. Lihat Jadwal Ustad lain
    """)
    inputFitur = int(
        input("Masukkan angka untuk menggunakna fitur yang ada: "))
    router = Router(inputFitur)
    if 1 <= inputFitur <= 6:
        router.viewUstadz()
    else:
        print("Akses Data Tidak Ditemukan!!!")
        exit()


main()
