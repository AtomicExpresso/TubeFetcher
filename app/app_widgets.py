import customtkinter as ctk
from utils.config import Config
from PIL import Image

#Handles creating app widgets
class AppWidgets:
  def __init__(self, parent):
    self.parent = parent

  def create_images(self):
    settingsImgSrc = Image.open("./images/settings.png")
    folderImgSrc = Image.open("./images/folder.png")
    trashImgSrc = Image.open("./images/trash.png")
    plusImgSrc = Image.open("./images/plus.png")

    self.settingsImg = ctk.CTkImage(light_image=settingsImgSrc, size=(20,20))
    self.folderImg = ctk.CTkImage(light_image=folderImgSrc, size=(20,20))
    self.trashImg = ctk.CTkImage(light_image=trashImgSrc, size=(20,20))
    self.plusImg = ctk.CTkImage(light_image=plusImgSrc, size=(20,20))

  #create widgets for progress frame
  def create_progress_widgets(self):
    #labels
    self.download_progress_txt = ctk.CTkLabel(
      self.parent.frames.progress_frame, 
      text="25%", 
      fg_color="transparent", 
      font=("ariel", 20))
    self.error_txt = ctk.CTkLabel(
      self.parent.frames.progress_frame, 
      text_color="red", 
      text="Error", 
      fg_color="transparent", 
      font=("ariel", 20))
    #progress bar
    self.download_progress_bar = ctk.CTkProgressBar(
      self.parent.frames.progress_frame, 
      progress_color=f"{Config.progress_color}", 
      orientation="horizontal", 
      width=250)
    
  #create widgets for top frame
  def create_top_widgets(self):
    #input box
    self.input = ctk.CTkEntry(
      self.parent.frames.top_frame, 
      border_width=0, 
      height=30, 
      corner_radius=0, 
      placeholder_text="Video URL")
    #Add videos to que button
    self.addvideo_btn = ctk.CTkButton(
      self.parent.frames.top_frame, 
      image=self.plusImg, 
      fg_color=f"{Config.secondary_color}", 
      hover_color="#363535", 
      text="", 
      bg_color="transparent", 
      corner_radius=0, 
      width=45, 
      command=self.parent.add_video_clbck)
    #Settings button
    self.settings_btn = ctk.CTkButton(
      self.parent.frames.top_frame, 
      image=self.settingsImg, 
      fg_color=f"{Config.secondary_color}", 
      hover_color=f"{Config.btn_color}", 
      text="", 
      width=45, 
      command=self.parent.st_clbck)
  #create widgets for bottom frame
  def create_bottom_widgets(self):
    #buttons
    self.download_button = ctk.CTkButton(
      self.parent.frames.bottom_frame, 
      text="Download", 
      fg_color=f"{Config.btn_color_download}", 
      hover_color="#2d6e2b", 
      command=self.parent.download_btn_clbck)
    #App download option
    self.options = ctk.CTkOptionMenu(
      self.parent.frames.bottom_frame, 
      fg_color=f"{Config.secondary_color}", 
      button_color=f"{Config.btn_color}", 
      button_hover_color=f"{Config.btn_color_hover}", 
      values=[*Config.dl_options], 
      command=self.parent.set_dl_option_clbck)
    #Folder button for file path
    self.folder_btn = ctk.CTkButton(
      self.parent.frames.bottom_frame, 
      fg_color=f"{Config.secondary_color}", 
      hover_color="#363535", 
      image=self.folderImg, 
      text="", 
      width=45, 
      command=self.parent.folder_path_clbck)
    #Trash button
    self.trash_btn = ctk.CTkButton(
      self.parent.frames.bottom_frame, 
      image=self.trashImg, 
      fg_color=f"{Config.secondary_color}", 
      hover_color="#363535", 
      text="", 
      width=45,
      command=self.parent.clear_mf_clbck)
  
  #creates all widgets
  def create_widgets(self):
    #top frame widgets
    self.create_top_widgets()
    #Progress frame widgets
    self.create_progress_widgets()
    #Bottom frame widgets
    self.create_bottom_widgets()