import os
import shutil
import pathlib
from pathlib import Path

downloads_folder=Path.home() / "Downloads"

DEST_FOLDERS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Executables": [".exe", ".msi"],
    "Archives": [".zip", ".tar", ".gz", ".7z", ".rar"],
    "Media": [".mp4", ".mkv", ".mp3", ".wav"],
    "Code": [".py", ".json", ".sh", ".yaml", ".yml", ".sql"]
}

def organize_downloads():
    if not downloads_folder.exists():
        print(f"ERROR: Directory '{downloads_folder}' does not exist.")
        return  

    print(f"Organizing files in '{downloads_folder}'...")

    for item in os.listdir(downloads_folder):
        file_path = downloads_folder / item
        if file_path.is_dir():
            continue  

        file_ext=file_path.suffix.lower()
        moved=False

        for foldername,extensions in DEST_FOLDERS.items():
            if file_ext in extensions:
                target_folder=downloads_folder / foldername
                target_folder.mkdir(exist_ok=True)
                shutil.move(str(file_path), str(target_folder / item))
                print(f"Moved: '{item}' -> {foldername}/")
                moved=True
                break
        if not moved and file_ext != "":
            target_folder=downloads_folder / "Others"
            target_folder.mkdir(exist_ok=True)
            shutil.move(str(file_path), str(target_folder / item ))
            print(f"Moved: '{item}' -> {foldername}/")

if __name__ == "__main__":
    organize_downloads()
