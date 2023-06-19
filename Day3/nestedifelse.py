height = int(input("Enter your height: "))

if height > 120:
    print("You can ride")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5")
    elif age < 18:
        print("Please pay $7")
    else:
        print("please pay $12")
else:
    print("You are not eligible")
