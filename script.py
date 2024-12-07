import customtkinter
from classes.cmd import AppCmd

"""
todo:
-Add ability to download audio only
-Add save system
-Add info button for videos
-Finish video thumbnail, title, size and percentage downloaded to main content
-Add que system to downloads
-Add delete button to clear main frame
-Add video size to vid frame
-Add total time to duriation (its counted in seconds)
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