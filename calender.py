import time
from datetime import datetime
date_input = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
dt = datetime.strptime(date_input, "%Y-%m-%d %H:%M:%S")
print("a) Date and time:", dt)
print("b) Year:", dt.year)
print("c) Month of the year:", dt.month)
print("d) Week number of the year:", dt.isocalendar()[1])
print("e) Weekday of the week:", dt.strftime("%A"))
print("f) Day of year:", dt.timetuple().tm_yday)
print("g) Day of month:", dt.day)
print("h) Day of week:", time.strftime("%A", dt.timetuple()))

~                                                                             
~                                                                             
~                                                                             
~           
