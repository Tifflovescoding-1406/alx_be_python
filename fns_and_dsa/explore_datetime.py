from datetime import datetime, timedelta

def display_current_datetime():
    current_time = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date
def calculate_future_date():
    try:
        days = int(input("Enter the number of days to add: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Date after {days} days: {formatted_future_date}")
        return future_date
def main():
    display_current_datetime()
    calculate_future_date()

if _name_ == "_main_":
    main()


