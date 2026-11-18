from datetime import datetime
import sys

target_date=sys.argv[1]

target=datetime.strptime(target_date, "%Y-%m-%d")
today=datetime.now()

days_left=(target-today).days


print(f"Days until {target_date}: {days_left}")