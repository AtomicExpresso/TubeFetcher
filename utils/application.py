import customtkinter as ctk
from app.vidinfo import VidInfo
from app.frames import AppFrames
from app.app_widgets import AppWidgets

class Application(ctk.CTk):
  def __init__(self, download_btn_clbck, folder_path_clbck, add_vid_clbck, st_clbck, set_dl_clbck, set_dl_single_clbck, clear_mf_clbck):
    super().__init__()
    self.width = 500
    self.height = 350
    self.geometry(f"{self.width}x{self.height}")
    self.title("TubeFetcher")

    #setup callback functions
    self.download_btn_clbck = download_btn_clbck #Downloads all videos in mainframe
    self.folder_path_clbck = folder_path_clbck #Opens folder dialog
    self.add_video_clbck = add_vid_clbck #Adds new videos to mainframe
    self.st_clbck = st_clbck #open settings window
    self.set_dl_option_clbck = set_dl_clbck #sets default resoultion and download type for all new videos
    self.set_dl_single_clbck = set_dl_single_clbck #Sets resoultion and download type for a single video
    self.clear_mf_clbck = clear_mf_clbck #Clear main frame

    self.url = ""
    self.yt = None
    self.vid_info = None #is a dict of video info
    self.vid_queue = [] #list for video queue

    self.frames = AppFrames(parent=self)
    self.widgets = AppWidgets(parent=self)
    self.vid_frame = VidInfo(parent=self)

    self.frames.create_frames()
    self.widgets.create_images()
    self.widgets.create_widgets()

    self.grid_config()
    self.append_widgets()

  #fetchs vid info attribute for vidInfo class
  def get_vid_info(self)->dict:
    return self.vid_info
  
  #Configures grid positions
  def grid_config(self):
    #configure grid
    self.grid_columnconfigure(0, weight=0)
    self.grid_columnconfigure(1, weight=1)
    self.grid_columnconfigure(2, weight=0)
    
    self.grid_rowconfigure(0, weight=0)
    self.grid_rowconfigure(1, weight=1)
    self.grid_rowconfigure(2, weight=0)
    self.grid_rowconfigure(3, weight=0)

    #confiigure frame grid
    self.frames.grid_config()

  #append progress frame
  def append_progress_widgets(self):
    self.frames.progress_frame.grid(row=2, column=0, columnspan=3, sticky="nsew")

  #Appends widgets to frames
  def append_widgets(self):
    #frames
    self.frames.top_frame.grid(row=0, column=0, columnspan=3, sticky="sew")
    self.frames.main_frame.grid(row=1, column=0, columnspan=3, sticky="nsew")
    self.append_progress_widgets()
    self.frames.bottom_frame.grid(row=3, column=0, columnspan=3, sticky="nsew")

    #input row
    self.widgets.input.grid(column=0, columnspan=3, row=0, pady=10, padx=(20, 90), sticky="ew")
    self.widgets.addvideo_btn.grid(column=1, row=0, pady=10, padx=(0, 0), sticky="e")
    self.widgets.settings_btn.grid(column=2, row=0, pady=10, padx=(20, 20), sticky="e")

    #bottom row
    self.widgets.folder_btn.grid(column=0, row=0, pady=10, padx=(20, 10), sticky="w")
    self.widgets.trash_btn.grid(column=2, row=0, pady=10, padx=(0, 10), sticky="e")
    self.widgets.download_button.grid(column=3,row=0, padx=(0, 20), pady=(10,10), sticky="e")
    self.widgets.options.grid(column=1,row=0, padx=10, pady=(10,10), sticky="w")