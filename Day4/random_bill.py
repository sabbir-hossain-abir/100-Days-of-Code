import random

string_name = input("Give the names separated by comma(, ) :")

names = string_name.split(", ")

nam_len = len(names)

random_num = random.randint(0, nam_len-1)

person_who_will_pay = names[random_num]

print(person_who_will_pay + " is going to pay the bill today.")
