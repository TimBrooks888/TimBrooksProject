# simple_calendar_generator.py
import calendar

def generate_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    return cal

if __name__ == "__main__":
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    cal = generate_calendar(year, month)
    print(calendar.month_name[month], year)
    print("Mo Tu We Th Fr Sa Su")
    for week in cal:
        print(" ".join(f"{day:2}" if day != 0 else "  " for day in week))
