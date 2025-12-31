import random  # used for seeds, all things random should use this
import pandora
import pathlib
import shutil

def seed(value: int):
    try:
        random.seed(value)  # changed the randomness of the library
        pandora.Display.display_info("method", f"seed <> {value}")
    except Exception as e:
        pandora.Display.display_error("method", f"seed <> {e}")

def move(source: str | list[str], destination: str):
    try:
        destination = shutil.move(source, destination) # redoes destination to
        pandora.Display.display_info("method", f" move <> {pathlib.Path(source).parts[:-2]} -> {pathlib.Path(source).parts[:-2]}")
    except Exception as e:
        pandora.Display.display_error("method", f" move <> {e}")

def copy(source: str | list[str], destination: str):
    try:
        if pathlib.Path.is_file(source):  # copying files
            destination = shutil.copy2(source, destination)
        elif pathlib.Path.is_dir(source):  # copying folders
            destination = shutil.copytree(source, destination)
        pandora.Display.display_info("method", f" copy <> {source} -> {destination}")
    except Exception as e:
        pandora.Display.display_error("method", f" copy <> {e}")

def zip(source: str | list[str]):
    try:
        pandora.Display.display_info("method", f" zip <> {}")
    except Exception as e:
        pandora.Display.display_error("method", f" zip <> {e}")

def unzip(source: str | list[str]):
    try:
        pandora.Display.display_info("method", f" unzip <> {}")
    except Exception as e:
        pandora.Display.display_error("method", f" unzip <> {e}")

def delete(source: str | list[str]):
    try:
        pandora.Display.display_info("method", f" delete <> {}")
    except Exception as e:
        pandora.Display.display_error("method", f" delete <> {e}")

def redo_name(source: str | list[str]):
    try:
        pandora.Display.display_info("method", f" redo_name <> {}")
    except Exception as e:
        pandora.Display.display_error("method", f" redo_name <> {e}")

def redo_extension(source: str | list[str]):
    try:
        pandora.Display.display_info("method", f" redo_extension <> {}")
    except Exception as e:
        pandora.Display.display_error("method", f" redo_extension <> {e}")

def create_file(source: str | list[str]):
    try:
        pandora.Display.display_info("method", f" create_file <> {}")
    except Exception as e:
        pandora.Display.display_error("method", f" create_file <> {e}")

def create_folder(source: str | list[str]):
    try:
        pandora.Display.display_info("method", f" create_folder <> {}")
    except Exception as e:
        pandora.Display.display_error("method", f" create_folder <> {e}")

# ==========================================
# INTERNAL METHODS
# ==========================================