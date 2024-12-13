import customtkinter as ctk
from utils.utils import Utils
from utils.config import Config
from io import BytesIO
from requests import get
from tkinter.font import BOLD
from PIL import Image
  
#Handles video info frame
class VidInfo:
  def __init__(self, parent):
    self.parent = parent
    self.info = None

  #Configure the grid
  def config_vid_grid(self)->None:
    #Cols
    self.vid_frame.grid_columnconfigure(0, weight=0)
    self.vid_frame.grid_columnconfigure(1, weight=0)
    #Rows
    self.vid_ct_frame.grid_rowconfigure(0, weight=0)
    self.vid_ct_frame.grid_rowconfigure(1, weight=0)
    self.vid_ct_frame.grid_rowconfigure(2, weight=0)

  def append_vid_widget(self)->None:
    #Append widgets to grid
    self.vid_tn_frame.grid(column=0, row=0, padx=10, pady=10, sticky="n")
    self.vid_ct_frame.grid(column=1, row=0, padx=10, pady=10, sticky="n")
    self.vid_frame.grid(row=[len(self.parent.vid_queue)+1], column=0, columnspan=3, padx=20, pady=5, sticky="nsew")
    self.vid_thumbnail_lbl.grid(column=0, row=1, pady=0, padx=(20, 10), sticky="w")
    self.vid_title_lbl.grid(column=0, row=0, columnspan=2, pady=(10, 10), padx=(20, 10), sticky="w")

    self.vid_dl_option.grid(column=0, row=1, padx=(10, 0), sticky="w")
    self.vid_res_option.grid(column=1, row=1, padx=(10, 10), sticky="w")

    self.vid_duriation_lbl.grid(column=0, row=2, pady=(10, 10), padx=(10, 0), sticky="w")
    self.vid_size_lbl.grid(column=1, row=2, pady=(10,10), padx=(10, 10), sticky="w")

  #Create video widgets
  def create_vid_widgets(self)->None:
    #--main vid frame
    self.vid_frame = ctk.CTkFrame(
      self.parent.frames.main_frame,
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
      text=f"{self.info["index"]}")
    index = int(self.vid_index.cget("text"))

    #create labels
    self.vid_title_lbl = ctk.CTkLabel(
      self.vid_ct_frame, 
      text=f"{self.info["title"]}", 
      font=('ariel', 13, BOLD))
    self.vid_thumbnail_lbl = ctk.CTkLabel(
      self.vid_tn_frame, 
      text="", 
      image=self.vid_thumbnail)
    self.vid_duriation_lbl = ctk.CTkLabel(
      self.vid_ct_frame, 
      text=f"Duriation: {Utils.calculate_Time(self.info["duriation"])}")
    self.vid_size_lbl = ctk.CTkLabel(
      self.vid_ct_frame, 
      text=f"Size: {self.info["size"]}")
    #Create options
    self.vid_dl_option = ctk.CTkOptionMenu(
      self.vid_ct_frame, 
      fg_color=f"{Config.secondary_color}", 
      button_color=f"{Config.btn_color}", 
      button_hover_color=f"{Config.btn_color_hover}", 
      values=[*Config.dl_options], 
      command=lambda cur_val: self.parent.set_dl_single_clbck(txt=cur_val, i=index))
    self.vid_res_option = ctk.CTkOptionMenu(
      self.vid_ct_frame, 
      fg_color=f"{Config.secondary_color}", 
      button_color=f"{Config.btn_color}", 
      button_hover_color=f"{Config.btn_color_hover}", 
      values=[*Config.res_options], 
      command=lambda cur_val:self.parent.set_dl_single_clbck(txt=cur_val, i=index))
    #Set vid values to the ones selected
    self.vid_dl_option.set(Config.dl_cur_option)
    self.vid_res_option.set(Config.res_cur_option)

  #fetch video image
  def fetch_vid_thumbnail(self):
    # Download the image using requests
    image_url = self.info["thumbnail"]
    response = get(image_url)
    img_data = response.content

    vid_thumbnail_img = Image.open(BytesIO(img_data))
    self.vid_thumbnail = ctk.CTkImage(light_image=vid_thumbnail_img, size=(150,120))

  def update_vid_info(self, new_info: dict):
    #change specified fields
    for key, value in new_info.items():
      if key in self.info:
        self.info[key] = value
    
    # Update the widgets
    if self.vid_title_lbl:
      self.vid_title_lbl.configure(text=f"{self.info['title']}")
        
    if self.vid_size_lbl:
      self.vid_size_lbl.configure(text=f"Size: {self.info['size']}")

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

  #Adds video info to frame
  def append_vid_info(self):
    self.info = self.parent.get_vid_info()
    self.fetch_vid_thumbnail()
    self.create_vid_widgets()
    self.config_vid_grid()
    self.append_vid_widget()