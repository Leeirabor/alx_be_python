from datetime import datetime, timedelta




print("future date: ")

def display_current_datetime():
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    number_of_days
    future_date = current_date + timedelta(days=number_of_days)
    future_format = future_date.strftime("%Y-%m-%d")
    print (f"future_date is: {future_format}")

display_current_datetime()