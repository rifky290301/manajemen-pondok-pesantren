from View import View


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
            viewPengurus()
        elif inputSbgUser == 2:
            viewSantri()
        elif inputSbgUser == 3:
            viewUstadz()
        else:
            print("===Akses User tidak ada / Input Salah!!!===")
            print(" ")


def viewPengurus():

    def dataSpp():
        print("""====AKSES FITUR SPP====
        1. Tampilkan Data Spp
        2. Updata Data Spp
        3. Hapus Data Spp
        """)
        inputAksesFitur = int(input("Masukkan angka Akses Fitur Spp: "))
        view1 = View(inputAksesFitur)
        if 1 <= inputAksesFitur <= 3:
            view1.spp()
        else:
            print("Akses Fitur Tidak Ditemukan!!!")

    def dataSantri():
        print("""====AKSES FITUR SANTRI====
        1. Tampilkan Data Santri
        2. Updata Data Santri
        3. Hapus Data Santri
        """)
        inputAksesFitur = int(input("Masukkan angka Akses Fitur Santri: "))
        view1 = View(inputAksesFitur)
        if 1 <= inputAksesFitur <= 3:
            view1.santri()
        else:
            print("Akses Fitur Tidak Ditemukan!!!")

    def dataUstadz():
        print("""====AKSES FITUR USTADZ====
        1. Tampilkan Data Ustadz
        2. Updata Data Ustadz
        3. Hapus Data Ustadz
        """)
        inputAksesFitur = int(input("Masukkan angka Akses Fitur Ustadz: "))
        view1 = View(inputAksesFitur)
        if 1 <= inputAksesFitur <= 3:
            view1.ustadz()
        else:
            print("Akses Fitur Tidak Ditemukan!!!")

    def dataJagapost():
        print("""====AKSES FITUR JAGAPOST====
        1. Tampilkan Data JagaPost
        2. Updata Data JagaPost
        3. Hapus Data JagaPost
        """)
        inputAksesFitur = int(input("Masukkan angka Akses Fitur JagaPost: "))
        view1 = View(inputAksesFitur)
        if 1 <= inputAksesFitur <= 3:
            view1.jagapost()
        else:
            print("Akses Fitur Tidak Ditemukan!!!")

    print(""" ====AKSES DATA====
    1. Akses Data SPP
    2. Askes Data Santri
    3. Akses Data Ustadz
    4. Akses Data JagaPost
    """)
    inputAkses = int(input("Masukkan Angka Akses Data Pilihan: "))
    if inputAkses == 1:
        dataSpp()
    elif inputAkses == 2:
        dataSantri()
    elif inputAkses == 3:
        dataUstadz()
    elif inputAkses == 4:
        dataJagapost()
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
