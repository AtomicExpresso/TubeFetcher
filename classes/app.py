from tkinter.font import BOLD
import customtkinter as ctk
from PIL import Image
from io import BytesIO
from requests import get
from classes.config import Config
from classes.utils import Utils

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

    self.create_frames()
    self.create_images()
    self.create_widgets()
    self.grid_config()
    self.append_widgets()

  #re-creates mainframe
  def create_main_frame(self):
    self.main_frame = ctk.CTkScrollableFrame(
      self, 
      corner_radius=0, 
      fg_color="#363636",
      scrollbar_button_color=f"{Config.primary_color}",
      scrollbar_button_hover_color=f"{Config.secondary_color}")

  def create_frames(self):
    #Frame for url input
    self.top_frame = ctk.CTkFrame(
      self, 
      fg_color=f"{Config.primary_color}", 
      corner_radius=0)
    #Frame for main content
    self.create_main_frame()
    #Frame for progress bar
    self.progress_frame = ctk.CTkFrame(
      self,
      bg_color=f"{Config.primary_color}",
      fg_color="transparent",
      height=30, 
      corner_radius=0)
    #Frame for bottom row
    self.bottom_frame = ctk.CTkFrame(
      self, 
      fg_color=f"{Config.primary_color}",
      corner_radius=0)

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
      self.top_frame, 
      border_width=0, 
      height=30, 
      corner_radius=0, 
      placeholder_text="Video URL")

    #Texts
    self.download_progress_txt = ctk.CTkLabel(
      self.progress_frame, 
      text="25%", 
      fg_color="transparent", 
      font=("ariel", 20))
    self.error_txt = ctk.CTkLabel(
      self.progress_frame, 
      text_color="red", 
      text="Error", 
      fg_color="transparent", 
      font=("ariel", 20))

    #buttons
    self.download_button = ctk.CTkButton(
      self.bottom_frame, 
      text="Download", 
      fg_color=f"{Config.btn_color_download}", 
      hover_color="#2d6e2b", 
      command=self.download_btn_clbck)
    #App download option
    self.options = ctk.CTkOptionMenu(
      self.bottom_frame, 
      fg_color=f"{Config.secondary_color}", 
      button_color=f"{Config.btn_color}", 
      button_hover_color=f"{Config.btn_color_hover}", 
      values=[*Config.dl_options], 
      command=self.set_dl_option_clbck)
    #Folder button for file path
    self.folder_btn = ctk.CTkButton(
      self.bottom_frame, 
      fg_color=f"{Config.secondary_color}", 
      hover_color="#363535", 
      image=self.folderImg, 
      text="", 
      width=45, 
      command=self.folder_path_clbck)
    #Trash button
    self.trash_btn = ctk.CTkButton(
      self.bottom_frame, 
      image=self.trashImg, 
      fg_color=f"{Config.secondary_color}", 
      hover_color="#363535", 
      text="", 
      width=45,
      command=self.clear_mf_clbck)
    #Add videos to que button
    self.addvideo_btn = ctk.CTkButton(
      self.top_frame, 
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
      self.top_frame, 
      image=self.settingsImg, 
      fg_color=f"{Config.secondary_color}", 
      hover_color=f"{Config.btn_color}", 
      text="", 
      width=45, 
      command=self.st_clbck)

    #progress bar
    self.download_progress_bar = ctk.CTkProgressBar(
      self.progress_frame, 
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
    self.top_frame.grid_columnconfigure(0, weight=1)
    self.top_frame.grid_columnconfigure(1, weight=0)
    self.top_frame.grid_columnconfigure(2, weight=0)

    self.main_frame.grid_columnconfigure(0, weight=0)
    self.main_frame.grid_columnconfigure(1, weight=1)
    self.main_frame.grid_columnconfigure(2, weight=1)

    self.progress_frame.grid_rowconfigure(0, weight=0)
    self.progress_frame.grid_rowconfigure(1, weight=0)

    self.progress_frame.grid_columnconfigure(0, weight=0)
    self.progress_frame.grid_columnconfigure(1, weight=1)

    self.bottom_frame.grid_columnconfigure(0, weight=0)
    self.bottom_frame.grid_columnconfigure(1, weight=1)
    self.bottom_frame.grid_columnconfigure(2, weight=1)

  #Adds video info to frame
  def append_vid_info(self):
    #fetch image
    # Download the image using requests
    image_url = self.vid_info["thumbnail"]
    response = get(image_url)
    img_data = response.content

    vid_thumbnail_img = Image.open(BytesIO(img_data))
    self.vid_thumbnail = ctk.CTkImage(light_image=vid_thumbnail_img, size=(150,120))

    #Create video widgets
    #--main vid frame
    self.vid_frame = ctk.CTkFrame(
      self.main_frame,
      fg_color=f"{Config.primary_color}")
    #--thumbnail frame
    self.vid_tn_frame = ctk.CTkFrame(
      self.vid_frame, 
      fg_color=f"{Config.primary_color}")
    #--content frame
    self.vid_ct_frame = ctk.CTkFrame(
      self.vid_frame, 
      fg_color=f"{Config.primary_color}")
    #Special case
    #--Index, used for changeing a single video res and dl type
    self.vid_index = ctk.CTkLabel(
      self.vid_ct_frame, 
      text=f"{self.vid_info["index"]}")
    index = int(self.vid_index.cget("text"))

    #create labels
    self.vid_title_lbl = ctk.CTkLabel(
      self.vid_ct_frame, 
      text=f"{self.vid_info["title"]}", 
      font=('ariel', 13, BOLD))
    self.vid_thumbnail_lbl = ctk.CTkLabel(
      self.vid_tn_frame, 
      text="", 
      image=self.vid_thumbnail)
    self.vid_duriation_lbl = ctk.CTkLabel(
      self.vid_ct_frame, 
      text=f"Duriation: {Utils.calculate_Time(self.vid_info["duriation"])}")
    self.vid_size_lbl = ctk.CTkLabel(
      self.vid_ct_frame, 
      text=f"Size: {self.vid_info["size"]}")
    #Create options
    self.vid_dl_option = ctk.CTkOptionMenu(
      self.vid_ct_frame, 
      fg_color=f"{Config.secondary_color}", 
      button_color=f"{Config.btn_color}", 
      button_hover_color=f"{Config.btn_color_hover}", 
      values=[*Config.dl_options], 
      command=lambda cur_val: self.set_dl_single_clbck(txt=cur_val, i=index))
    self.vid_res_option = ctk.CTkOptionMenu(
      self.vid_ct_frame, 
      fg_color=f"{Config.secondary_color}", 
      button_color=f"{Config.btn_color}", 
      button_hover_color=f"{Config.btn_color_hover}", 
      values=[*Config.res_options], 
      command=lambda cur_val:self.set_dl_single_clbck(txt=cur_val, i=index))    
    #Set vid values to the ones selected
    self.vid_dl_option.set(Config.dl_cur_option)
    self.vid_res_option.set(Config.res_cur_option)
    #Configure the grid
    def config_vid_grid():
      #Cols
      self.vid_frame.grid_columnconfigure(0, weight=0)
      self.vid_frame.grid_columnconfigure(1, weight=0)
      #Rows
      self.vid_ct_frame.grid_rowconfigure(0, weight=0)
      self.vid_ct_frame.grid_rowconfigure(1, weight=0)
      self.vid_ct_frame.grid_rowconfigure(2, weight=0)

    #Append widgets to grid
    def append_vid_widget():
      self.vid_tn_frame.grid(column=0, row=0, padx=10, pady=10, sticky="n")
      self.vid_ct_frame.grid(column=1, row=0, padx=10, pady=10, sticky="n")
      self.vid_frame.grid(row=[len(self.vid_queue)+1], column=0, columnspan=3, padx=20, pady=5, sticky="nsew")
      self.vid_thumbnail_lbl.grid(column=0, row=1, pady=0, padx=(20, 10), sticky="w")
      self.vid_title_lbl.grid(column=0, row=0, columnspan=2, pady=(10, 10), padx=(20, 10), sticky="w")

      self.vid_dl_option.grid(column=0, row=1, padx=(10, 0), sticky="w")
      self.vid_res_option.grid(column=1, row=1, padx=(10, 10), sticky="w")

      self.vid_duriation_lbl.grid(column=0, row=2, pady=(10, 10), padx=(10, 0), sticky="w")
      self.vid_size_lbl.grid(column=1, row=2, pady=(10,10), padx=(10, 10), sticky="w")

    config_vid_grid()
    append_vid_widget()

  #Appends widgets to frames
  def append_widgets(self):
    #frames
    self.top_frame.grid(row=0, column=0, columnspan=3, sticky="sew")
    self.main_frame.grid(row=1, column=0, columnspan=3, sticky="nsew")
    self.progress_frame.grid(row=2, column=0, columnspan=3, sticky="nsew")
    self.bottom_frame.grid(row=3, column=0, columnspan=3, sticky="nsew")

    #input row
    self.input.grid(column=0, columnspan=3, row=0, pady=10, padx=(20, 90), sticky="ew")
    self.addvideo_btn.grid(column=1, row=0, pady=10, padx=(0, 0), sticky="e")
    self.settings_btn.grid(column=2, row=0, pady=10, padx=(20, 20), sticky="e")

    #bottom row
    self.folder_btn.grid(column=0, row=0, pady=10, padx=(20, 10), sticky="w")
    self.trash_btn.grid(column=2, row=0, pady=10, padx=(0, 10), sticky="e")
    self.download_button.grid(column=3,row=0, padx=(0, 20), pady=(10,10), sticky="e")
    self.options.grid(column=1,row=0, padx=10, pady=(10,10), sticky="w")