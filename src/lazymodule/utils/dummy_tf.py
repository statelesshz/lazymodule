from .import_utils import require_tf


class TFBertEmbeddings:
    def __init__(self):
        require_tf(self)