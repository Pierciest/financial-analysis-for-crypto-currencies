from datetime import date, timedelta


def daterange(Date):
    today = date.today()
    for n in range(int((today - Date).days) + 1):
        yield Date + timedelta(n)

