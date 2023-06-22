print("Welcome to python pizza Deliveries!")
size = input("What size pizza do you want? S,M,L: ")

bill = 0

if size == "S":
    bill += 15
    print(f"Small size pizza is ${bill} ")
elif size == "M":
    bill += 20
    print(f"Medium size pizza is ${bill}")
elif size == "L":
    bill += 25
    print(f"Large size pizza is ${bill}")

else:
    print("Enter a valid size")

add_pepperoni = input("Do you want to add pepperoni? Y/N ")
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

extra_cheese = input("Want some extra cheese? Y/N ")

if extra_cheese == "Y":
    bill += 1
else:
    print(f"Total bill ${bill}")
