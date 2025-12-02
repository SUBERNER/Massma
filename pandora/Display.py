import pathlib
# main import for displaying infomration to users
import logging
# formating outputs and making them more understandable
from rich.console import Console
from rich.theme import Theme
from rich.logging import RichHandler

# Used to better communicate how methods affected files
# Used to make Errors, Warnings and other notifications more noticeable
# Used to distinguish between different typs of alterations
_colors = Theme({
    "debug": "bright_white on black",  # Black Background, allows user to know more about how methods are actually working for debugging
    "info": "bright_white on green3",  # Green Background, notification for something positive or completion
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
    "normal": "bright_white"  # the text style used by default
})

# creates the console for the unique style of output pandora has
console = Console()

# test if the rich colors can be used in the terminal, if not, reverts to legacy colors
if console.is_terminal: console = Console(theme=_colors)
else: pass
# TODO: warn users with warning that it cannot display correctly

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