class Utils:
  #Calculate total elapsed time for videos/audio
  def calculate_Time(time)->str:
    try:
      hrs:int = time // 3600
      mins:int = (time % 3600) // 60
      secs:int = time % 60

      elapsed_time:str = "{h}:{m}:{s}".format(h=hrs, m=mins, s=secs)
      
      return elapsed_time
    except:
      raise ValueError("An error occured while calculating time")
  
  #Calculates file size for videos/audio
  def calculate_file_size(cur)->str:
    try:
      #Change file size based on stream, division converts it from bytes to megabytes and rounds 2 decimal places
      file_size = cur["stream"].filesize / 1048576
      mb_size = f"{file_size:.2f} MB"

      return mb_size
    except:
      raise ValueError("An error occured while calculating file size")