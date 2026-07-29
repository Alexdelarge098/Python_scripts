import os 
import shutil

def file_organizer():
    path = input("Enter the path: ").strip()
    files=os.listdir(path)
    for file in files:
        filename,extension=os.path.splitext(file) #splits the file name and extension
        extension=extension[1:] #splits the extension from the dot

        if extension:
            folder_path=os.path.join(path,extension) #it will helps to create a folder along with the extension name
            if not os.path.exists(folder_path): #if the folder does not exists
                os.makedirs(folder_path) #it will create a folder with the extension name
            shutil.move(os.path.join(path,file),os.path.join(folder_path,file)) #after creating the folder it will move the files along with the extensions to that folder

file_organizer()
