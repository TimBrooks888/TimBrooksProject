# calculate_days_between_dates.py
from datetime import datetime

def days_between_dates(date1, date2):
    date_format = "%Y-%m-%d"
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    return abs((d2 - d1).days)

if __name__ == "__main__":
    date1 = input("Enter the first date (YYYY-MM-DD): ")
    date2 = input("Enter the second date (YYYY-MM-DD): ")
    days = days_between_dates(date1, date2)
    print(f"There are {days} days between {date1} and {date2}")
