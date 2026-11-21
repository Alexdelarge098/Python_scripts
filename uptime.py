import psutil
from datetime import datetime

def get_uptime():
    boot_time=psutil.boot_time()
    boot_time=datetime.fromtimestamp(boot_time)
    current_time=datetime.now()

    up_time=current_time-boot_time

    print(f"Boot time:{boot_time}")
    print(f"current_time:{current_time}")
    print(f"up_time:{up_time}")

if __name__ == "__main__":
    get_uptime()
