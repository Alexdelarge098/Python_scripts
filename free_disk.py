import shutil
import sys

def check_disk_usage(drive):
    folder=sys.argv[1]
    total, used, free = shutil.disk_usage(drive)

    print(f"Drive: {drive}")
    print(f"Total Space: {total // (1024 ** 3)} GB")
    print(f"Used Space: {used // (1024 ** 3)} GB")
    print(f"Free Space: {free // (1024 ** 3)} GB")

if __name__ == "__main__":
    check_disk_usage(folder)

