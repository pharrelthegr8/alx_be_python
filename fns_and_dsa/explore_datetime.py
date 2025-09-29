from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now().date()
    
    print (f"Current date: {current_date}")
    number_of_days = int(input("Enter the number of days to add to the current date: "))

    future_date = current_date + timedelta(days=number_of_days)
    print("Future date:", future_date)

display_current_datetime()
