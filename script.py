import customtkinter
from utils.cmd import AppCmd
from utils.utils import Utils

"""
todo:
-Add info button for videos
-Add individual progress bars to each video frame when downloading
"""
"""
    def dl_in_progress(self):
      #destroy options to make room for progress bar
      self.vid_res_option.destroy()
      self.vid_dl_option.destroy()

      #create progress bar
      self.vid_dl_progress = ctk.CTkProgressBar(
        self.vid_ct_frame, 
        progress_color=f"{Config.progress_color}", 
        orientation="horizontal", 
        width=250
      )
      self.vid_dl_progress_txt = ctk.CTkLabel(
        self.vid_ct_frame, 
        text="25%", 
        fg_color="transparent", 
        font=("ariel", 20))
    self.vid_dl_progress_txt.grid(column=0, row=0, pady=50, padx=(10, 10), sticky="w")
    self.vid_dl_progress.grid(column=0, row=1, padx=(10, 0), columnspan=3, sticky="w")

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