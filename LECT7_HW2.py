
date_s = ["14-Dec", "12-Apr", "13-Apr", "31-Dec", "01-Jan", "12-Jan"]


print(sorted(date_s))

print(sorted(date_s, key=lambda date: [d for d in date.split("-")][0]))

print(sorted(date_s, key=lambda date: [d for d in date.split("-")][1]))