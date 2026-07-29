from pytubefix import YouTube #importing the pytube library
from sys import argv #Importing the argv module from sys library to take input from command line

link=argv[1] #link is the first argument taken from command line
yt=YouTube(link) #creating the youtube object with the link provided  

#viewing the title and views of the video
print("title:", yt.title) 
print("Views: ", yt.views)

#downloading the video in highest resolution
yd=yt.streams.get_highest_resolution()

#path to download the video
yd.download('C:/Users/prity/Downloads/Youtube Download folder')
