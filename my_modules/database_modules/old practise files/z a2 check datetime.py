import datetime

# Create a datetime object

dt = datetime.datetime(2024, 4, 10, 12, 00, 0)

timestamp = dt.timestamp()
timestamp = 1712238097
timestamp = datetime.datetime.fromtimestamp(timestamp)

print(timestamp.strftime("%Y %m %d \n%I %M %S %p "))
