from pathlib import Path

import sys

def find_largest_file(folder):
    largest_file= None
    largest_size=0

    for file in folder.rglob("*"):
        if file.is_file():
            size=file.stat().st_size

            if size > largest_size:
                largest_size=size
                largest_file=file

    if largest_file:
        print(f"Largest file:{largest_file.name}")
        print(f"Location:{largest_file.parent}")
        print(f"size:{largest_size/(1024*1024):.2f} MB")
    else:
        print("No files found")

if __name__=="__main__":
    folder=Path(sys.argv[1])
    find_largest_file(folder)
