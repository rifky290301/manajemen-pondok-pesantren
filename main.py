from Router import Router
from Santri import Santri
from Pengurus import Pengurus
from Ustad import Ustad


def main():
    while(True):
        print("""
    Daftar Pilihan User Pondok.In
    1. Pengurus
    2. Santri
    3. Ustadz
        """)
        inputSbgUser = int(input("Masukkan angka untuk akses sebagai user: "))
        if inputSbgUser == 1:
            while(Pengurus().login(input("nama"), input("email:"), input("password:"))):
                print("mungkin ada yang salah")
            viewPengurus()
        elif inputSbgUser == 2:
            while(Santri().login(input("email:"), input("password:"))):
                print("mungkin ada yang salah")
            viewSantri()
        elif inputSbgUser == 3:
            while(Santri().login(input("email:"), input("password:"))):
                print("mungkin ada yang salah")
            viewUstadz()
        else:
            print("===Akses User tidak ada / Input Salah!!!===")
            print(" ")


def template():
    print("""
        1. Tampilkan Data
        2. Updata Data
        3. Hapus Data
        4. Tambah Data
    """)
    inputAksesFitur = int(input("Masukkan angka Akses Fitur: "))
    return inputAksesFitur


def viewPengurus():

    def dataSpp():
        print("""====AKSES FITUR SPP====""")
        fitur = template()
        # inputAksesFitur = int(input("Masukkan angka Akses Fitur Spp: "))
        view1 = View(fitur)
        if 1 <= fitur <= 4:
            view1.spp()
        else:
            print("Akses Fitur Tidak Ditemukan!!!")

    def dataSantri():
        print("====AKSES FITUR SANTRI====")
        # 1. Tampilkan Data Santri
        # 2. Updata Data Santri
        # 3. Hapus Data Santri
        # """)
        fitur = template()
        # inputAksesFitur = int(input("Masukkan angka Akses Fitur Santri: "))
        view1 = View(fitur)
        if 1 <= fitur <= 4:
            view1.santri()
        else:
            print("Akses Fitur Tidak Ditemukan!!!")

    def dataUstadz():
        print("====AKSES FITUR USTADZ====")
        fitur = template()
        view1 = View(fitur)
        if 1 <= fitur <= 4:
            view1.ustadz()
        else:
            print("Akses Fitur Tidak Ditemukan!!!")

    def dataJagaPos():
        print("====AKSES FITUR JAGAPOST====")
        fitur = template()
        view1 = View(fitur)
        if 1 <= fitur <= 3:
            view1.jagapost()
        else:
            print("Akses Fitur Tidak Ditemukan!!!")

    def dataTransaksi():
        pass

    print(""" ====AKSES DATA====
    1. Akses Data SPP
    2. Askes Data Santri
    3. Akses Data Ustadz
    4. Akses Data Jaga Pos
    """)
    inputAkses = int(input("Masukkan Angka Akses Data Pilihan: "))
    if 1 <= inputAkses <= 4:
        dataSpp()
    else:
        print("Akses Data Tidak Ditemukan!!!")
        exit()


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
            router.viewSantri()
        else:
            print("Akses Data Tidak Ditemukan!!!")
            exit()


main()
