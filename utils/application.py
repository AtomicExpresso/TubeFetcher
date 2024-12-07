import customtkinter as ctk
from app.vidinfo import VidInfo
from app.frames import AppFrames
from app.app_widgets import AppWidgets
from app.app_append import AppAppend

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

    self.url = "" #url from input
    self.yt = None #pytube libary instance
    self.vid_info = None #is a dict of video info
    self.vid_queue = [] #list for video queue

    self.is_downloading:bool = False #used for preventing the user for changing res or dl options while a download is in progress

    self.frames = AppFrames(parent=self)
    self.widgets = AppWidgets(parent=self)
    self.vid_frame = VidInfo(parent=self)
    self.app_append = AppAppend(parent=self)

    self.frames.create_frames()
    self.widgets.create_images()
    self.widgets.create_widgets()

    self.app_append.grid_config()
    self.app_append.append_widgets()

  #fetchs vid info attribute for vidInfo class
  def get_vid_info(self)->dict:
    return self.vid_info