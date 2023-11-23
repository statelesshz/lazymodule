import importlib.util


def is_torch_available():
    return importlib.util.find_spec("torch") is not None


def is_tf_available():
    return importlib.util.find_spec("tf") is not None
