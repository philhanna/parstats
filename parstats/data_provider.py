import configparser
import os.path


class DataProvider:
    """DataProvider is a structure holding a map of section names to values,
    obtained from the .config/gnome-games/aisleriot file
    """
    def __init__(self, filename=None):
        if not filename:
            filename = DataProvider.default_filename()

    @staticmethod
    def default_filename() -> str:
        """Returns the name of the .ini file containing aisleriot
        configuration and statistics
        """
        config_dir = os.path.expanduser("~/.config")
        filename = os.path.join(config_dir, "gnome-games", "aisleriot.ini")
        return filename