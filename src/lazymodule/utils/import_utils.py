import importlib.util


def is_torch_available():
    return importlib.util.find_spec("torch") is not None


def is_tf_available():
    return importlib.util.find_spec("tf") is not None


PYTORCH_IMPORT_ERROR= """
{0} requires the PyTorch library but it was not found in your environment. Checkout the instructions on
the installation page: https://pytorch.org/get-started/locally/ and follow the ones that match your
environment.
"""


TENSORFLOW_IMPORT_ERROR = """
{0} requires the TensorFlow library but it was not found in your environment. Checkout the instructions on
the installation page: https://www.tensorflow.org/install and follow the ones that match your
environment.
"""

def require_torch(obj):
    name = obj.__name__ if hasattr(obj, "__name__") else obj.__class__.__name__
    if not is_torch_available():
        raise ImportError(PYTORCH_IMPORT_ERROR.format(name))


def require_tf(obj):
    name = obj.__name__ if hasattr(obj, "__name__") else obj.__class__.__name__
    if not is_tf_available():
        raise ImportError(TENSORFLOW_IMPORT_ERROR.format(name))
