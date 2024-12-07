from tkinter import messagebox
import customtkinter as ctk
from pytubefix import YouTube, Playlist
from utils.application import Application
from utils.Window import SettingsWindow
from utils.config import Config
from utils.utils import Utils

class AppCmd:
  def __init__(self):
    self.app = Application(
      download_btn_clbck=self.download_btn, 
      folder_path_clbck=self.select_folder, 
      add_vid_clbck=self.add_video,
      st_clbck=self.open_settings_window,
      set_dl_clbck=self.set_download_option,
      set_dl_single_clbck=self.set_single_download_option,
      clear_mf_clbck=self.clear_main_frame)
    
    self.settings_window = None

  #For adding videos to main frame
  def add_video(self)->None:
    try:
      self.app.url = self.app.widgets.input.get()
      self.app.yt = YouTube(
        self.app.url, 
        on_progress_callback=self.set_progress, 
        on_complete_callback=self.set_complete)
      
      #Fetch video info
      thumbnail:str = self.app.yt.thumbnail_url
      title:str = self.app.yt.title
      desc:str = self.app.yt.description
      duriation:str|int = self.app.yt.length
      author:str = self.app.yt.author
      res_opt:str = Config.res_cur_option
      dl_opt:str = Config.dl_cur_option
      size:str|int = "Pending" #file size
      stream = None #download stream
      index:int = len(self.app.vid_queue)

      self.app.vid_info = {
        "thumbnail": thumbnail, 
        "title":title, 
        "desc":desc, 
        "duriation": duriation, 
        "author":author, 
        "url": self.app.url,
        "res_opt": res_opt,
        "dl_opt": dl_opt,
        "size": size,
        "stream": stream,
        "index": index}
      self.app.vid_queue.append(self.app.vid_info) #Add video to queue

      self.check_vid_resoultion(index)
      self.app.vid_frame.append_vid_info()
      
      #reset progress bar
      if self.app.frames.progress_frame.winfo_exists():
        self.destroy_progress_frame()
    except:
      self.throw_progress_error(msg="Invalid URL")
      raise ValueError("Invalid url")

  #For specifying download path
  def select_folder(self)->None:
    #open folder dialog
    try:
      folder_selected = ctk.filedialog.askdirectory(title="Select a Folder")

      if folder_selected:
        Config.folder_path = folder_selected
        messagebox.showinfo("File path updated", f"Download folder is now, {folder_selected}")
    except:
      self.app.widgets.error_txt.configure(text="Incorrect file path")
      self.app.widgets.error_txt.grid(row=0, column=0, columnspan=2, pady=(120, 0), padx=(0, 0))
      raise ValueError("Unable to change file path, did you give the app permissions?")

  #open the settings window
  def open_settings_window(self)->None:
    self.settings_window = SettingsWindow(self.app)
    self.settings_window.grab_set()
    self.set_settings_values()

  #Set progress bar progress
  def set_progress(self, stream, chunk, bytes_remaining)->None:
    total_size:str|int = stream.filesize
    bytes_downloaded:str|int = total_size - bytes_remaining
    percentage_left:str|int = bytes_downloaded / total_size * 100
    progess_per:int = int(percentage_left)

    #update progress text
    self.app.widgets.download_progress_txt.configure(text=f"{progess_per}%")
    self.app.widgets.download_progress_txt.update()

    #update progress bar
    self.app.widgets.download_progress_bar.set(float(percentage_left)/100)
    self.app.widgets.download_progress_bar.update()

  #Runs after video has been completed
  def set_complete(self,stream, chunk)->None:
    #update progress text
    self.app.widgets.download_progress_txt.configure(text=f"Complete!",text_color="green")

  #Clears videos from main frame
  def clear_main_frame(self)->None:
    try:
      self.app.vid_info = {}
      self.app.vid_queue = []

      self.app.frames.create_main_frame()
      self.app.append_widgets()
      self.app.grid_config()
    except:
      raise ValueError("An error occured while clearing widgets")

  #reset feilds
  def reset_feilds(self)->None:
    self.app.widgets.download_progress_txt.configure(text="", text_color="white")
    self.app.widgets.error_txt.configure(text="")
    self.app.widgets.download_progress_bar.set(0)

  #set download option
  def set_download_option(self, txt)->None:
    if txt in Config.dl_options:
      Config.dl_cur_option = txt
      self.set_settings_values()
    elif txt in Config.res_options:
      Config.res_cur_option = txt
      self.set_settings_values()
  
  #Check resoultion
  def check_vid_resoultion(self, i)->None:
    try:
      #Check if users perfered resoultion is possible, if not fall back to the highest resolution
      cur = self.app.vid_queue[i]
      cur_stream = YouTube(
        cur["url"], 
        on_progress_callback=self.set_progress, 
        on_complete_callback=self.set_complete).streams
      cur_filter = cur_stream.filter(
        res=f"{Config.res_cur_option}").get_highest_resolution()

      if cur_filter:
        cur["stream"] = cur_filter
      else:
        cur["stream"] = cur_stream.get_highest_resolution()

      cur["size"] = Utils.calculate_file_size(cur)
    except:
      raise ValueError("An error occured while fetching video stream, is your internet connected?")

  #Set single video download option
  def set_single_download_option(self, txt, i)->None:
    cur = self.app.vid_queue[i]
    if txt in Config.dl_options:
      cur["dl_opt"] = txt
      cur["size"] = Utils.calculate_file_size(cur)
    elif txt in Config.res_options:
      cur["res_opt"] = txt
    self.check_vid_resoultion(i)

  #Sets app widgets to the values in config
  def set_settings_values(self)->None:
    self.app.widgets.options.set(Config.dl_cur_option)

    #Apply config values to settings if setting window exists
    if self.settings_window and self.settings_window.winfo_exists():
      self.settings_window.opt.set(Config.dl_cur_option)
      self.settings_window.res_opt.set(Config.res_cur_option)

  #used for deleting progress frame
  def destroy_progress_frame(self)->None:
    if self.app.frames.progress_frame.winfo_exists():
      self.app.frames.progress_frame.destroy()
  #used for recreating progress frame
  def check_progress_frame(self)->None:
    if not self.app.frames.progress_frame.winfo_exists():
      self.app.frames.create_progress_frame()
      self.app.widgets.create_progress_widgets()
      self.app.append_progress_widgets()
      self.app.frames.grid_config()
  #throw error
  def throw_progress_error(self, msg:str)->None:
    self.destroy_progress_frame() #preventing duplicates
    self.check_progress_frame()

    self.app.widgets.error_txt.configure(text=f"{msg}")
    self.app.widgets.error_txt.grid(row=0, column=0, columnspan=2, pady=(10, 0), padx=(0, 0))

  #Runs on download button click
  def download_btn(self)->None:
    #Check if progress frame is missing
    self.check_progress_frame()
    self.reset_feilds()
    
    try:
      #loop over video queue
      for video in self.app.vid_queue:
        cur_vid_yt = YouTube(
          video["url"], 
          on_progress_callback=self.set_progress, 
          on_complete_callback=self.set_complete)
        cur_stream = cur_vid_yt.streams
        cur_filter = None
        
        #apply filters
        if video["dl_opt"] == "Video + Audio":
          cur_filter = cur_stream.filter(
            res=f"{video["res_opt"]}").get_highest_resolution()
        elif video["dl_opt"] == "Audio":
          cur_filter = cur_stream.get_audio_only()
        
        #check if desired resoultion is possible, if not find the best possible resoultion
        if cur_filter:
          cur_filter.download(f"{Config.folder_path}")
        else:
          cur_stream.get_highest_resolution().download(f"{Config.folder_path}")

      #Append progress content to frame
      self.app.frames.progress_frame.grid(row=2, column=0, columnspan=3, sticky="nsew")
      self.app.widgets.download_progress_txt.grid(row=0, column=0, pady=(10, 0), padx=(20, 0))
      self.app.widgets.download_progress_bar.grid(row=1, column=0, columnspan=2, padx=(20, 20), pady=(0, 10), sticky="ew")
      self.app.widgets.error_txt.configure(text="")
    except:
      self.throw_progress_error(msg="Invalid URL")

  def run(self)->None:
    self.app.mainloop()