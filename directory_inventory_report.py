from pathlib import Path
import sys

def inventory_report(folder):
    total_files = 0
    total_folders = 0
    total_size = 0

    for item in folder.rglob("*"):

        if item.is_file():
            total_files += 1
            total_size += item.stat().st_size

        elif item.is_dir():
            total_folders += 1

    print("\nDirectory Inventory Report")
    print("-" * 30)
    print(f"Folder        : {folder}")
    print(f"Total Files   : {total_files}")
    print(f"Total Folders : {total_folders}")
    print(f"Total Size    : {total_size / (1024 * 1024):.2f} MB")

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python inventory.py <folder_path>")
        sys.exit(1)

    folder = Path(sys.argv[1])

    if folder.exists():
        inventory_report(folder)
    else:
        print("The folder does not exist")
