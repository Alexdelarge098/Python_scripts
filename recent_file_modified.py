from pathlib import Path
from datetime import datetime
import sys

target_directory = Path(sys.argv[1])


def find_latest_file(folder):
    latest_file = None
    latest_time = 0

    for file in folder.rglob("*"):
        if file.is_file():
            modified_time = file.stat().st_mtime
            if modified_time > latest_time:
                latest_time = modified_time
                latest_file = file
    if latest_file:
        print(f"Latest file:{latest_file.name}")
        print(f"Location: {latest_file.parent}")
        readable_time=datetime.fromtimestamp(latest_time)
        print(
            f"Modifed on :"
            f"{readable_time.strftime('%Y-%m-%d %H:%M:%S')}"
        )

if __name__== "__main__":
    find_latest_file(target_directory)