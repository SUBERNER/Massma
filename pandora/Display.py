# main import for displaying information to users
import logging
# formating outputs and making them more understandable
from rich.console import Console
from rich.theme import Theme
from rich.logging import RichHandler
from rich.text import Text

# Used to better communicate how methods affected files
# Used to make Errors, Warnings and other notifications more noticeable
# Used to distinguish between different typs of alterations
_colors = Theme({
    "logging.level.debug": "bright_white",  # only white text, allows user to know more about how methods are actually working for debugging
    "logging.level.info": "bright_white on black",  # Black Background, allows user to see the information about changes made with pandora
    "logging.level.warning": "bright_white on yellow3",  # Yellow Background, warning users that the input or output might not be what they wanted
    "logging.level.error": "bright_white on red3",  # Red Background, errors that have stopped the code completely, unless told to ignore
    "logging.level.critical": "bright_white on orange3",  # orange Background, critical errors will not attempt to run action and will stop code, no matter what
    "display": "bright_white",  # lets users know the alteration was made by the display methods
    "method": "cyan1",  # lets users know the alteration was made by the display methods
    "search": "green1",  # lets users know the alteration was made by the search methods
    "filter": "blue3",  # lets users know the alteration was made by the filters methods
    "inner": "red1",  # lets users know the alteration was made by the inner methods
    "outer": "yellow1",  # lets users know the alteration was made by the outer methods
    "image": "hot_pink",  # lets users know the alteration was made by the image methods
    "audio": "purple",  # lets users know the alteration was made by the audio methods
})

# custom logger variables used for special atributes
_configs = {
    "logger": None, # will store the logger itself
    "quit_error": True,
    "quit_warning": False
}

# Setup for the default configurations of the loggers
# Sets up console and handler to correctly display the logs
_console = Console(theme=_colors)
# logs outputs from alterations into terminals with there being a root and individual for each change type
_loggers = {} # stotres each log and the additional variables they have
# creates each logger and direcotery to access its variables
for key in ['display','method','search','filter','inner','outer','image','audio']:

    _rich_handler = RichHandler(console=_console, markup=True, omit_repeated_times= False, log_time_format = "", show_time=False, show_path=False)
    _rich_handler.setFormatter(logging.Formatter("[%(name)s]%(name)+6s[/%(name)s] <> %(message)s"))

    _loggers[key] = _configs.copy()
    _loggers[key]["logger"] = logging.getLogger(key)
    _loggers[key]["logger"].addHandler(_rich_handler) # allows for configuring the log's format
    _loggers[key]["logger"].propagate = False # stops sending the messages to root to stop double printing
    _loggers[key]["logger"].setLevel("INFO") # sets default level to info

# ==========================================
# GETS & SETS METHODS
# ==========================================

# sets and gets if errors will cause the program to stop
def set_error_quitting(loggers: str | list[str], error_quitting: bool):
    
    loggers = log_list(loggers) # gets and formats all loggers
    for log in loggers:
        log = log_testing(log)
        if log is None: # displays warning if no logger was found
            continue
        _loggers[log]["quit_error"] = error_quitting
   
def get_error_quitting(logger: str):
    logger = log_testing(logger)
    if logger is None: # displays warning if no logger was found
        return None
    return _loggers[logger]["quit_error"]
    

# sets and gets if warning will cause the program to stop
def set_warning_quitting(loggers: str | list[str], warning_quitting: bool):
    loggers = log_list(loggers) # gets and formats all loggers
    for log in loggers:
        log = log_testing(log)
        if log is None: # displays warning if no logger was found
            continue
        _loggers[log]["quit_warning"] = warning_quitting
   
def get_warning_quitting(logger: str):
    logger = log_testing(logger)
    if logger is None: # displays warning if no logger was found
        return None
    return _loggers[logger]["quit_warning"]


# sets and gets the types of display types that will be displayed in the console
def set_level(loggers: str | list[str], level: str):
    loggers = log_list(loggers) # gets and formats all loggers
    for log in loggers:
        log = log_testing(log)
        if log is None: # displays warning if no logger was found
            continue
        # changes the minimum level log that will be displayed    
        _loggers[log]["logger"].setLevel(level.strip().upper()) # make sure into its all uppercase

