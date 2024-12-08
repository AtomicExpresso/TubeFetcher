import customtkinter
from utils.cmd import AppCmd
from utils.utils import Utils

"""
todo:
-Add info button for videos
-Add individual progress bars to each video frame when downloading
"""

#Run application
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