import configparser
import os


class DataProvider:
    """DataProvider is a structure holding a map of section names to values,
    obtained from the .config/gnome-games/aisleriot file
    """
    def __init__(self, filename=None):

        # If the user specified a configuration file name, use that.
        # Otherwise, use the default file name, which is
        # ~/.config/gnome-games/aisleriot

        if not filename:
            filename = DataProvider.default_filename()
        
        # Make sure it exists
        if not os.path.exists(filename):
            raise FileNotFoundError(f"{filename} does not exist")
        
        # Create a ConfigParser object and read the .ini file into it
        
        self.config = configparser.ConfigParser()
        self.config.read(filename)
        

    @staticmethod
    def default_filename() -> str:
        """Returns the name of the .ini file containing aisleriot
        configuration and statistics.  Note: in this case, the file
        name does not actually end in ".ini", but its contents are
        in that format.
        """
        config_dir = os.path.expanduser("~/.config")
        filename = os.path.join(config_dir, "gnome-games", "aisleriot")
        return filename