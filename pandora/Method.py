import random  # used for seeds, all things random should use this
import pandora
import pathlib
import shutil

def seed(value):
    try:
        random.seed(value)  # changed the randomness of the library
        pandora.Display.display_info("method", f"seed <> {value}")
        return value
    except Exception as e:
        pandora.Display.display_error("method", f"seed <> {e}")
        return None

def move(sources: str | list[str], destination: str):
    try:
        results = [] # the new locations of the moved files and folders
        # makes sure source is a list
        sources = source_list(sources)
        # makes the effect for each source
        for source in sources:
            try:
                if not exist_test(source, "move", True): # ends loop if file could not be found and warns user give an error
                    continue
                destination = shutil.move(source, destination)  # adds the file or folder form the source into the destination
                results.append(destination) # adds source to list of competed/altered sources to be listed for the user
                pandora.Display.display_info("method", f"move <> {pathlib.Path(source)} -> {pathlib.Path(destination)}")
            except Exception as e:
                pandora.Display.display_error("method", f"move <> {e}")
            return result_correction(results)
    except Exception as e:
        pandora.Display.display_error("method", f"move <> {e}")
        return None

def copy(sources: str | list[str], destination: str):
    try:
        results = [] # the new locations of the copied files and folders
        # makes sure source is a list
        sources = source_list(sources)
        # makes the effect for each source
        for source in sources:
            try:
                if not exist_test(source, "copy", True): # ends loop if file could not be found and warns user give an error
                    continue
                elif pathlib.Path(source).is_file():  # copying files
                    destination = shutil.copy2(source, destination) # adds the file or folder form the source into the destination
                elif pathlib.Path(source).is_dir():  # copying folders
                    destination = shutil.copytree(source, destination) # adds the file or folder form the source into the destination
                results.append(destination) # adds source to list of competed/altered sources to be listed for the user
                pandora.Display.display_info("method", f"copy <> {pathlib.Path(source)} -> {pathlib.Path(destination)}")
            except Exception as e:
                pandora.Display.display_error("method", f"copy <> {e}")
            return result_correction(results)
    except Exception as e:
        pandora.Display.display_error("method", f"copy <> {e}")
        return None

def zip(sources: str | list[str], extension: str):
    try:
        results = [] # the names of all new zip files
        # makes sure source is a list
        sources = source_list(sources)
        # makes the effect for each source
        for source in sources:
            try:
                if not exist_test(source, "zip", True): # ends loop if file could not be found and warns user give an error
                    continue
                extension = extension.lower().strip().replace(".", "") #cleanups extension
                destination = shutil.make_archive(source, extension, source) # zips files
                results.append(destination) # adds source to list of competed/altered sources to be listed for the user
                pandora.Display.display_info("method", f"zip <> {destination}")
            except Exception as e:
                pandora.Display.display_error("method", f"zip <> {e}")
        return result_correction(results)
    except Exception as e:
        pandora.Display.display_error("method", f"zip <> {e}")
        return None

def unzip(sources: str | list[str]):
    try:
        results = [] # the names of all new unzip files
        # makes sure source is a list
        sources = source_list(sources)
        # makes the effect for each source
        for source in sources:
            try:
                if not exist_test(source, "unzip", True): # ends loop if file could not be found and warns user give an error
                    continue
                
                #gets zip file to remove the extension for destination
                destination = pathlib.Path(source).with_suffix("")
                # converts form zip to none zip
                destination = shutil.unpack_archive(source, destination)
                results.append(destination) # adds source to list of competed/altered sources to be listed for the user
                pandora.Display.display_info("method", f"unzip  <> {destination}")
            except Exception as e:
                pandora.Display.display_error("method", f"unzip  <> {e}")
        return result_correction(results)
    except Exception as e:
        pandora.Display.display_error("method", f"unzip  <> {e}")
        return None

def delete(sources: str | list[str]):
    try:
        results = [] # the amount fo files that where deleted in Nones
        # makes sure source is a list
        sources = source_list(sources)
        # makes the effect for each source
        for source in sources:
            try:
                if not exist_test(source, "delete", False): # ends loop if file could not be found and warns user give an error
                    continue
                elif pathlib.Path(source).is_file():  # copying files
                    pathlib.Path(source).unlink() # deletes the file
                elif pathlib.Path(source).is_dir():  # copying folders
                    shutil.rmtree(source) # deletes the folder
                results.append(None) # adds source to list of competed/altered sources to be listed for the user
                pandora.Display.display_info("method", f"delete <> {source} -> None")
            except Exception as e:
                pandora.Display.display_error("method", f"delete <> {e}")
        return result_correction(results)
    except Exception as e:
        pandora.Display.display_error("method", f"delete <> {e}")
        return None

