import customtkinter
from utils.cmd import AppCmd

"""
Libraries Used:
- Third-Party Libraries:
  - CustomTkinter
  - Pillow
  - Pyperclip
  - Requests
  - Pytube

- Standard Python Modules:
  - os
  - json
"""

"""
todo:
-if possible, add hotreload to theme
"""

#Run application
def run():
  customtkinter.set_appearance_mode("System")
  customtkinter.set_default_color_theme("blue")

  program = AppCmd()

  program.run()

run()