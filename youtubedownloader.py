#importing the module 
from pytube import YouTube 
  
#where to save 
SAVE_PATH = "ubicacion de guardado" #to_do 
  
#link of the video to be downloaded 
a = "https://www.youtube.com/watch?v="
b = str(input("URL DEL VIDEO: https://www.youtube.com/watch?v="))
link = a+b  
try: 
    #object creation using YouTube which was imported in the beginning 
    yt = YouTube(link) 
except: 
    print("Connection Error") #to handle exception 
  
#filters out all the files with "mp4" extension 
mp4files = yt.filter('mp4') 
  
yt.set_filename('GeeksforGeeks Video') #to set the name of the file 
  
#get the video with the extension and resolution passed in the get() function 
d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
try: 
    #downloading the video 
    d_video.download(SAVE_PATH) 
except: 
    print("Some Error!") 
print('Task Completed!')
