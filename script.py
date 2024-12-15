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

"""
todo:
-Fix btn bug with vid info frame
-Add delete btn to vid info frame, so users can delete vids from queue
"""
#Run application
#these are just test videos to make sure the app works, test cases will be deleted upon release
#https://www.youtube.com/shorts/IQDA39A44AA
#https://www.youtube.com/watch?v=PCH-l94KnXU
#https://www.youtube.com/watch?v=iJpxJuv0mqY
#https://www.youtube.com/watch?v=sWbUDq4S6Y8&t=459s
def run():
  customtkinter.set_appearance_mode("System")
  customtkinter.set_default_color_theme("blue")

  program = AppCmd()

  program.run()

run()