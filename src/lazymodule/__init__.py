from .utils import is_tf_available, is_torch_available

if is_torch_available():
    from .models import BertEmbeddings
else:
    print(f'>>> PyTorch is not available')

if is_tf_available():
    from .models import TFBertEmbeddings
else:
    print(f'>>> TensorFlow is not available')