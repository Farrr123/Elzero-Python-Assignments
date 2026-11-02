import datetime

date = datetime.datetime(2021, 6, 25)
date_now = datetime.datetime.now()

print(f"Days From {date} To {date_now} Is => {(date_now - date).days}")

print("=" * 50)

print(date_now.strftime("%d %B %Y"))
print(date_now.strftime("%d, %B, %Y"))
print(date_now.strftime("%d / %B / %Y"))
print(date_now.strftime("%d - %B - %Y"))
