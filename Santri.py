from Model import Model


class Post(Model):

    def __init__(self):
        super().__init__("santri", ["title", "body"])
