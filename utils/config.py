import os

#Config class is global state
class Config:
  #-Theme
  theme = {
    "colors": {
        "primary": "#1f1f1f",
        "secondary": "#282828",
        "button": {
            "default": "#363535",
            "hover": "#403f3f",
            "download": {
                "default": "#4ea94b",
                "hover": "#2d6e2b"
            }
        },
        "progress": "#4ea94b",
        "error": "#eb4034"
    },
    "text_colors": {
        "success": "#4ea94b",
        "primary": "#ffffff"
    }
  }

  #-Window size
  primary_win_width:int = 500
  primary_win_height:int = 350

  secondary_win_width:int = 400
  secondary_win_height:int = 300

  #-max text length
  max_paragraph_len:int = 500

  #-Options
  dl_options:list[str] = ["Video + Audio", "Audio"]
  res_options:list[str] = ["1080p", "720p", "360p"]
  theme_options:list[str] = ["Dark", "Midnight", "Ocean Blue", "Coffee"]

  #-Current settings
  dl_cur_option:str = dl_options[0]
  res_cur_option:str = res_options[0]
  theme_cur_option:str = theme_options[0]
  #Downloaded content goes here
  folder_path:str = os.path.join(os.path.expanduser("~"), "Downloads")