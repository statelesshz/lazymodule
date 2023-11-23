from ..utils import is_tf_available, is_torch_available

if is_torch_available():
    from .modeling_pt import BertEmbeddings

if is_tf_available():
    from .modeling_tf import TFBertEmbeddings