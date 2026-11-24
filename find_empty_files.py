from pathlib import Path
import sys

def find_empty_files(folder):
    count=0

    print("Empty files report")
    print("-"*20)
    for file in folder.rglob("*"):
        if file.is_file() and file.stat().st_size == 0:
            print(file)
            count +=1
    if count == 0:
        print("THere are no empty files")

if __name__ == "__main__":
     folder=Path(sys.argv[1])
     find_empty_files(folder)

