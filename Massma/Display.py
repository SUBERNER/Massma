import os


class Color:
    # Used to better communicate how methods effected files
    # Used to make Errors and Warnings more noticeable
    ERROR = '\033[41m'  # Red Background, errors that have stopped the code completely, unless told to ignore
    NOTIFY = '\033[42m'  # Green Background, notification for something positive or completion
    WARNING = '\033[43m'  # Yellow Background, warning users that the input or output might not be what they wanted
    RED = '\033[31m'  # Red Text, original value or trait before change or shuffled
    GREEN = '\033[32m'  # Green Text, new value or trait after change or shuffle
    YELLOW = '\033[33m'  # Yellow Text, value or trait is unchanged before and after change or shuffle
    RESET = '\033[0m'  # Removes all effects

    # Used to better communicate the grouping of methods effected files
    # These are the recommend colors to be used, as they are more likely to work with many terminals
    GROUPS = (
        "\033[91m",  # [0] light red
        "\033[31m",  # [1] red
        "\033[92m",  # [2] light green
        "\033[32m",  # [3] green
        "\033[93m",  # [4] light yellow
        "\033[33m",  # [5] yellow
        "\033[94m",  # [6] light blue
        "\033[34m",  # [7] blue
        "\033[95m",  # [8] light purple
        "\033[35m",  # [9] purple
        "\033[96m",  # [10] light cyan
        "\033[36m",  # [11] cyan
        "\033[97m",  # [12] white
        "\033[37m",  # [13] light gray
        "\033[90m",  # [14] dark gray
        "\033[30m",  # [15] black
    )


class Stats:
    altered = 0  # total alters made by a method
    unaltered = 0  # total unalters made by a method
    warnings = 0  # total warnings triggered by a method
    errors = 0  # total errors triggered by a method
    notifications = 0  # total notifications triggered by a method


