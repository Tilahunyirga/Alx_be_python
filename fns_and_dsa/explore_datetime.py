from datetime import datetime, timedelta
def display_current_datetime():
    date = datetime.now()
    current_date = date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date:"))
    delta = timedelta(days=number_of_days)
    day = datetime.today()
    future_date = day + delta
    result = future_date.strftime("%y-%m-%d")

    print(f"Future date: {result}")

display_current_datetime()
calculate_future_date()

