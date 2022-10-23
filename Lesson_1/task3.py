import time
import datetime

timestamp = int(input("Enter number of seconds: "))
value = datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)

print("=============================")
print("Year: " f"{value:%Y}")
print("Month: " f"{value:%m}")
print("Day: " f"{value:%d}")
print("=============================")
print("Hours: " f"{value:%H}")
print("Minutes: " f"{value:%M}")
print("Seconds: " f"{value:%S}")
print("=============================")
print( f"{value:%Y-%m-%d %H:%M:%S}")
print("=============================")