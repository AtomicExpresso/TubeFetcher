from tkinter import messagebox
from pyperclip import copy
import customtkinter as ctk
from pytubefix import YouTube
from utils.application import Application
from utils.Window import SettingsWindow, InfoWindow
from utils.config import Config
from utils.utils import Utils
from app.vidinfo import VidInfo

#class for handeling app commands, handles callback functions, and downloading videos
class AppCmd:
  def __init__(self):
    self.app = Application(
      download_btn_clbck=self.download_btn, 
      folder_path_clbck=self.select_folder, 
      add_vid_clbck=self.add_video,
      st_clbck=self.open_settings_window,
      info_clbck=self.open_info_window,
      set_dl_clbck=self.set_download_option,
      set_dl_single_clbck=self.set_single_download_option,
      clear_mf_clbck=self.clear_main_frame,
      copy_video_url_clbck=self.copy_video_url,
      dialog_notfi_clbck=self.create_dialog_notfication,
      update_new_queue_clbck=self.update_new_queue)
    #Default window state
    self.settings_window = None
    self.info_window = None

  #For adding videos to main frame
  def add_video(self)->None:
    if self.app.is_downloading:
      self.create_dialog_notfication("Cant add new videos because a download is in progress")
      pass
    else:
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
        index:int = self.app.frames.main_frame.grid_size()[1]

        self.app.vid_info = {
          "thumbnail": thumbnail, 
          "title":title, 
          "desc":desc, 
          "duriation": Utils.calculate_Time(duriation), 
          "author":author, 
          "url": self.app.url,
          "res_opt": res_opt,
          "dl_opt": dl_opt,
          "size": size,
          "stream": stream,
          "index": index}
        self.app.vid_queue.append(self.app.vid_info) #Add video to queue

        self.check_vid_resoultion(index)
        
        # Create a new VidInfo instance for the current video
        new_vid_info = VidInfo(parent=self.app)
        new_vid_info.append_vid_info()
        #append it to app parent
        self.app.vid_frames.append(new_vid_info)

        #reset progress bar
        self.destroy_progress_frame()
      except:
        self.throw_progress_error(msg="Invalid URL")
        self.create_dialog_notfication("Invalid video URL")
        raise ValueError("Invalid url")

  #For copying video url to clipboard, uses pyperclip libary
  def copy_video_url(self, i:int)->None:
    url:str = self.app.vid_queue[i]["url"]
    copy(url)
    self.create_dialog_notfication(f"Url copied to clipboard:\n{url}")
     
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
  
  #open the info window
  def open_info_window(self, i:int)->None:
    self.info_window = InfoWindow(self.app, i)
    self.info_window.grab_set()

  #Set progress bar progress
  def set_progress(self)->None:
    percentage_left:int|float = self.app.vid_dl_count/len(self.app.vid_queue)

    #update progress text
    self.app.widgets.download_progress_txt.configure(text=f"{self.app.vid_dl_count} of {len(self.app.vid_queue)} completed")
    self.app.widgets.download_progress_txt.update()

    #update progress bar
    self.app.widgets.download_progress_bar.set(float(percentage_left))
    self.app.widgets.download_progress_bar.update()

  #Runs after all videos has been completed
  def set_complete(self)->None:
    #update progress text
    self.app.widgets.download_progress_txt.configure(text=f"Complete!",text_color=f"{Config.theme["colors"]["progress"]}")
    self.app.widgets.download_progress_bar.set(100)
    self.app.widgets.download_progress_bar.update()
    self.app.is_downloading = False

  #Clears videos from main frame
  def clear_main_frame(self)->None:
    if self.app.is_downloading:
      self.create_dialog_notfication("Cant clear frame because a download is in progress")
      pass
    else:
      try:
        self.destroy_progress_frame()

        self.app.vid_info = {}
        self.app.vid_queue = []
        self.app.vid_frames = []

        self.app.frames.main_frame.destroy()
        self.app.frames.create_main_frame()
        self.app.app_append.append_widgets()
        self.app.app_append.grid_config()
      except:
        raise ValueError("An error occured while clearing widgets")

  #reset feilds
  def reset_feilds(self)->None:
    self.app.widgets.download_progress_txt.configure(text="", text_color="white")
    self.app.widgets.error_txt.configure(text="")
    self.app.widgets.download_progress_bar.set(0)

  #set options
  def set_download_option(self, txt)->None:
    if txt in Config.dl_options:
      Config.dl_cur_option = txt
    elif txt in Config.res_options:
      Config.res_cur_option = txt
    elif txt in Config.theme_options:
      Config.theme_cur_option = txt
      Utils.load_theme()
    self.set_settings_values()
    Utils.save_settings_data()
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
      self.app.is_downloading = False
      raise ValueError("An error occured while fetching video stream, is your internet connected?")

  #Set single video download option
  def set_single_download_option(self, txt, i)->None:
    if self.app.is_downloading:
      self.create_dialog_notfication("Cant change options because a download is in progress")
      pass
    else:
      cur = self.app.vid_queue[i]
      if txt in Config.dl_options:
        cur["dl_opt"] = txt
        cur["size"] = Utils.calculate_file_size(cur)
      elif txt in Config.res_options:
        cur["res_opt"] = txt

      self.update_single_video_info(i, cur)
      self.check_vid_resoultion(i)

  #Sets app widgets to the values in config
  def set_settings_values(self)->None:
    self.app.widgets.options.set(Config.dl_cur_option)
    Utils.load_theme()

    #Apply config values to settings if setting window exists
    if self.settings_window and self.settings_window.winfo_exists():
      self.settings_window.opt.set(Config.dl_cur_option)
      self.settings_window.res_opt.set(Config.res_cur_option)
      self.settings_window.theme_opt.set(Config.theme_cur_option)

  #used for deleting progress frame
  def destroy_progress_frame(self)->None:
    if self.app.frames.progress_frame.winfo_exists() and not self.app.is_downloading:
      self.app.frames.progress_frame.destroy()
      self.app.is_downloading = False
  #used for recreating progress frame
  def check_progress_frame(self)->None:
    if not self.app.frames.progress_frame.winfo_exists():
      self.app.frames.create_progress_frame()
      self.app.widgets.create_progress_widgets()
      self.app.app_append.append_progress_widgets()
      self.app.frames.grid_config()
  #throw error
  def throw_progress_error(self, msg:str)->None:
    self.destroy_progress_frame() #preventing duplicates
    self.check_progress_frame()

    self.app.widgets.error_txt.configure(text=f"{msg}")
    self.app.widgets.error_txt.grid(row=0, column=0, columnspan=2, pady=(10, 0), padx=(0, 0))
  
  #used for warnings
  def create_dialog_notfication(self, msg:str)->None:
    messagebox.showinfo("Notification", f"{msg}")

  #update info
  def update_single_video_info(self, i:int, new_info:dict)->None:
    vid_info_instance = self.app.vid_frames[i]
    vid_info_instance.update_vid_info(new_info)

  #build progress bar for single video
  def create_single_video_progress(self, i:int)->None:
    vid_info_instance = self.app.vid_frames[i]
    vid_info_instance.dl_in_progress()

  #Error handeling for if a video fails to download
  def handle_dl_error(self, i:int)->None:
    vid_info_instance = self.app.vid_frames[i]
    vid_info_instance.handle_error()

  #Updates queue when a video is deleted
  def update_new_queue(self):
    self.app.vid_frames = []

    #recreate the vid frame
    self.destroy_progress_frame()
    
    self.app.frames.main_frame.destroy()
    self.app.frames.create_main_frame()
    self.app.app_append.append_widgets()
    self.app.app_append.grid_config()

    #update video indexs
    for video in self.app.vid_queue:
      if video["index"] != 0:
        video["index"] -= 1

    #rebuild from vid queue
    for video in self.app.vid_queue:
      self.app.vid_info = video
      # Create a new VidInfo instance for the current video
      new_vid_info = VidInfo(parent=self.app)
      new_vid_info.append_vid_info()
      #append it to app parent
      self.app.vid_frames.append(new_vid_info)
      

  #Runs on download button click
  def download_btn(self)->None:
    if self.app.is_downloading:
      self.create_dialog_notfication("Unable to download because a download is already in progress")
      pass

    #Check if progress frame is missing
    self.check_progress_frame()
    self.reset_feilds()

    try:
      self.app.is_downloading = True
      #loop through video frames
      for i in range(len(self.app.vid_frames)):
        #build progress bar for single video
        self.create_single_video_progress(i)
    except:
      self.create_dialog_notfication("an error occured while building progress bars")
      raise ValueError("an error occured while building progress bars")
    try:
      #bottom progress frame
      self.app.frames.progress_frame.grid(row=2, column=0, columnspan=3, sticky="nsew")
      self.app.widgets.download_progress_txt.grid(row=0, column=0, pady=(10, 0), padx=(20, 0))
      self.app.widgets.download_progress_bar.grid(row=1, column=0, columnspan=2, padx=(20, 20), pady=(0, 10), sticky="ew")
      self.app.widgets.error_txt.configure(text="")

      #loop over video queue
      for i, video in enumerate(self.app.vid_queue):
        try:
          cur_vid_yt = YouTube(
              video["url"], 
              on_progress_callback=self.app.vid_frames[i].set_progress, 
              on_complete_callback=self.app.vid_frames[i].set_complete)
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
          #update total download progress
          self.set_progress()
        except:
          self.handle_dl_error(i)
      #mark download queue as completed
      self.set_complete()
    except:
      self.app.is_downloading = False
      self.throw_progress_error(msg="Unable to download")

  def run(self)->None:
    self.app.mainloop()