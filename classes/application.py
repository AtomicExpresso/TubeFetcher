import customtkinter as ctk
from PIL import Image
from app.vidinfo import VidInfo
from classes.config import Config
from app.frames import AppFrames

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
    self.vid_frame = VidInfo(parent=self)

    self.frames.create_frames()
    self.create_images()
    self.create_widgets()
    self.grid_config()
    self.append_widgets()

  def get_vid_info(self)->dict:
    return self.vid_info

  def create_images(self):
    settingsImgSrc = Image.open("./images/settings.png")
    folderImgSrc = Image.open("./images/folder.png")
    trashImgSrc = Image.open("./images/trash.png")
    plusImgSrc = Image.open("./images/plus.png")

    self.settingsImg = ctk.CTkImage(light_image=settingsImgSrc, size=(20,20))
    self.folderImg = ctk.CTkImage(light_image=folderImgSrc, size=(20,20))
    self.trashImg = ctk.CTkImage(light_image=trashImgSrc, size=(20,20))
    self.plusImg = ctk.CTkImage(light_image=plusImgSrc, size=(20,20))

  def create_widgets(self):
    #input box
    self.input = ctk.CTkEntry(
      self.frames.top_frame, 
      border_width=0, 
      height=30, 
      corner_radius=0, 
      placeholder_text="Video URL")

    #Texts
    self.download_progress_txt = ctk.CTkLabel(
      self.frames.progress_frame, 
      text="25%", 
      fg_color="transparent", 
      font=("ariel", 20))
    self.error_txt = ctk.CTkLabel(
      self.frames.progress_frame, 
      text_color="red", 
      text="Error", 
      fg_color="transparent", 
      font=("ariel", 20))

    #buttons
    self.download_button = ctk.CTkButton(
      self.frames.bottom_frame, 
      text="Download", 
      fg_color=f"{Config.btn_color_download}", 
      hover_color="#2d6e2b", 
      command=self.download_btn_clbck)
    #App download option
    self.options = ctk.CTkOptionMenu(
      self.frames.bottom_frame, 
      fg_color=f"{Config.secondary_color}", 
      button_color=f"{Config.btn_color}", 
      button_hover_color=f"{Config.btn_color_hover}", 
      values=[*Config.dl_options], 
      command=self.set_dl_option_clbck)
    #Folder button for file path
    self.folder_btn = ctk.CTkButton(
      self.frames.bottom_frame, 
      fg_color=f"{Config.secondary_color}", 
      hover_color="#363535", 
      image=self.folderImg, 
      text="", 
      width=45, 
      command=self.folder_path_clbck)
    #Trash button
    self.trash_btn = ctk.CTkButton(
      self.frames.bottom_frame, 
      image=self.trashImg, 
      fg_color=f"{Config.secondary_color}", 
      hover_color="#363535", 
      text="", 
      width=45,
      command=self.clear_mf_clbck)
    #Add videos to que button
    self.addvideo_btn = ctk.CTkButton(
      self.frames.top_frame, 
      image=self.plusImg, 
      fg_color=f"{Config.secondary_color}", 
      hover_color="#363535", 
      text="", 
      bg_color="transparent", 
      corner_radius=0, 
      width=45, 
      command=self.add_video_clbck)
    #Settings button
    self.settings_btn = ctk.CTkButton(
      self.frames.top_frame, 
      image=self.settingsImg, 
      fg_color=f"{Config.secondary_color}", 
      hover_color=f"{Config.btn_color}", 
      text="", 
      width=45, 
      command=self.st_clbck)

    #progress bar
    self.download_progress_bar = ctk.CTkProgressBar(
      self.frames.progress_frame, 
      progress_color=f"{Config.progress_color}", 
      orientation="horizontal", 
      width=250)
  
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

  #Appends widgets to frames
  def append_widgets(self):
    #frames
    self.frames.top_frame.grid(row=0, column=0, columnspan=3, sticky="sew")
    self.frames.main_frame.grid(row=1, column=0, columnspan=3, sticky="nsew")
    self.frames.progress_frame.grid(row=2, column=0, columnspan=3, sticky="nsew")
    self.frames.bottom_frame.grid(row=3, column=0, columnspan=3, sticky="nsew")

    #input row
    self.input.grid(column=0, columnspan=3, row=0, pady=10, padx=(20, 90), sticky="ew")
    self.addvideo_btn.grid(column=1, row=0, pady=10, padx=(0, 0), sticky="e")
    self.settings_btn.grid(column=2, row=0, pady=10, padx=(20, 20), sticky="e")

    #bottom row
    self.folder_btn.grid(column=0, row=0, pady=10, padx=(20, 10), sticky="w")
    self.trash_btn.grid(column=2, row=0, pady=10, padx=(0, 10), sticky="e")
    self.download_button.grid(column=3,row=0, padx=(0, 20), pady=(10,10), sticky="e")
    self.options.grid(column=1,row=0, padx=10, pady=(10,10), sticky="w")