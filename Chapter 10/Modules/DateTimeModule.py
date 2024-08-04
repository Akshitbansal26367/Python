# import a module named datetime to work with dates as data objects
import datetime

'''today = datetime.date.today()
print(today)'''

# This method returns current year, month, date, day, hour, minute, second and microsecond
x = datetime.datetime.now()
print(x)

# This method returns current year, month, date with time 00:00:00
y = datetime.datetime(2022, 1, 14)
print(y)

# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string
# %d directive for day.
# %Y directive for year.
# %B directive for full month name
# %p directive gives AM/PM
year = x.strftime("%d %B %Y %p")
print(year)
