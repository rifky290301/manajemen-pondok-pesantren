from Model import Model


class Pengumuman(Model):

    def __init__(self):
        super().__init__("pengumuman", ["isi_pengumuman", "pengurus_id"])
