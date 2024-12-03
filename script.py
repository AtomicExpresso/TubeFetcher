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
"""

#Run application
#https://www.youtube.com/shorts/IQDA39A44AA
def run():
  customtkinter.set_appearance_mode("System")
  customtkinter.set_default_color_theme("blue")

  program = AppCmd()

  program.run()

run()