age = input("Enter your age: ")

remaining_age = 90 - int(age)

days_remaining = remaining_age * 365
weeks_remaining = remaining_age * 52
months_remaining = remaining_age * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left")
