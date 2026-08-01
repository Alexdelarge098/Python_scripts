import sys
import logging 
from datetime import datetime
from pathlib import Path
import psutil   

CPU_THRESHOLD = 80.0  # CPU usage threshold in percentage
RAM_THRESHOLD = 80.0  # RAM usage threshold in percentage
DISK_THRESHOLD = 80.0  # Disk usage threshold in percentage

LOG_DIR = Path.home() / "system_monitor_logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

today_str = datetime.now().strftime("%Y-%m-%d")
log_file = LOG_DIR / f"system_monitor_{today_str}.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)

def check_system():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
        return False
    logging.info(f"CPU usage is normal: {cpu_usage}%")
    return True

def check_ram():
    ram = psutil.virtual_memory()
    ram_usage = ram.percent
    if ram_usage > RAM_THRESHOLD:
        logging.warning(f"High RAM usage detected: {ram_usage}%")
        return False
    logging.info(f"RAM usage is normal: {ram_usage}%")
    return True

def check_disk():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"High Disk usage detected: {disk_usage}%")
        return False
    logging.info(f"Disk usage is normal: {disk_usage}%")
    return True   # ✅ Added return here

def main():
    logging.info("Starting system monitoring...")
    cpu_status = check_system()
    ram_status = check_ram()
    disk_status = check_disk()
    is_healthy = cpu_status and ram_status and disk_status

    if is_healthy:
        logging.info("System is healthy.")
        print("System's health checks are passed. Details will be stored in logs")
        sys.exit(0)
    else:
        logging.error("System health check failed. Please check the logs for details.")
        print("System's health checks failed. Details will be stored in logs")
        sys.exit(1)

if __name__ == "__main__":
    main()
