print("Welcome to tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? "))
num_of_people = int(input("How many people to split the bill? "))

final_amount = (total_bill + (total_bill * tip_percentage / 100)) / num_of_people
final_amount = "{:.2f}".format(final_amount)

print(f"Each person should pay: ${final_amount}")
