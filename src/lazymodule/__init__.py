__version__ = "0.0.1"

import sys
from .utils import is_tf_available, is_torch_available, _LazyModule

_import_structure = {
    "utils": ["is_tf_available", "is_torch_available"],
}

if is_torch_available():
    _import_structure["models"] = ["BertEmbeddings"]
else:
    _import_structure["utils.dummy_pt"] = ["BertEmbeddings"]

if is_tf_available():
    _import_structure["models"] = ["TFBertEmbeddings"]
else:
    _import_structure["utils.dummy_tf"] = ["TFBertEmbeddings"]


sys.modules[__name__] = _LazyModule(
    __name__,
    globals()["__file__"],
    _import_structure,
    module_spec=__spec__,
    extra_objects={"__version__": __version__},
)
