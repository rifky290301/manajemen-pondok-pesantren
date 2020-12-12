from View import View
view1 = View()


def main():
    while(True):
        print("Program Pondok")
        print("""
        1. lihat santri
        2. lihat pengurus
        """)
        inputan = int(input("Masukan Pilihan : "))
        if inputan == 1 or inputan == 2:
            view1.pengurus(inputan)
            break
        else:
            break


main()
