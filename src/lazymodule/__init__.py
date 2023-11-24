from .utils import is_tf_available, is_torch_available


if is_torch_available():
    from .models import BertEmbeddings
else:
    from .utils.dummy_pt import BertEmbeddings

if is_tf_available():
    from .models import TFBertEmbeddings
else:
    from .utils.dummy_tf import TFBertEmbeddings
