# some reference:
# https://github.com/huggingface/transformers/pull/9446

__version__ = "0.0.1"

import sys
from typing import TYPE_CHECKING

from .utils import is_tf_available, is_torch_available, _LazyModule


if TYPE_CHECKING:
    from .utils import is_tf_available, is_torch_available
    if is_torch_available():
        from .models import BertEmbeddings
    if is_tf_available():
        from .models import TFBertEmbeddings
else:
    _import_structure = {
        "utils": ["is_tf_available", "is_torch_available"],
    }

    if is_torch_available():
        _import_structure["models"] = ["BertEmbeddings"]
    else:
        from .utils import dummy_pt

        _import_structure["utils.dummy_pt"] = [
            name for name in dir(dummy_pt) if not name.startswith("_")
        ]

    if is_tf_available():
        _import_structure["models"] = ["TFBertEmbeddings"]
    else:
        from .utils import dummy_tf

        _import_structure["utils.dummy_tf"] = [
            name for name in dir(dummy_tf) if not name.startswith("_")
        ]

    sys.modules[__name__] = _LazyModule(
        __name__,
        globals()["__file__"],
        _import_structure,
        module_spec=__spec__,
        extra_objects={"__version__": __version__},
    )
