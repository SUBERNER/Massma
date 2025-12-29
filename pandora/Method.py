import random  # used for seeds, all things random should use this
import pandora
import pathlib

def seed(value: int):
    try:
        random.seed(value)  # changed the randomness of the library
        pandora.Display.display_info("method", f"seed <> {value}")
    except Exception as e:
        pandora.Display.display_error("method", f"seed <> {e}")

def move(source: str | list[str]):
    pass

def copy(source: str | list[str]):
    pass

def zip(source: str | list[str]):
    pass

def unzip(source: str | list[str]):
    pass

def delete(source: str | list[str]):
    pass

def redo_name(source: str | list[str]):
    pass

def redo_extension(source: str | list[str]):
    pass

def create_file(source: str | list[str]):
    pass

def create_folder(source: str | list[str]):
    pass

# ==========================================
# INTERNAL METHODS
# ==========================================