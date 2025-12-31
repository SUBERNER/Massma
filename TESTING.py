import pandora

pandora.Display.set_error_quitting("method", False)
pandora.Display.set_error_quitting("image", False)

pandora.seed(pandora)

#pandora.Display.display_info("root", "Show must go on")

pandora.Display.display_debug("outer", "WILL NOT SHOW")
pandora.Display.set_level(["inner","outer","audio","image"], "debug")
pandora.Display.set_level("display", "info")
pandora.Display.set_level("audio", "warning") # help with debugging
pandora.Display.display_debug("outer", "WILL SHOW")
pandora.Display.display_info("outer", "ALWAYS SHOW")

# testing changes based displays
pandora.Display.display_info("inner", "[10] -> [20]")
pandora.Display.display_warning("image", "WARNS OF MAYBE PROBLEMS")
pandora.Display.set_show_date("image", True)
pandora.Display.set_show_path("image", False)
pandora.Display.set_show_date("image", True)
pandora.Display.display_error("image", "WARNS OF ERRORS, FOR NOW WILL NOT STOP CODE")

# testing levels
pandora.Display.set_level("image", "ERROR")
pandora.Display.display_info("search", "ROOT INFO")
pandora.Display.display_warning("search", "ROOT WARNING")
pandora.Display.display_info("audio", "AUDIO INFO")
pandora.Display.display_warning("audio", "AUDIO WARNING")
pandora.Display.display_info("image", "IMAGE INFO")
pandora.Display.display_warning("image", "IMAGE WARNING")
print("-----------------------------------")
pandora.Display.set_level("all", "INFO")
# again after resetting level with root
pandora.Display.display_info("search", "ROOT INFO")
pandora.Display.display_warning("search", "ROOT WARNING")
pandora.Display.display_info("audio", "AUDIO INFO")
pandora.Display.display_warning("audio", "AUDIO WARNING")
pandora.Display.display_info("image", "IMAGE INFO")
pandora.Display.display_warning("image", "IMAGE WARNING")