def redo_name(sources: str | list[str], name: str):
    try:
        results = [] # the new files that have new names
        # makes sure source is a list
        sources = source_list(sources)
        # makes the effect for each source
        for source in sources:
            try:
                if not exist_test(source, "redo name", True): # ends loop if file could not be found and warns user give an error
                    continue
                # changes only the files name and not directory
                new_source = pathlib.Path(source)
                destination = new_source.with_name(name)
                new_source.rename(destination)
                results.append(destination) # adds source to list of competed/altered sources to be listed for the user
                pandora.Display.display_info("method", f"redo name <> {source} -> {destination.name}")
            except Exception as e:
                pandora.Display.display_error("method", f"redo name <> {e}")
        return result_correction(results)
    except Exception as e:
        pandora.Display.display_error("method", f"zip <> {e}")
        return None

def redo_extension(sources: str | list[str], extension: str):
    try:
        results = [] # the new files that have new extensions
        # makes sure source is a list
        sources = source_list(sources)
        # makes the effect for each source
        for source in sources:
            try:
                if not exist_test(source, "redo_extension", True): # ends loop if file could not be found and warns user give an error
                    continue
                # changes only the files extension and not name
                new_source = pathlib.Path(source)
                destination = new_source.with_suffix(extension)
                new_source.rename(destination)
                results.append(destination) # adds source to list of competed/altered sources to be listed for the user
                pandora.Display.display_info("method", f"redo extension <> {source} -> {destination.name}")
            except Exception as e:
                pandora.Display.display_error("method", f"redo extension <> {e}")
        return result_correction(results)
    except Exception as e:
        pandora.Display.display_error("method", f"redo extension <> {e}")
        return None

def create_file(sources: str | list[str]):
    try:
        results = [] # the new files that where made
        # makes sure source is a list
        sources = source_list(sources)
        # makes the effect for each source
        for source in sources:
            try:
                with open(source, 'x') as file: # creates file
                    pass
                results.append(pathlib.Path(source)) # adds source to list of competed/altered sources to be listed for the user
                pandora.Display.display_info("method", f"create file <> {source}")
            except Exception as e:
                pandora.Display.display_error("method", f"create file <> {e}")
        return result_correction(results)
    except Exception as e:
        pandora.Display.display_error("method", f"create file <> {e}")
        return None

def create_folder(sources: str | list[str]):
    try:
        results = [] # the new folders that where made
        # makes sure source is a list
        sources = source_list(sources)
        # makes the effect for each source
        for source in sources:
            try:
                pathlib.Path(source).mkdir(parents=True) # creates folder
                results.append(pathlib.Path(source)) # adds source to list of competed/altered sources to be listed for the user
                pandora.Display.display_info("method", f"create folder <> {source}")
            except Exception as e:
                pandora.Display.display_error("method", f"create folder <> {e}")
        return result_correction(results)
    except Exception as e:
        pandora.Display.display_error("method", f"create folder <> {e}")
        return None

# ==========================================
# INTERNAL METHODS
# ==========================================
def source_list(sources: str | list[str]): # makes sures all strings of sources are turned into lists
    if isinstance(sources, str): # converts to list if str
        return [sources.strip()] # strips to remove a missinput
    else: # if already a list
        return [source.strip() for source in sources]
    
def exist_test(source: str, method: str , error: bool): # makesw sure a file or folder exists before trying to do anything with
    if not pathlib.Path(source).exists(): # ends loop if file could not be found and warns user
        if error: # if the test fails it will result in an error, not a warning
            pandora.Display.display_error("method", f"{method} <> Could not find {source}")
        else: # results in a warning not a error, use if the file not existing changes nothing
            pandora.Display.display_warning("method", f"{method} <> Could not find {source}")
        return False # file or folder does not exist
    return True # file or folder does exist

def result_correction(sources: list[str]): # corrects results to allow user to effectivly use the output of methods
    if len(sources) == 1: # only one source in the list
        return sources[0]
    elif len(sources) == 0: # no sources worked in the methods
        return None
    else:
        return sources # keeps sources a list if more than one source is in it