class Result:
    """
    Manages the display and logging of method results, warnings, and errors.
    """
    _display_alter = True  # Displaying alter and unalter information from a method
    _display_warning = True  # Displaying warning information from a method
    _display_notify = True  # Displaying notification information from a method
    _quit_error = True  # Stops script program while running is an error result appears
    _quit_warning = False  # Stops script program while running is a warning result appears
    _flatten_output = True  # Removed new lines from displaying with outputs
    _source_compression = False  # Shortens the method's source to the last 3 directories
    _source_length = 0  # Minimum amount of space given to the source section of a result for readability
    _method_color = Color.GROUPS[12]  # Colors used for easier method groups identification, white by default
    _stats = Stats  # tracks the running total of changed and triggered activated

    def __init__(self, *, method_color: str = Color.GROUPS[12], display_alter: bool = True, display_warning: bool = True,
                 display_notify: bool = True, source_compression: bool = False, quit_error: bool = True,
                 quit_warning: bool = False, flatten_output: bool = True, source_length: int = 0):
        """
        Initializes the result handler with configurable display options.

        Keyword Parameter:
            method_color (str): Color for method name display. Defaults to white.

            display_alter (bool): Whether to display altered/unaltered results. Defaults to True.

            display_warning (bool): Whether to display warnings. Defaults to True.

            display_notify (bool): Whether to display notifications. Defaults to True.

            source_compression (bool): Whether to shorten source paths to the last 3 directories. Defaults to False.

            quit_error (bool): Whether to terminate script on error. Defaults to True.

            quit_warning (bool): Whether to terminate script on warning. Defaults to False.

            flatten_output (bool): Whether to remove new lines from outputs. Defaults to True.

            source_length (int): Minimum display width for the source column. Defaults to 0.
        """
        try:
            self._display_alter = display_alter
            self._method_color = method_color
            self._display_warning = display_warning
            self._display_notify = display_notify
            self._source_compression = source_compression
            self._quit_error = quit_error
            self._quit_warning = quit_warning
            self._flatten_output = flatten_output
            self._source_length = source_length
        except Exception as e:
            self.result_error(os.getcwd(), "display", str(e))

    def set_display_alter(self, display_alter: bool = None) -> bool:
        """
        Enables or disables the display of altered and unaltered results.

        Parameters:
            display_alter (bool | None): If provided, updates the setting. Otherwise, returns the current value.

        Return:
            bool: Current setting for displaying altered results.
        """
        try:
            # only changes data if not None, use None to only see data
            if display_alter is not None:
                self._display_alter = display_alter
            return self._display_alter
        except Exception as e:
            self.result_error(os.getcwd(), "display", str(e))

    def set_display_warning(self, display_warning: bool = None) -> bool:
        """
        Enables or disables the display of warning messages.

        Parameters:
            display_warning (bool | None): If provided, updates the setting. Otherwise, returns the current value.

        Return:
            bool: Current setting for displaying warnings.
        """
        try:
            # only changes data if not None, use None to only see data
            if display_warning is not None:
                self._display_warning = display_warning
            return self._display_warning
        except Exception as e:
            self.result_error(os.getcwd(), "display", str(e))

    def set_display_notify(self, display_notify: bool = None) -> bool:
        """
        Enables or disables the display of notifications.

        Parameters:
            display_notify (bool | None): If provided, updates the setting. Otherwise, returns the current value.

        Return:
            bool: Current setting for displaying notifications.
        """
        try:
            # only changes data if not None, use None to only see data
            if display_notify is not None:
                self._display_notify = display_notify
            return self._display_notify
        except Exception as e:
            self.result_error(os.getcwd(), "display", str(e))

    def set_flatten_output(self, flatten_output: bool = None) -> bool:
        """
        Enables or disables the removal of new lines in displayed outputs.

        Parameters:
            flatten_output (bool | None): If provided, updates the setting. Otherwise, returns the current value.

        Return:
            bool: Current setting for flattening output.
        """
        try:
            # only changes data if not None, use None to only see data
            if flatten_output is not None:
                self._flatten_output = flatten_output
            return self._flatten_output
        except Exception as e:
            self.result_error(os.getcwd(), "display", str(e))

    def set_source_compression(self, source_compression: bool = None) -> bool:
        """
        Enables or disables compression of file paths to the last 3 directories for display.

        Parameters:
            source_compression (bool | None): If provided, updates the setting. Otherwise, returns the current value.

        Return:
            bool: Current setting for source compression.
        """
        try:
            # only changes data if not None, use None to only see data
            if source_compression is not None:
                self._source_compression = source_compression
            return self._source_compression
        except Exception as e:
            self.result_error(os.getcwd(), "display", str(e))

    def set_quit_error(self, quit_error: bool = None) -> bool:
        """
        Enables or disables automatic termination of the script on an error.

        Parameters:
            quit_error (bool | None): If provided, updates the setting. Otherwise, returns the current value.

        Return:
            bool: Current setting for quitting on errors.
        """
        try:
            # only changes data if not None, use None to only see data
            if quit_error is not None:
                self._quit_error = quit_error
            return self._quit_error
        except Exception as e:
            self.result_error(os.getcwd(), "display", str(e))

    def set_quit_warning(self, quit_warning: bool = None) -> bool:
        """
        Enables or disables automatic termination of the script on a warning.

        Parameters:
            quit_warning (bool | None): If provided, updates the setting. Otherwise, returns the current value.

        Return:
            bool: Current setting for quitting on warnings.
        """
        try:
            # only changes data if not None, use None to only see data
            if quit_warning is not None:
                self._quit_warning = quit_warning
            return self._quit_warning
        except Exception as e:
            self.result_error(os.getcwd(), "display", str(e))

    def set_source_length(self, source_length: int | str = None) -> int:
        """
        Sets the minimum display width for the source column.

        Parameters:
            source_length (int | str | None): If an integer, sets the width directly.
                                              If a string, calculates the width based on the given path.
                                              If None, returns the current value.

        Return:
            int: Current source length setting.
        """
        try:
            # only changes data if not None, use None to only see data
            if source_length is not None:
                if isinstance(source_length, int):  # putting in the length directly
                    self._source_length = source_length
                elif isinstance(source_length, str):  # putting in the length based on source directory length
                    if self._source_compression:
                        limited_parts = source_length.split(os.sep)[-3:]
                        source_length = os.path.join(*limited_parts)
                    self._source_length = len(source_length)
            return self._source_length
        except Exception as e:
            self.result_error(os.getcwd(), "display", str(e))

    def set_method_color(self, method_color: str = None) -> str:
        """
        Sets the color used for displaying method names.

        Parameters:
            method_color (str | None): If provided, updates the color. Otherwise, returns the current color.

        Return:
            str: Current method color setting.
        """
        try:
            if method_color is not None:
                self._method_color = method_color
            return self._method_color
        except Exception as e:
            self.result_error(os.getcwd(), "display", str(e))

    def set_stats(self, alters: int = None, unalters: int = None, warnings: int = None, errors: int = None, notifications: int = None) -> [int, int, int, int, int]:
        """
        Sets or retrieves statistics related to method execution.

        Parameters:
            alters (int | None): Number of altered values. Defaults to None (no change).

            unalters (int | None): Number of unaltered values. Defaults to None (no change).

            warnings (int | None): Number of warnings recorded. Defaults to None (no change).

            errors (int | None): Number of errors recorded. Defaults to None (no change).

            notifications (int | None): Number of notifications recorded. Defaults to None (no change).

        Return:
            list[int]: A list containing [altered, unaltered, warnings, errors, notifications].
        """
        try:
            # only changes data if not None, use None to only see data
            if alters is not None:
                self._stats.altered = alters
            if unalters is not None:
                self._stats.unaltered = unalters
            if warnings is not None:
                self._stats.warnings = warnings
            if errors is not None:
                self._stats.errors = errors
            if notifications is not None:
                self._stats.notifications = notifications
            return [self._stats.altered, self._stats.unaltered, self._stats.warnings, self._stats.errors, self._stats.notifications]
        except Exception as e:
            self.result_error(os.getcwd(), "display", str(e))

    def result(self, source: str, method: str, original_value, updated_value):
        """
        Displays the result of a method, indicating whether a value was altered.

        Parameters:
            source (str): Path of the file or item being altered.

            method (str): Name of the method that was applied.

            original_value: Value before the method was applied.

            updated_value: Value after the method was applied.
        """
        try:
            if self._source_compression:
                limited_parts = source.split(os.sep)[-3:]
                source = os.path.join(*limited_parts)

            if self._flatten_output:
                if isinstance(original_value, str):
                    original_value.replace("\n", "")
                if isinstance(updated_value, str):
                    updated_value.replace("\n", "")

            if original_value != updated_value:  # changed value
                if self._display_alter:
                    print(f"{source:>{self._source_length}} <|> {self._method_color}{method}{Color.RESET} <|>   altered <|> [{Color.RED}{original_value}{Color.RESET}] -> [{Color.GREEN}{updated_value}{Color.RESET}]")
                self._stats.altered += 1  # tracking total "altered" made

            else:  # unchanged value
                if self._display_alter:
                    print(f"{source:>{self._source_length}} <|> {self._method_color}{method}{Color.RESET} <|> unaltered <|> [{Color.YELLOW}{updated_value}{Color.RESET}]")
                self._stats.unaltered += 1  # tracking total "unaltered" made

        except Exception as e:
            self.result_error(f"{source:>{self._source_length}}", method, str(e))

    def result_error(self, source: str, method: str, error: str):
        """
        Displays and handles error messages.

        Parameters:
            source (str): Path of the file or item related to the error.

            method (str): Name of the method that caused the error.

            error (str): Error message.
        """
        try:
            if self._source_compression:
                limited_parts = source.split(os.sep)[-3:]
                source = os.path.join(*limited_parts)

            # add flattening to error in the future

            print(f"{Color.ERROR}{source:>{self._source_length}} <|> {method} <|>     ERROR <|> {error}{Color.RESET}")
            if self._quit_error:
                self._stats.errors += 1  # tracking total "errors" made
                quit()  # ends running code
            self._stats.errors += 1  # tracking total "errors" made

        except Exception as e:
            print(f"{Color.ERROR}{os.getcwd():>{self._source_length}} <|> error <|>     ERROR <|> {e}{Color.RESET}")
            if self._quit_error:
                quit()  # ends running code

    def result_warning(self, source: str, method: str, warning: str):
        """
        Displays a warning message.

        Parameters:
            source (str): Path of the file or item related to the warning.

            method (str): Name of the method issuing the warning.

            warning (str): Warning message.
        """
        try:
            if self._source_compression:
                limited_parts = source.split(os.sep)[-3:]
                source = os.path.join(*limited_parts)

            if self._flatten_output:
                warning = warning.replace("\n", "\t")  # replaces new lines with a tab

            if self._display_warning:  # if warning will be displayed
                print(f"{Color.WARNING}{source:>{self._source_length}} <|> {method} <|>   WARNING <|> {warning}{Color.RESET}")
                if self._quit_warning:
                    self._stats.warnings += 1  # tracking total "warnings" made
                    quit()  # ends running code
            self._stats.warnings += 1  # tracking total "warnings" made

        except Exception as e:
            self.result_error(f"{source:>{self._source_length}}", method, str(e))

    def result_notify(self, source: str, method: str, notification: str):
        """
        Displays a notification message.

        Parameters:
            source (str): Path of the file or item related to the notification.

            method (str): Name of the method issuing the notification.

            notification (str): Notification message.
        """
        try:
            if self._source_compression:
                limited_parts = source.split(os.sep)[-3:]
                source = os.path.join(*limited_parts)

            if self._flatten_output:
                notification = notification.replace("\n", "\t")  # replaces new lines with a tab

            if self._display_notify:  # if notification will be displayed
                print(f"{Color.NOTIFY}{source:>{self._source_length}} <|> {method} <|>    NOTIFY <|> {notification}{Color.RESET}")
            self._stats.notifications += 1  # tracking total "notifications" made

        except Exception as e:
            self.result_error(f"{source:>{self._source_length}}", method, str(e))


# PLACE RESULT INSTANCES HERE FOR ORGANIZED ACCESS
outer = Result(method_color=Color.GROUPS[10])
inner = Result(method_color=Color.GROUPS[6])
image = Result(method_color=Color.GROUPS[4])
methods = Result(method_color=Color.GROUPS[12])
search = Result(method_color=Color.GROUPS[0])
audio = Result(method_color=Color.GROUPS[2])
filter = Result(method_color=Color.GROUPS[8])
