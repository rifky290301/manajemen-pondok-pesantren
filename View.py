from Santri import Santri
from Pengurus import Pengurus
from Ustad import Ustad
from Transaksi import Transaksi
from Kamar import Kamar
from Kitab import Kitab
from Pengumuman import Pengumuman
from JagaPos import JagaPos


class View:
    def pengurus(x):
        pengurus1 = Pengurus()
        santri1 = Santri()
        if x == 1:
            pengurus1.read()
        elif x == 2:
            santri1.read()
