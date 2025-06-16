from importlib.metadata import version, PackageNotFoundError

__all__ = ["__version__"]

try:
    __version__ = version("FoxySheep")
except PackageNotFoundError:
    # when running from source, metadata isn’t installed yet
    __version__ = "0.0.0"
