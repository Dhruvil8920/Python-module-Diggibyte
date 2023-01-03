import calendar
year=(input().split())
month=year[0]
day=year[1]
year=int(year[2])
dates=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
if int(month)<=9:
    month=month.replace("0","")
    month=int(month)
else:
    month=int(month)
if int(day)<=9:
    day=day.replace("0","")
    day=int(day)
else:
    day=int(day)
day=calendar.weekday(year,month,day)
print(dates[day].upper())
