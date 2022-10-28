seconds_number = int(input("Enter the number of seconds:"))

days = seconds_number // (3600 * 24)
days_value = seconds_number % (3600 * 24)
hour = days_value // 3600
hour_value = days_value % 3600
min = hour_value // 60
seconds = hour_value % 60

print("Days:", days, end = " - ")
print(hour,min,seconds, sep =":")



