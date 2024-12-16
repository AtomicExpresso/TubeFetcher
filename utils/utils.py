from utils.config import Config
from tkinter import messagebox
import json
import os
import sys


# Used for general utility commands, such as calculating time, file size, etc.
class Utils:
    #Gets abs file path for files, so it will compile correctly
    def get_resource_path(relative_path: str):
        if getattr(sys, 'frozen', False):
            # Running in a bundled app
            app_path = sys._MEIPASS
        else:
            # Running in script mode
            app_path = os.path.abspath(".")
    
        return os.path.join(app_path, relative_path)

    # Calculate total elapsed time for videos/audio
    def calculate_Time(time) -> str:
        try:
            hrs: int = time // 3600
            mins: int = (time % 3600) // 60
            secs: int = time % 60

            elapsed_time: str = "{h}:{m}:{s}".format(h=hrs, m=mins, s=secs)

            return elapsed_time
        except:
            raise ValueError("An error occured while calculating time")

    # Calculates file size for videos/audio
    def calculate_file_size(cur) -> str:
        try:
            # Change file size based on stream, division converts it from bytes to megabytes and rounds 2 decimal places
            file_size = cur["stream"].filesize / 1048576
            mb_size = f"{file_size:.2f} MB"

            return mb_size
        except:
            raise ValueError("An error occured while calculating file size")

    # Save settings data
    @classmethod
    def save_settings_data(self) -> None:
        data = {
            "res_type": Config.res_cur_option,
            "dl_type": Config.dl_cur_option,
            "folder_path": Config.folder_path,
            "theme": Config.theme_cur_option,
        }
        settings_path = self.get_resource_path("settings/settings.json")
        with open(settings_path, "w") as file:
            json.dump(data, file)

    # Fetch save data
    @classmethod
    def load_settings_data(self) -> None:
        try:
            self.save_settings_data()
            settings_path = self.get_resource_path("settings/settings.json")
            with open(settings_path, "r") as file:
                data = json.load(file)

            if data["dl_type"] in Config.dl_options:
                Config.dl_cur_option = data["dl_type"]
            if data["res_type"] in Config.res_options:
                Config.res_cur_option = data["res_type"]
            if data["theme"] in Config.theme_options:
                Config.theme_cur_option = data["theme"]
            if data["folder_path"]:
                print(Config.folder_path)
                Config.folder_path = data["folder_path"]
        except:
            self.save_settings_data()

    # used for dialog notifications
    @classmethod
    def create_dialog_notfication(self, msg: str) -> None:
        messagebox.showinfo("Notification", f"{msg}")

    # used for dialog error notifications
    @classmethod
    def create_dialog_error_notification(self, msg: str) -> None:
        messagebox.showerror("Error", msg)

    # Set theme
    @classmethod
    def load_theme(self) -> None:
        try:
            themes_path = self.get_resource_path("settings/themes.json")
            with open(themes_path, "r") as file:
                themes = json.load(file)

            if Config.theme_cur_option in themes:
                Config.theme = themes[Config.theme_cur_option]
        except:
            self.create_dialog_error_notification(
                "A fatal error occured while changing the theme, was the theme.json file modified?"
            )
            raise ValueError(
                "A fatal error occured while changing the theme, was the theme.json file modified?"
            )
