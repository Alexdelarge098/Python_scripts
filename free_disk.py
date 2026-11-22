import shutil
import sys

def check_disk_usage(drive):
    total, used, free = shutil.disk_usage(drive)

    print(f"Drive: {drive}")
    print(f"Total Space: {total // (1024 ** 3)} GB")
    print(f"Used Space: {used // (1024 ** 3)} GB")
    print(f"Free Space: {free // (1024 ** 3)} GB")

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python disk_usage.py <path>")
        sys.exit(1)

    drive = sys.argv[1]

    check_disk_usage(drive)
