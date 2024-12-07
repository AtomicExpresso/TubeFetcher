from tkinter import messagebox
import customtkinter as ctk
from pytubefix import YouTube, Playlist
from classes.app import Application
from classes.Window import SettingsWindow
from classes.config import Config

class AppCmd:
  def __init__(self):
    self.app = Application(
      download_btn_clbck=self.download_btn, 
      folder_path_clbck=self.select_folder, 
      add_vid_clbck=self.add_video,
      st_clbck=self.open_settings_window,
      set_dl_clbck=self.set_download_option,
      set_dl_single_clbck=self.set_single_download_option)
    
    self.settings_window = None

  #For adding videos to main frame
  def add_video(self)->None:
    try:
      self.app.url = self.app.input.get()
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
      self.app.append_vid_info()
    except:
      self.app.error_txt.configure(text="Invalid url")
      self.app.error_txt.grid(row=0, column=0, columnspan=2, pady=(120, 0), padx=(0, 0))
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
      self.app.error_txt.configure(text="Incorrect file path")
      self.app.error_txt.grid(row=0, column=0, columnspan=2, pady=(120, 0), padx=(0, 0))
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
    self.app.download_progress_txt.configure(text=f"{progess_per}%")
    self.app.download_progress_txt.update()

    #update progress bar
    self.app.download_progress_bar.set(float(percentage_left)/100)
    self.app.download_progress_bar.update()

  #Runs after video has been completed
  def set_complete(self,stream, chunk)->None:
    #update progress text
    self.app.download_progress_txt.configure(text=f"Complete!",text_color="green")

  #destroy text and feilds
  def destory_fields(self)->None:
    self.app.header.destroy()
    self.app.download_progress_txt.destroy()
    self.app.error_txt.destroy()
    self.app.input.destroy()
    self.app.download_button.destroy()
    self.app.url = ""
    self.app.yt = None

  #reset feilds
  def reset_feilds(self)->None:
    self.app.download_progress_txt.configure(text="", text_color="white")
    self.app.error_txt.configure(text="")
    self.app.download_progress_bar.set(0)

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

      #Change file size based on stream, division converts it from bytes to megabytes and rounds 2 decimal places
      file_size = cur["stream"].filesize / 1048576
      cur["size"] = f"{file_size:.2f} MB"
    except:
      raise ValueError("An error occured while fetching video stream, is your internet connected?")

  #Set single video download option
  def set_single_download_option(self, txt, i)->None:
    if txt in Config.dl_options:
      self.app.vid_queue[i]["dl_opt"] = txt
    elif txt in Config.res_options:
      self.app.vid_queue[i]["res_opt"] = txt
    self.check_vid_resoultion(i)

  #Sets app widgets to the values in config
  def set_settings_values(self)->None:
    self.app.options.set(Config.dl_cur_option)

    #Apply config values to settings if setting window exists
    if self.settings_window and self.settings_window.winfo_exists():
      self.settings_window.opt.set(Config.dl_cur_option)
      self.settings_window.res_opt.set(Config.res_cur_option)

  #Runs on download button click
  def download_btn(self)->None:
    self.reset_feilds()
    try:
      self.app.url = self.app.input.get()

      #Check options for video + audio, audio or playlist
      if self.app.options.get() == 'Video':
        self.app.yt = YouTube(
          self.app.url, 
          on_progress_callback=self.set_progress, 
          on_complete_callback=self.set_complete)

        #Download at desired resoultion
        if Config.res_cur_option == "Best":
          self.app.yt.streams.get_highest_resolution().download(f"{self.app.folder_path}")
        else:
          self.app.yt.streams.get_highest_resolution().download(f"{self.app.folder_path}")
      elif self.app.options.get() == 'Playlist':
        self.app.yt = Playlist(
          self.app.url, 
          on_progress_callback=self.set_progress, 
          on_complete_callback=self.set_complete)
        
        for video in self.app.yt.videos:
          ys = video.streams.get_highest_resolution()
          ys.download("./videos")
      
      #Append progress content to frame
      self.app.progress_frame.grid(row=2, column=0, columnspan=3, sticky="nsew")
      self.app.download_progress_txt.grid(row=0, column=0, pady=(120, 0), padx=(20, 0))
      self.app.download_progress_bar.grid(row=1, column=0, columnspan=2, padx=(20, 20), pady=(0, 10), sticky="ew")
      self.app.error_txt.configure(text="")
    except:
      self.app.error_txt.configure(text="Invalid URL")
      self.app.error_txt.grid(row=0, column=0, columnspan=2, pady=(120, 0), padx=(0, 0))

  def run(self)->None:
    self.app.mainloop()