#x pattern
def print_name_in_x(name):
    name_length = len(name)
    for i in range(name_length):
        for j in range(name_length):
            if i == j or i + j == name_length - 1:
                print(name[j], end='')
            else:
                print(' ', end='')
        print()

user_name = input("Enter your name: ")
print_name_in_x(user_name)

#v patterndef 
def print_v_pattern(username):
    n = len(username)
    for i in range(n):
        for j in range(n*2-1):
            if j == i or j == (n*2-2-i):
                print(username[i], end="")
            else:
                print(" ", end="")
        print()

username = input("Enter your username: ")
print_v_pattern(username)

#z pattern
def print_z_pattern(name):
    length = len(name)
    for i in range(length):
        for j in range(length):
            if i == 0 or i == length - 1:
                print(name[j], end=' ')
            elif i + j == length - 1:
                print(name[j], end=' ')
            else:
                print(' ', end=' ')
        print()

# Taking user input for the name
name = input("Enter your name: ")
print("Z pattern for your name:")
print_z_pattern(name)

import datetime

current_datetime = datetime.datetime.now()
current_date = current_datetime.strftime("%Y-%m-%d")
current_time = current_datetime.strftime("%H:%M:%S")
current_day = current_datetime.strftime("%A")

print("Current date:", current_date)
print("Current time:", current_time)
print("Day of the week:", current_day)







    