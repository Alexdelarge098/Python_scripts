from pathlib import Path
import sys

def count_items(folder):
    files=0
    directories=0

    for item in folder.rglob("*"):
        if item.is_file():
            files += 1
        elif item.is_dir():
            directories +=1

    print(f"Folder: {folder}")
    print(f"Files: {files}") 
    print(f"Directory: {directories}") 

if __name__ == "__main__":
    folder=Path(sys.argv[1])
    count_items(folder)     