def get_level(logger: str | None):
    logger = log_testing(logger)
    if logger is None: # displays warning if no logger was found
        return None
    # sends back the current level of the minimum allowed displayed
    return logging.getLevelName(_loggers[logger]["logger"].getEffectiveLevel())


# sets and gets if the level of the log is shown
def set_show_level(loggers: str | list[str], show_level: bool):
    loggers = log_list(loggers) # gets and formats all loggers
    for log in loggers:
        log = log_testing(log)
        if log is None: # displays warning if no logger was found
            continue
        
        # get existing handler form logger
        handler = handle_finding(log, RichHandler)
        if handler is None:  # displays warning if no handler was found
            return None
        
        handler._log_render.show_level = show_level
    
def get_show_level(logger: str | None):
    logger = log_testing(logger)
    if logger is None: # displays warning if no logger was found
        return None
        # get existing handler form logger
    handler = handle_finding(logger, RichHandler)
    if handler is None:  # displays warning if no handler was found
        return None
    
    return handler._log_render.show_level


# sets and gets if the time of the log being displayed is shown
def set_show_time(loggers: str | list[str], show_time: bool):
    loggers = log_list(loggers) # gets and formats all loggers
    for log in loggers:
        log = log_testing(log)
        if log is None: # displays warning if no logger was found
            continue

        # get existing handler form logger
        handler = handle_finding(log, RichHandler)
        if handler is None:  # displays warning if no handler was found
            return None
        
        # determines how to format the data and time, if both data and time are not shown, it will simply turn of the displaying
        # if one of them is true, it will set either only time, only date, or both
        show_date = get_show_date(log)
        handler._log_render.time_format = date_time_format(show_date, show_time)
        if handler._log_render.time_format == "": # no date or data will be displayed
            handler._log_render.show_time = False
        else:
            handler._log_render.show_time = True 
    
def get_show_time(logger: str):
    logger = log_testing(logger)
    if logger is None: # displays warning if no logger was found
        return None
    # get existing handler form logger
    handler = handle_finding(logger, RichHandler)
    if handler is None:  # displays warning if no handler was found
        return None

    # simply stats true or false if there is any resemblence of a time being displayed
    if "%H:%M:%S" in handler._log_render.time_format:
        return True
    else:
        return False


# sets and gets if the date of the log being displayed is shown
def set_show_date(loggers: str | list[str], show_date: bool):
    loggers = log_list(loggers) # gets and formats all loggers
    for log in loggers:
        log = log_testing(log)
        if log is None: # displays warning if no logger was found
            continue
        # get existing handler form logger
        handler = handle_finding(log, RichHandler)
        if handler is None:  # displays warning if no handler was found
            return None
        # determines how to format the data and time, if both data and time are not shown, it will simply turn of the displaying
        # if one of them is true, it will set either only time, only date, or both
        show_time = get_show_time(log)
        handler._log_render.time_format = date_time_format(show_date, show_time)
        if handler._log_render.time_format == "": # no date or data will be displayed
            handler._log_render.show_time = False
        else:
            handler._log_render.show_time = True
    
def get_show_date(logger: str):
    logger = log_testing(logger)
    if logger is None: # displays warning if no logger was found
        return None
        # get existing handler form logger
    handler = handle_finding(logger, RichHandler)
    if handler is None:  # displays warning if no handler was found
        return None
    
    # simply stats true or false if there is any resemblence of a date being displayed
    if "%Y-%m-%d" in handler._log_render.time_format:
        return True
    else:
        return False


# sets and gets if the path and location of where the log was sent from is shown
def set_show_path(loggers: str | list[str], show_path: bool):
    loggers = log_list(loggers) # gets and formats all loggers
    for log in loggers:
        log = log_testing(log)
        if log is None: # displays warning if no logger was found
            continue
        # get existing handler form logger
        handler = handle_finding(log, RichHandler)
        if handler is None:  # displays warning if no handler was found
            return None
        
        handler._log_render.show_path = show_path
    
