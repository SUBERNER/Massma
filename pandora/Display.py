import pathlib
# main import for displaying information to users
import logging
# formating outputs and making them more understandable
from rich.console import Console
from rich.theme import Theme
from rich.logging import RichHandler
from logging import FileHandler

# Used to better communicate how methods affected files
# Used to make Errors, Warnings and other notifications more noticeable
# Used to distinguish between different typs of alterations
_colors = Theme({
    "debug": "bright_white on black",  # Black Background, allows user to know more about how methods are actually working for debugging
    "info": "bright_white",  # only white text, allows user to see the information about changes made with pandora
    "warning": "bright_white on yellow3",  # Yellow Background, warning users that the input or output might not be what they wanted
    "error": "bright_white on red3",  # Red Background, errors that have stopped the code completely, unless told to ignore
    "critical": "bright_white on orange3",  # orange Background, critical errors will not attempt to run action and will stop code, no matter what
    "display": "bright_white",  # lets users know the alteration was made by the display methods
    "methods": "cyan1",  # lets users know the alteration was made by the display methods
    "search": "green1",  # lets users know the alteration was made by the search methods
    "filters": "blue1",  # lets users know the alteration was made by the filters methods
    "inner": "red1",  # lets users know the alteration was made by the inner methods
    "outer": "yellow1",  # lets users know the alteration was made by the outer methods
    "image": "hot_pink",  # lets users know the alteration was made by the image methods
    "audio": "purple",  # lets users know the alteration was made by the audio methods
})

# logs outputs from alterations into terminals with there being a root and individual for each change type
# changes to root changes all of them but changes to individual only effects that logger
_loggers = {
    'root': logging.getLogger(), # root logger, any changes to this effects all other loggers
    'display': logging.getLogger('display'),
    'methods': logging.getLogger('methods'),
    'search': logging.getLogger('search'),
    'filter': logging.getLogger('filter'),
    'inner': logging.getLogger('inner'),
    'outer': logging.getLogger('outer'),
    'image': logging.getLogger('image'),
    'audio': logging.getLogger('audio')}

# commands used to alter loggers to allow users to get their desired output
def set_format(logger: str | None, *, show_time: bool = None, show_type: bool = None, show_path: bool = None):
    logger = log_testing(logger)
    if logger is None: # displays warning if no logger was found
        # TODO: DISPLAY WARNING
        return
    # get existing handler form logger
    handler = handle_finding(logger, RichHandler)
    if handler is None:  # displays warning if no handler was found
        # TODO: DISPLAY WARNING
        return

    # makes changes to the format of the logger
    if show_time is not None:
        handler._log_render.show_time = show_time
    if show_type is not None:
        handler._log_render.show_type = show_type
    if show_path is not None:
        handler._log_render.show_path = show_type

# gets the current data about how data is formated from the console
def get_format():
    pass

# sets the types of display types that will be displayed in the console
def set_level():
    pass

# gets the types of display types that will be displayed in the console
def get_level():
    pass

# sets how the logger will save the logs made by the console
def set_saving():
    pass

# gets the current data about how data is saved from the console
def get_saving():
    pass

def display_debug():
    pass

def display_info():
    pass

def display_warning():
    pass

def display_error():
    pass

def display_critical():
    pass

# find the logger the system is trying to access
def log_testing(target: str | None):
    if isinstance(target, str): # if a string, it will clean string before testing
        target = target.strip().lower()
    if target == any('', None):  # attempting to access root logger
        return 'root'
    if target in _loggers:  # checks if logger attempting to be altered exists, or if user is trying to access the root logger
        return target
    return None # lets system know an error has occurred and nothing was found

# find the handler the system is trying to access
def handle_finding(target: str | None, handle_type: type):
    target = log_testing(target)
    # goes through each handler to find the one needed
    for handler in logging.getLogger(target).handlers:
        if isinstance(handler, handle_type):
            return handler
    # error will occur if none is provided
    return None


'''
console.print("[debug]The quick brown fox jumps over the lazy dog 1234567890[/debug]")
console.print("[info]The quick brown fox jumps over the lazy dog 1234567890[/info]")
console.print("[warning]The quick brown fox jumps over the lazy dog 1234567890[/warning]")
console.print("[error]The quick brown fox jumps over the lazy dog 1234567890[/error]")
console.print("[critical]The quick brown fox jumps over the lazy dog 1234567890[/critical]")

console.print("[display]The quick brown fox jumps over the lazy dog 1234567890")
console.print("[methods]The quick brown fox jumps over the lazy dog 1234567890")
console.print("[search]The quick brown fox jumps over the lazy dog 1234567890")
console.print("[filters]The quick brown fox jumps over the lazy dog 1234567890")
console.print("[inner]The quick brown fox jumps over the lazy dog 1234567890")
console.print("[outer]The quick brown fox jumps over the lazy dog 1234567890")
console.print("[image]The quick brown fox jumps over the lazy dog 1234567890")
console.print("[audio]The quick brown fox jumps over the lazy dog 1234567890")
'''