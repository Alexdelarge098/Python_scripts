import shutil

drive="/home/prityushs/Python"

def check_disk_uage(drive):
    total,used,free=shutil.disk_usage(drive)

    print(f"Drive:{drive}")
    print(f"total Space:{total // {1024**3}} GB")
    print(f"Used Space:{used // {1024**3}} GB")
    print(f"Free space:{free // {1024 **3}} GB")

if __name__=="__main__":
    check_disk_usage(drive)

