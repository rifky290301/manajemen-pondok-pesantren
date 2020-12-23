from model import Model


class Transaksi(Model):

    def __init__(self):
        super().__init__("transaksi", [
            "tgl_pembayaran", "nominal", "jenis_transaksi", "santri_id", "pengurus_id", "ustad_id"])
