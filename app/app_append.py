#Handles appending widgets to app
class AppAppend:
  def __init__(self, parent):
    self.parent = parent

  #Configures grid positions
  def grid_config(self)->None:
    #configure grid
    self.parent.grid_columnconfigure(0, weight=0)
    self.parent.grid_columnconfigure(1, weight=1)
    self.parent.grid_columnconfigure(2, weight=0)
    
    self.parent.grid_rowconfigure(0, weight=0)
    self.parent.grid_rowconfigure(1, weight=1)
    self.parent.grid_rowconfigure(2, weight=0)
    self.parent.grid_rowconfigure(3, weight=0)

    #confiigure frame grid
    self.parent.frames.grid_config()

  #append progress frame
  def append_progress_widgets(self)->None:
    self.parent.frames.progress_frame.grid(row=2, column=0, columnspan=3, sticky="nsew")
  #append top frame widgets
  def append_top_widgets(self)->None:
    self.parent.frames.top_frame.grid(row=0, column=0, columnspan=3, sticky="sew")
    self.parent.widgets.input.grid(column=0, columnspan=3, row=0, pady=10, padx=(20, 90), sticky="ew")
    self.parent.widgets.addvideo_btn.grid(column=1, row=0, pady=10, padx=(0, 0), sticky="e")
    self.parent.widgets.settings_btn.grid(column=2, row=0, pady=10, padx=(20, 20), sticky="e")
  #append bottom frame widgets
  def append_bottom_widgets(self)->None:
    self.parent.frames.bottom_frame.grid(row=3, column=0, columnspan=3, sticky="nsew")
    self.parent.widgets.folder_btn.grid(column=0, row=0, pady=10, padx=(20, 10), sticky="w")
    self.parent.widgets.trash_btn.grid(column=2, row=0, pady=10, padx=(0, 10), sticky="e")
    self.parent.widgets.download_button.grid(column=3,row=0, padx=(0, 20), pady=(10,10), sticky="e")
    self.parent.widgets.options.grid(column=1,row=0, padx=10, pady=(10,10), sticky="w")
  #append main frame widgets
  def append_main_widgets(self)->None:
    self.parent.frames.main_frame.grid(row=1, column=0, columnspan=3, sticky="nsew")

  #Appends widgets to frames
  def append_widgets(self)->None:
    #frames
    self.append_top_widgets()
    self.append_main_widgets()
    self.append_progress_widgets()
    self.append_bottom_widgets()