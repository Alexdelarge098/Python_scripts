import os
import shutil

def new_file_organizer():
    path = input("enter the path:").strip()
    files=os.listdir(path) 

    for file in files:
        filename, extension=os.path.splitext(file)
        extension=extension[1:]

        folder_path=os.path.join(path,extension)
        if os.path.exists(folder_path):
            shutil.move(os.path.join(path,file),os.path.join(folder_path,file))
        else:
            os.makedirs(folder_path)
            shutil.move(os.path.join(path,file),os.path.join(folder_path,file))
            
new_file_organizer()
