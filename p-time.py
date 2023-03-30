import datetime


d = input()
dt = datetime.datetime.strptime(d, "%H:%M")
dt3 = dt - datetime.timedelta(hours=8)

# ゼロ埋め
print(datetime.datetime.strftime(dt3, '%H:%M'))

# ゼロ埋めなし
print(datetime.datetime.strftime(dt3, '%-H:%-M'))

