hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
overtime = 0

try:
    hours_float = float(hours)
    rate_float = float(rate)
except ValueError or NameError:
    print("Please enter valid hours and rate.")
else:
    if hours_float > 40:
        overtime = hours_float - 40
    else:
        overtime = 0

    payout = (overtime * rate_float * 1.5) + ((hours_float - overtime) * rate_float)
    print(f"Pay: Php{payout}")
