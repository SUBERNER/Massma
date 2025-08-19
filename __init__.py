import random  # used to keep a consistent random seed and format between all methods and classes

from . import Display
from . import Filter
from .Filter import Logic  # allowing for easier access
from . import Search
from . import Image
from . import Audio
from . import Outer
from . import Inner

from .Methods import seed
from .Methods import move
from .Methods import copy
from .Methods import delete
from .Methods import create_folder
from .Methods import create_file
from .Methods import redo_name
from .Methods import redo_extension
from .Methods import zip
from .Methods import unzip

# used when users uses "from ______ import *
__all__ = [""]

# Pandora's metadata
__version__ = "1.0.1"
__author__ = "SUBERNER"
__license__ = "GNU v3"
__url__ = "https://github.com/SUBERNER/pandora/tree/main"
__description__ = "Python library designed to provide game developers and modders a tool to log, organize, shuffle, and alter files' data and metadata"



