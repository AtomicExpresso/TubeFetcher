#Config class is global state
class Config:
  #Theme
  primary_color:str = f"#1f1f1f"
  secondary_color:str = f"#282828"
  btn_color:str = f"#363535"
  btn_color_hover:str = f"#403f3f"
  btn_color_download:str = f"#4ea94b"
  progress_color:str = f"#4ea94b"

  #Options
  dl_options:list[str] = ["Video + Audio", "Audio"]
  res_options:list[str] = ["1080p", "720p", "360p"]

  #Current settings
  dl_cur_option:str = dl_options[0]
  res_cur_option:str = res_options[0]

  folder_path:str = "./downloads" #downloaded vids go here