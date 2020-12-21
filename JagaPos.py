from model import Model


class JagaPos(Model):

    def __init__(self):
        super().__init__("jaga_pos", ["tgl_piket", "kamar_id"])
