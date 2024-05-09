def mnt(x):
    months = {
        "jan": 1,
        "feb": 2,
        "mar": 3,
        "apr": 4,
        "may": 5,
        "jun": 6,
        "jul": 7,
        "aug": 8,
        "sep": 9,
        "oct": 10,
        "nov": 11,
        "dec": 12
    }
    a = x.strip()[:3].lower()
    try:
        e = months[a]
        return e
    except:
        raise ValueError('Not a month')
# ========================================================= #


# date_s = ["14-Dec", "12-Apr", "13-Apr", "31-Dec", "1-Jan", "12-Jan"]
date_s = ["31-Feb", "14-Dec", "5-May", "19-Apr", "12-Apr", "13-Apr", "31-Dec", "1-Jan", "12-Jan", "10-Dec"]

print(sorted(date_s, key=lambda m: (mnt(m.split("-")[1]), m.split("-")[0])))



