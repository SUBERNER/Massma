import random  # USED FOR SEEDS

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

# used when users uses "from ___ import *
__all__ = [""]

# Massma metadata
__version__ = "1.0.0"
__author__ = "SUBERNER"
__license__ = "GNU v3"
__url__ = "https://github.com/SUBERNER/Massma"
__description__ = "Python library designed to provide game developers and modders a tool to shuffle and randomizer mass file data and to alter"



