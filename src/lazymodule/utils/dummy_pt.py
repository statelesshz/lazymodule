from .import_utils import require_torch


class BertEmbeddings:
    def __init__(self):
        require_torch(self)