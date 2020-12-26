from model import Model


class JadwalNgaji(Model):
    def __init__(self):
        super().__init__("jadwal", ["hari", "waktu", "ustad_id", "kitab_id"])
