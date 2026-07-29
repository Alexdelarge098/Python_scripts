import os
from pytubefix import YouTube 

def downlad_video(link):
    backup_dir="C:/Users/prity/Downloads/Youtube Download folder"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        print(f"directory:{backup_dir} is succesfully created")
    yt=YouTube(link)
    print("title:", yt.title)
    print("Views: ", yt.views)
    stream=yt.streams.get_highest_resolution() 
    stream.download("C:/Users/prity/Downloads/Youtube Download folder")
    download_path = os.path.join(backup_dir, stream.default_filename)
    print(f"Video downloaded succesfully to the path:{download_path}")

link=input("Enter the url of the video you want to download: ")
downlad_video(link)


