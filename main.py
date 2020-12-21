from View import View
from Santri import Santri
from Pengurus import Pengurus
from Ustad import Ustad


def main():
    while(True):
        print("""
    Daftar Pilihan User Pondok.In
    1. Pengurus
    2. Ustadz
    3. Santri
        """)
        inputSbgUser = int(input("Masukkan angka untuk akses sebagai user: "))
        if inputSbgUser == 1:
            while(Pengurus().login()):
            viewPengurus()
        elif inputSbgUser == 2:
            while(Santri().login()):
            viewSantri()
        elif inputSbgUser == 3:
            while(Ustad().login()):
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
        fitur = int(input("Masukkan angka Akses Fitur Ustadz: "))
        view1 = View(fitur)
        if 1 <= fitur <= 4:
            view1.ustadz()
        else:
            print("Akses Fitur Tidak Ditemukan!!!")

    def dataJagapost():
        print("====AKSES FITUR JAGAPOST====")
        fitur = int(input("Masukkan angka Akses Fitur Jaga Pos: "))
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
    4. Akses Data JagaPost
    """)
    inputAkses = int(input("Masukkan Angka Akses Data Pilihan: "))
    if 1 <= inputAkses <= 4:
        dataSpp()
    else:
        print("Akses Data Tidak Ditemukan!!!")
        exit()

    # inputFitur = int(
    #     input("Masukkan angka untuk menggunakna fitur yang ada: "))
    # view1 = View(inputFitur)
    # if inputFitur == 1:
    #     view1.pengurus()
    # elif inputFitur == 2:
    #     view1.pengurus()
    # elif inputFitur == 3:
    #     view1.pengurus()
    # elif inputFitur == 4:
    #     view1.pengurus()
    # elif inputFitur == 5:
    #     # Tampilkan Data Jaga Post
    #     pass
    # elif inputFitur == 6:
    #     # Tampilkan Data Jaga Post
    #     pass
    # elif inputFitur == 7:
    #     # Tampilkan Data Jaga Post
    #     pass
    # else:
    #     pass


def viewSantri():
    print("""
    1. Tampilkan Data Santri
    2. Mengaji
    3. Menyapu
    4. Menjaga Post
    5. Roa'an
    """)
    inputFitur = int(
        input("Masukkan angka untuk menggunakna fitur yang ada: "))
    if inputFitur == 1:
        # Tampilkan Data SPP
        pass
    elif inputFitur == 2:
        # Tampilkan Data Jaga Post
        pass
    elif inputFitur == 3:
        # Tampilkan Data Jaga Post
        pass
    elif inputFitur == 4:
        # Tampilkan Data Jaga Post
        pass
    elif inputFitur == 5:
        # Tampilkan Data Jaga Post
        pass


def viewUstadz():
    print("""
    1. Honor
    2. Mengajar
    3. Lihat Jadwal
    4. Khotbah
    """)
    inputFitur = int(
        input("Masukkan angka untuk menggunakna fitur yang ada: "))
    if inputFitur == 1:
        # Tampilkan Data SPP
        pass
    elif inputFitur == 2:
        # Tampilkan Data Jaga Post
        pass
    elif inputFitur == 3:
        # Tampilkan Data Jaga Post
        pass
    elif inputFitur == 4:
        # Tampilkan Data Jaga Post
        pass

    # print("Program Pondok")
    #  print("""
    #     1. lihat santri
    #     2. lihat pengurus
    #     """)
    #   inputan = int(input("Masukan Pilihan : "))
    #    if inputan == 1 or inputan == 2:
    #         view1.pengurus(inputan)
    #         break
    #     else:
    #         break
main()
