row1 = ["O","O","O"]
row2 = ["O","O","O"]
row3 = ["O","O","O"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

user_input_str = input("Where do you want to place your treasure? ")

horizontal = int(user_input_str[0])
vertical = int(user_input_str[1])

selected_row = map[vertical-1]
selected_row[horizontal-1] = "X"

print(f"{row1}\n{row2}\n{row3}")





