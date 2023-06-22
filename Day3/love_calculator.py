print("Welcome to love calculator!")

name1 = input("What is your name? \n")
name2 = input("What is your partners name? \n")

name1_s = name1.lower()
name2_s = name2.lower()

t = name1_s.count("t") + name2_s.count("t")
r = name1_s.count("r") + name2_s.count("r")
u = name1_s.count("u") + name2_s.count("u")
e = name1_s.count("e") + name2_s.count("e")

sum_true = str(t + r + u + e)

l = name1_s.count("l") + name2_s.count("l")
o = name1_s.count("o") + name2_s.count("o")
v = name1_s.count("v") + name2_s.count("v")
e = name1_s.count("e") + name2_s.count("e")

sum_love = str(l + o + v + e)

total = int(sum_true + sum_love)

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together")
else:
    print(f"Your score is {total}")
