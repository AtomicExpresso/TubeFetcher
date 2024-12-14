from tkinter.font import BOLD
import customtkinter as ctk
from utils.config import Config

#handles popups
class Window(ctk.CTkToplevel):
  def __init__(self, parent):
    super().__init__(parent)
    self.geometry(f"{Config.secondary_win_width}x{Config.secondary_win_height}")

class SettingsWindow(Window):
  def __init__(self, parent):
    super().__init__(parent)
    self.parent = parent
    self.title("Settings")
    self.create_widgets()
    self.config_grid()
    self.append_grid()
  
  def create_widgets(self):
    self.settings_frame = ctk.CTkFrame(
      self, 
      fg_color=f"{Config.primary_color}")

    self.defLbl = ctk.CTkLabel(
      self.settings_frame, 
      text="General", 
      font=('ariel', 20, BOLD))
    self.resLbl = ctk.CTkLabel(
      self.settings_frame, 
      text="Resolution:")
    self.dowLbl = ctk.CTkLabel(
      self.settings_frame, 
      text="Download Type:")
    #Download options menu, inherits from config
    self.opt = ctk.CTkOptionMenu(
      self.settings_frame, 
      fg_color=f"{Config.secondary_color}", 
      button_color=f"{Config.btn_color}", 
      button_hover_color=f"{Config.btn_color_hover}", 
      values=[*Config.dl_options],
      command=self.parent.set_dl_option_clbck)
    #Resoultion options menu, inherits from config
    self.res_opt = ctk.CTkOptionMenu(
      self.settings_frame, 
      fg_color=f"{Config.secondary_color}", 
      button_color=f"{Config.btn_color}", 
      button_hover_color=f"{Config.btn_color_hover}", 
      values=[*Config.res_options],
      command=self.parent.set_dl_option_clbck)
    #Closes menu
    self.closeBtn = ctk.CTkButton(
      self.settings_frame, 
      fg_color=f"{Config.btn_color}", 
      hover_color=f"{Config.btn_color_hover}", 
      text="Close", 
      command=self.destroy)

  def config_grid(self):
    self.grid_columnconfigure(0, weight=1)
    self.grid_rowconfigure(0, weight=1)

    self.settings_frame.grid_columnconfigure(0, weight=0)
    self.settings_frame.grid_rowconfigure(1, weight=0)
    self.settings_frame.grid_rowconfigure(2, weight=0)
    self.settings_frame.grid_rowconfigure(3, weight=0)
    self.settings_frame.grid_rowconfigure(4, weight=1)

  def append_grid(self):
    self.settings_frame.grid(row=0, columnspan=3, column=0, sticky="nsew")

    self.defLbl.grid(row=1, column=0, columnspan=3, padx=(10, 0), pady=(20, 0), sticky="w")

    self.resLbl.grid(row=2, column=0, padx=(10, 0), pady=(0, 0), sticky="w")
    self.res_opt.grid(row=2, column=1, padx=(10, 10), pady=(10, 10), sticky="w")

    self.dowLbl.grid(row=3, column=0, padx=(10, 0), pady=(0, 0), sticky="w")
    self.opt.grid(row=3, column=1, padx=(10, 10), pady=(10, 10), sticky="w")

    self.closeBtn.grid(row=4, column=0, columnspan=3, padx=(10, 10), pady=(10, 10), sticky="s")

