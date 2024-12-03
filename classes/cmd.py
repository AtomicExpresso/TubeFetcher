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
      set_dl_clbck=self.set_download_option)
    
    self.settings_window = None

  #For adding videos to main frame
  def add_video(self):
    try:
      self.app.url = self.app.input.get()
      self.app.yt = YouTube(
        self.app.url, 
        on_progress_callback=self.set_progress, 
        on_complete_callback=self.set_complete)
      
      #Fetch video info
      thumbnail = self.app.yt.thumbnail_url
      title = self.app.yt.title
      desc = self.app.yt.description
      duriation = self.app.yt.length
      author = self.app.yt.author

      self.app.vid_info = {"thumbnail": thumbnail, "title":title, "desc":desc, "duriation": duriation, "author":author, "url": self.app.url}
      self.app.vid_queue.append(self.app.vid_info) #Add video to queue

      self.app.append_vid_info()
    except:
      self.app.error_txt.configure(text="Invalid url")
      self.app.error_txt.grid(row=0, column=0, columnspan=2, pady=(120, 0), padx=(0, 0))
      raise ValueError("Invalid url")

  #For specifying download path
  def select_folder(self):
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
  def open_settings_window(self):
    self.settings_window = SettingsWindow(self.app)
    self.settings_window.grab_set()
    self.set_settings_values()

  #Set progress bar progress
  def set_progress(self, stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_left = bytes_downloaded / total_size * 100
    progess_per = int(percentage_left)

    #update progress text
    self.app.download_progress_txt.configure(text=f"{progess_per}%")
    self.app.download_progress_txt.update()

    #update progress bar
    self.app.download_progress_bar.set(float(percentage_left)/100)
    self.app.download_progress_bar.update()

  #Runs after video has been completed
  def set_complete(self,stream, chunk):
    #update progress text
    self.app.download_progress_txt.configure(text=f"Complete!",text_color="green")

  #destroy text and feilds
  def destory_fields(self):
    self.app.header.destroy()
    self.app.download_progress_txt.destroy()
    self.app.error_txt.destroy()
    self.app.input.destroy()
    self.app.download_button.destroy()
    self.app.url = ""
    self.app.yt = None

  #reset feilds
  def reset_feilds(self):
    self.app.download_progress_txt.configure(text="", text_color="white")
    self.app.error_txt.configure(text="")
    self.app.download_progress_bar.set(0)

  #set download option
  def set_download_option(self, txt):
    if txt in Config.dl_options:
      Config.dl_cur_option = txt
      self.set_settings_values()
    elif txt in Config.res_options:
      Config.res_cur_option = txt
      self.set_settings_values()

  #Sets app widgets to the values in config
  def set_settings_values(self):
    self.app.options.set(Config.dl_cur_option)

    #Apply config values to settings if setting window exists
    if self.settings_window and self.settings_window.winfo_exists():
      self.settings_window.opt.set(Config.dl_cur_option)
      self.settings_window.res_opt.set(Config.res_cur_option)

  #Runs on download button click
  def download_btn(self):
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
      self.app.download_progress_txt.grid(row=0, column=0, pady=(120, 0), padx=(20, 0))
      self.app.download_progress_bar.grid(row=1, column=0, columnspan=2, padx=(20, 20), pady=(0, 10), sticky="ew")
      self.app.error_txt.configure(text="")
    except:
      self.app.error_txt.configure(text="Invalid URL")
      self.app.error_txt.grid(row=0, column=0, columnspan=2, pady=(120, 0), padx=(0, 0))

  def run(self):
    self.app.mainloop()