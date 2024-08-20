# By default, these calendars have Monday as the first day of the week(0), and Sunday as the last(6)
# calendar is an inbuilt module
import calendar

print("Enter the calender in (m/d/y) format : ", end="")
m, d, y = map(int, input().split())

# weekday(y, m, d) method returns the weekday number
w = calendar.weekday(y, m, d)
lst = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("The day is", lst[w])