class InfoWindow(Window):
  def __init__(self, parent, index:int):
    super().__init__(parent)
    self.parent = parent
    self.index = index
    self.title("Video Info")

    self.create_info_widgets()

  #fetchs video info from app vid queue
  def fetch_info(self)->None:
    self.info:dict = self.parent.vid_queue[self.index]
  
  def create_info_frames(self)->None:
    #Main info frame
    self.info_window_frame = ctk.CTkScrollableFrame(
      self, 
      fg_color=f"{Config.primary_color}")
    #Attribute frame
    self.info_attr_frame = ctk.CTkFrame(
      self.info_window_frame, 
      fg_color=f"{Config.primary_color}")
    #Description frame
    self.info_desc_frame = ctk.CTkFrame(
      self.info_window_frame, 
      fg_color=f"{Config.primary_color}")
    
  def create_info_labels(self)->None:
    #video title
    self.titleLbl = ctk.CTkLabel(
      self.info_attr_frame, 
      text=f"Title:",
      font=('ariel', 14, BOLD))
    self.titleContentLbl = ctk.CTkLabel(
      self.info_attr_frame, 
      text=f"{self.info["title"]}")
    #Video author
    self.authorLbl = ctk.CTkLabel(
        self.info_attr_frame, 
        text=f"Author:",
        font=('ariel', 14, BOLD))
    self.authorContentLbl = ctk.CTkLabel(
        self.info_attr_frame, 
        text=f"{self.info["author"]}")
    #Video duriation
    self.duriationLbl = ctk.CTkLabel(
        self.info_attr_frame, 
        text=f"Duriation:",
        font=('ariel', 14, BOLD))
    self.duriationContentLbl = ctk.CTkLabel(
        self.info_attr_frame, 
        text=f"{self.info["duriation"]}")
    #Video file size
    self.sizeLbl = ctk.CTkLabel(
        self.info_attr_frame, 
        text=f"Size:",
        font=('ariel', 14, BOLD))
    self.sizeContentLbl = ctk.CTkLabel(
        self.info_attr_frame, 
        text=f"{self.info["size"]}")
    #Video Description
    self.descLbl = ctk.CTkLabel(
        self.info_desc_frame, 
        text=f"Description:",
        font=('ariel', 14, BOLD))
    #Description content
    self.descContentLbl = ctk.CTkLabel(
      self.info_desc_frame, 
      text=f"{self.info["desc"]}",
      wraplength=Config.max_paragraph_len,
      justify="left")
      
  def create_info_btns(self)->None:
    #Closes menu
    self.closeBtn = ctk.CTkButton(
      self.info_window_frame, 
      fg_color=f"{Config.btn_color}", 
      hover_color=f"{Config.btn_color_hover}", 
      text="Close", 
      command=self.destroy)
  
  def config_info_grid(self)->None:
    self.grid_columnconfigure(0, weight=1)
    self.grid_rowconfigure(0, weight=1)

    self.info_window_frame.grid_rowconfigure(0, weight=1)
    self.info_window_frame.grid_rowconfigure(1, weight=1)
    self.info_window_frame.grid_rowconfigure(2, weight=1)
    self.info_window_frame.grid_rowconfigure(3, weight=0)

    self.info_attr_frame.grid_columnconfigure(0, weight=0)
    self.info_attr_frame.grid_columnconfigure(1, weight=1)

  def append_info_grid(self)->None:
    self.info_window_frame.grid(row=0, column=0, sticky="nsew")
    self.info_attr_frame.grid(row=1, column=0, sticky="nsew")
    self.info_desc_frame.grid(row=2, column=0, sticky="nsew")

    self.titleLbl.grid(row=0, column=0, padx=(10, 0), pady=(20, 0), sticky="w")
    self.titleContentLbl.grid(row=0, column=1, pady=(20, 0), sticky="w")
    
    self.authorLbl.grid(row=1, column=0, padx=(10, 0), pady=(0, 0), sticky="w")
    self.authorContentLbl.grid(row=1, column=1, pady=(0, 0), sticky="w")

    self.duriationLbl.grid(row=2, column=0, padx=(10, 0), pady=(0, 0), sticky="w")
    self.duriationContentLbl.grid(row=2, column=1, pady=(0, 0), sticky="w")

    self.sizeLbl.grid(row=3, column=0, padx=(10, 0), pady=(0, 0), sticky="w")
    self.sizeContentLbl.grid(row=3, column=1, pady=(0, 0), sticky="w")

    self.descLbl.grid(row=0, column=0, padx=(10, 0), pady=(0, 0), sticky="w")
    self.descContentLbl.grid(row=1, column=0, padx=(10, 0), pady=(0, 0), sticky="w")

    self.closeBtn.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="s")

  def create_info_widgets(self)->None:
    self.fetch_info()
    self.create_info_frames()
    self.create_info_labels()
    self.create_info_btns()
    self.config_info_grid()
    self.append_info_grid()

  


  
  
