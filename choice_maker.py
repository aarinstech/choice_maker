'''
Developer: @aarinstech
Date: 06-08-2022
This program helps to make hard choices without using feelings just like Kanao.
'''

# important module
import random
import time
from datetime import datetime

# class colours 
class cl:
    white = "\033[1;37m"
    grey = "\033[0;37m"
    purple = "\033[0;35m"
    red = "\033[1;31m"
    green = "\033[1;32m"
    yellow = "\033[1;33m"
    cyan = "\033[0;36m"
    cafe = "\033[0;33m"
    blue = "\033[1;34m"

# variable of colours
white=cl.white
grey=cl.grey
purple=cl.purple
red=cl.red
green=cl.green
yellow=cl.yellow
cyan=cl.cyan
cafe=cl.cafe
blue=cl.blue

# random colour in variable color
listcol = (white, grey, purple, red, green, yellow, cyan, cafe, blue)
color = random.choice(listcol)

# ascii 
print(color+'''
\n
\n
░░╔═══╦╗░░░░░░░░░░░░╔═╗╔═╗░░╔╗░░░░░░░░
░░║╔═╗║║░░░░░░░░░░░░║║╚╝║║░░║║░░░░░░░░
░░║║░╚╣╚═╦══╦╦══╦══╗║╔╗╔╗╠══╣║╔╦══╦═╗░
░░║║░╔╣╔╗║╔╗╠╣╔═╣║═╣║║║║║║╔╗║╚╝╣║═╣╔╝░
░░║╚═╝║║║║╚╝║║╚═╣║═╣║║║║║║╔╗║╔╗╣║═╣║░░
░░╚═══╩╝╚╩══╩╩══╩══╝╚╝╚╝╚╩╝╚╩╝╚╩══╩╝░░
\n
\n
''')

# start or quit
print("Enter 1 to start.")
print("\n")
print("Enter 2 to Quit.")
print("\n")

# input the choice
user_choice = input("Enter your choice: ")
user_choice = int(user_choice)
print("\n")

# if choice is 2
if user_choice == 2:
    print(purple+"Thank you for using Choice Maker.")
    exit()
# if choice is 1
# main------------
elif user_choice == 1:
    first_choice = input("Enter your first choice: ")
    print("\n")
    second_choice = input("Enter your second choice: ")
    print("\n")
    list_of_choice = [first_choice, second_choice]
    final_choice = random.choice(list_of_choice)
    print(red+"It's your final choice. You have to do it, no matter what.")
    print("\n")
    print(green+final_choice)
    # Choice date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("\n")
    print(grey+"Date & Time: ", grey+dt_string)
    print("\n")
    time.sleep(3)
    exit()
# if input is wrong
else:
    print(red+"Wrong Input! Try Executing the program again.")
    exit()