import customtkinter
from utils.cmd import AppCmd

"""
Libaries used:
-Customtkinter
-Pillow
-Pyperclip
-Requests
-Json
-Pytube
"""

#Run application
def run():
  customtkinter.set_appearance_mode("System")
  customtkinter.set_default_color_theme("blue")

  program = AppCmd()

  program.run()

run()