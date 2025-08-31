from datetime import date, time, datetime

today = date.today()
now = datetime.now()

print("Today's date: ",today)

print("Date components ")
print("Day: ",today.day)
print("Month: ",today.month)
print("Year: ",today.year)
