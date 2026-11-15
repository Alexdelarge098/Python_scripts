import shutil

directories=[
    "/",
    "/var",
    "/tmp",
    "/home"

]

def check_disk_usage():
    print("Print linux Disk usage")
    print("-"*30)
    for directory in directories:
        total,used,free=shutil.disk_usage(directory)
        print(f"Directory:{directory}")
        print(f"Total:{Total}")
        print(f"Used:{used}")
        print(f"free:{free}")
        print("-"*30)
if __name__=="__main__":
    check_disk_usage()