from pathlib import Path
from datetime import datetime
import sys

folder = Path(sys.argv[1])

def find_today_files(folder):
    count = 0
    today = datetime.now().date()

    print("Files Modified Today")
    print("-" * 25)

    for file in folder.rglob("*"):
        if file.is_file():
            modified_date = datetime.fromtimestamp(
                file.stat().st_mtime
            ).date()

            if modified_date == today:
                print(file.name)
                count += 1

    if count == 0:
        print("No files modified today")

    print(f"\nTotal files: {count}")

if __name__ == "__main__":
    find_today_files(folder)
