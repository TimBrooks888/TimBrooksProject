# fun_months_between_dates.py
from datetime import datetime

def months_between_dates(date1, date2):
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((d1.year - d2.year) * 12 + d1.month - d2.month)

date1 = "2024-01-01"
date2 = "2024-07-01"
print(f"Months between {date1} and {date2}: {months_between_dates(date1, date2)}")
