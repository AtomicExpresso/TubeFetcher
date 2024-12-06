from tkinter.font import BOLD
import customtkinter as ctk
from classes.config import Config

#handles popups
class Window(ctk.CTkToplevel):
  def __init__(self, parent):
    super().__init__(parent)
    self.geometry("300x200")
    self.title("Settings")

class SettingsWindow(Window):
  def __init__(self, parent):
    super().__init__(parent)
    self.parent = parent
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

  


  
  
