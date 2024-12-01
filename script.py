import tkinter
import customtkinter
from pytubefix import YouTube, Playlist

class application(customtkinter.CTk):
  def __init__(self):
    super().__init__()
    self.width = 500
    self.height = 350
    self.geometry(f"{self.width}x{self.height}")
    self.title("Youtube downloader")

    self.url = ""
    self.yt = None

    #Texts
    self.header = customtkinter.CTkLabel(self, text="Youtube Downloader", fg_color="transparent", font=("ariel", 35))
    self.download_progress_txt = customtkinter.CTkLabel(self, text="25%", fg_color="transparent", font=("ariel", 20))
    self.error_txt = customtkinter.CTkLabel(self, text_color="red", text="Error", fg_color="transparent", font=("ariel", 20))

    #input box
    self.input = customtkinter.CTkEntry(self, width=350, height=30, corner_radius=5, placeholder_text="Video URL")

    #buttons
    self.download_button = customtkinter.CTkButton(self, text="Download", command=self.download_btn)
    self.options = customtkinter.CTkOptionMenu(self, values=["Video", "Playlist"])

    #progress bar
    self.download_progress_bar = customtkinter.CTkProgressBar(self, orientation="horizontal", width=250)

    #append to grid
    self.grid_columnconfigure(0, weight=1)
    self.grid_columnconfigure(1, weight=1)

    self.header.grid(row=0, column=0,  columnspan=2, pady=20, sticky="ew")
    self.input.grid(column=0, row=1,  columnspan=2, pady=20, padx=50, sticky="ew")
    self.download_button.grid(column=0,row=3, padx=20, pady=1, sticky="ew")
    self.options.grid(column=1,row=3, padx=10, pady=1, sticky="ew")
  
  def set_progress(self, stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_left = bytes_downloaded / total_size * 100
    progess_per = int(percentage_left)

    #update progress text
    self.download_progress_txt.configure(text=f"{progess_per}%")
    self.download_progress_txt.update()

    #update progress bar
    self.download_progress_bar.set(float(percentage_left)/100)
    self.download_progress_bar.update()

  #Runs after video has been completed
  def set_complete(self,stream, chunk):
    #update progress text
    self.download_progress_txt.configure(text=f"Complete!",text_color="green")

  #destroy text and feilds
  def destory_fields(self):
    self.header.destroy()
    self.download_progress_txt.destroy()
    self.error_txt.destroy()
    self.input.destroy()
    self.download_button.destroy()
    self.url = ""
    self.yt = None

  #reset feilds
  def reset_feilds(self):
    self.download_progress_txt.configure(text="", text_color="white")
    self.error_txt.configure(text="")
    self.download_progress_bar.set(0)

  #Runs on download button click
  def download_btn(self):
    self.reset_feilds()
    try:
      self.url = self.input.get()

      #Check options for video or playlist
      if self.options.get() == 'Video':
        self.yt = YouTube(self.url, on_progress_callback=self.set_progress, on_complete_callback=self.set_complete)
        self.yt.streams.get_highest_resolution().download("./videos")
      elif self.options.get() == 'Playlist':
        self.yt = Playlist(self.url, on_progress_callback=self.set_progress, on_complete_callback=self.set_complete)
        
        for video in self.yt.videos:
          ys = video.streams.get_highest_resolution()
          ys.download("./videos")
      

      self.download_progress_txt.grid(row=4, column=0, columnspan=2, pady=(120, 0), padx=(0, 0))
      self.download_progress_bar.grid(row=5, column=0, columnspan=2, padx=(20, 20), sticky="ew")
      self.error_txt.configure(text="")
    except:
      self.error_txt.configure(text="Invalid URL")
      self.error_txt.grid(row=4, column=0, columnspan=2, pady=(120, 0), padx=(0, 0))


#Run application
def run():
  customtkinter.set_appearance_mode("System")
  customtkinter.set_default_color_theme("blue")

  app = application()

  #Run
  app.mainloop()

run()