def get_show_path(logger: str):
    logger = log_testing(logger)
    if logger is None: # displays warning if no logger was found
        return None
    # get existing handler form logger
    handler = handle_finding(logger, RichHandler)
    if handler is None:  # displays warning if no handler was found
        return None
    
    return handler._log_render.show_path


# sets and gets if a user can click a link to be sent to the location of the sent log
def set_link_path(loggers: str | list[str], link_path: bool):
    loggers = log_list(loggers) # gets and formats all loggers
    for log in loggers:
        log = log_testing(log)
        if log is None: # displays warning if no logger was found
            continue
        # get existing handler form logger
        handler = handle_finding(log, RichHandler)
        if handler is None:  # displays warning if no handler was found
            return None
        
        handler._log_render.link_path = link_path
    
def get_link_path(logger: str):
    logger = log_testing(logger)
    if logger is None: # displays warning if no logger was found
        return None
        # get existing handler form logger
    handler = handle_finding(logger, RichHandler)
    if handler is None:  # displays warning if no handler was found
        return None
    
    return handler._log_render.link_path

# ==========================================
# LOGGING OUTPUT METHODS
# ==========================================

def display_debug(logger: str, message: str):
    logger = log_testing(logger)
    if logger is None: # displays warning if no logger was found
        return None
    # displays debugging based messages
    _loggers[logger]["logger"].debug(message)

def display_info(logger: str, message: str):
    logger = log_testing(logger)
    if logger is None: # displays warning if no logger was found
        return None
    # displays information based messages about the results of the changes
    _loggers[logger]["logger"].info(message)

def display_warning(logger: str, message: str):
    logger = log_testing(logger)
    if logger is None: # displays warning if no logger was found
        return None
    # displays warnings based messages about what the user should be notifyed about that could alter desired outputs
    _loggers[logger]["logger"].warning(message)
    if _loggers[logger]["quit_warning"] == True:
        quit() # ends running code

def display_error(logger: str, message: str):
    logger = log_testing(logger)
    if logger is None: # displays warning if no logger was found
        return None
    # displays error based messages that could cause the program to not run correctly
    _loggers[logger]["logger"].error(message)
    if _loggers[logger]["quit_error"] == True:
        quit() # ends running code

def display_critical(logger: str, message: str):
    logger = log_testing(logger)
    if logger is None: # displays warning if no logger was found
        return None
    # displays critical error based messages that cannot be ignored no matter what
    _loggers[logger]["logger"].critical(message)
    quit()  # you cannot turn off critical quits, no matter what

# ==========================================
# INTERNAL METHODS
# ==========================================

# find the logger the system is trying to access to make sure it exists
def log_testing(target: str):
    target = target.strip().lower() # clean string beofre testing
    if target in _loggers.keys():  # checks if logger attempting to be altered exists, or if user is trying to access the root logger
        return target
    # warning will occur if none is provided
    display_warning("display", f"Could not find {target} Logger")
    return None # lets system know an error has occurred and nothing was found

# find the handler the system is trying to access
def handle_finding(target: str, handle_type: type):
    target = log_testing(target)
    # goes through each handler to find the one needed
    for handler in logging.getLogger(target).handlers:
        display_debug('display', f"Handler: {handler}") # DEBUG LOG
        if isinstance(handler, handle_type):
            return handler
    # warning will occur if none is provided
    display_warning("display", f"Could not find {target} Handler")
    return None

# correctly displays the date and time based on users wants
def date_time_format(show_date: bool, show_time: bool):
    if show_date and show_time:
        return "[%Y-%m-%d %H:%M:%S]"
    elif not show_date and show_time:
        return "[%H:%M:%S]"
    elif show_date and not show_time:
        return "[%Y-%m-%d]"
    else: # both date and time are now showing
        return "" # tell method to stop displaying time
    
# converts loggers into lists for easier managing
def log_list(loggers: str | list[str]):
    if isinstance(loggers, str):
        if loggers.strip().lower() == "all": # if user select all, it will automatically get all loggers for user to change at once
            return _loggers.keys()
        else:
            return [loggers]
    elif isinstance(loggers, list):
        return loggers

