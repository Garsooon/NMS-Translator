"""Top-level package for NMS Translator."""

__version__ = "0.1.0"  # Fallback version if metadata isn't available

try:
    from importlib.metadata import version, PackageNotFoundError
    __version__ = version("nms-translator")
except PackageNotFoundError:
    # Package not installed, will use fallback version
    pass

# Import key components for ease of access
from .core import translate, load_translations
from .cli import main

__all__ = [
    'translate',
    'load_translations',
    'main',
    '__version__'
]