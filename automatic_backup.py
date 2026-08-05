import os 
import shutil
import datetime
import schedule
import time

source_dir = input("Enter the source directory path to backup: ")
destination_dir = input("Enter the destination directory path for backup: ")

def backup_files(source, dest):
    today=datetime.date.today()
    dest_dir=os.path.join(dest, str(today))

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Backup directory created: {dest_dir}")

    # copy files and subdirectories from source to destination date folder
    if not os.path.exists(source):
        print(f"Source directory does not exist: {source}")
        return
    for item in os.listdir(source):
        s = os.path.join(source, item)
        d = os.path.join(dest_dir, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

    print(f"Backup completed to: {dest_dir}")
        

backup_files(source_dir, destination_dir)

schedule.every().day.at("17:24").do(lambda: backup_files(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(10)
