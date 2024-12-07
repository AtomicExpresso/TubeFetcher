class Utils:
  #Calculate total elapsed time
  def calculate_Time(time)->str:
    hrs:int = time // 3600
    mins:int = (time % 3600) // 60
    secs:int = time % 60

    elapsed_time:str = "{h}:{m}:{s}".format(h=hrs, m=mins, s=secs)
    
    return elapsed_time