# Contro Flow if statement

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everthing is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $ 12.")
    
    wants_photo = input("Do you wsant a to have pyoto? Y or No.")
    if wants_photo == "Y":
      bill += 3
    else:
      print(f"Your final bill is {bill}")
else:
  print("Sorry, you have to grow taller before you can ride.")
  
  #////////////////////////////
  
#Odd or Even Numbers
  
number = int(input("What is the your number to check?"))
if number % 2 == 0:
  print("This is a even number.")
else:
  print("This is a odd number.")
    
  #////////////////////////////////
  
  # BMI Calculator
  
# Don't change the code be👇
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
  
# write your code below this line 👇
bmi = round(weight / height ** 2)
if bmi < 18.5:
  print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your bmi is {bmi}, you are overweight.")
elif bmi < 35:
  print(f"Your bmi is {bmi}, you are obese.")
else:
  print(f"Your bim is {bmi}, you are clinically obese.")
    
# //////////////////
# Leap year program

# Don't change the code below 👇
year = int(input("What year do you want to check? "))
# Don't change the code below 👇
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leay year")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  
#////////////////////////////////

#pizza order program 
# Don't change the code below👇
print("Welcome to Python Pizza delaveries!")
size = input("What size pizza do you want? Y or N ")
add_depperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# write your code below 👇
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25
if add_depperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
if extra_cheese == "Y":
  bill += 1
print(f"Your final bill is ${bill}")
  
#////////////////////////////////

# Love Calculator 

# Don't change the code below 👇

print("Welcome to the love calculator!")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Write your code below this line 👇
combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(ture) + str(love)

if (love_score < 10) or (love_score >= 90):
  print(f"Your love score is {love_score}, you go together like coke and mentos")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}")
#////////////////////////////////

# Welcome to Tresure Island.

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /

*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('you\'re at a crossroad, where do you want to go? Type "left" or "right".\n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an Island in the middle of the lake. Type "Wait" to wait for a boat. Type "wait" to swim across.\n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house whth 3 doors. One red, One yellow and one blue. Which colour do you choose?\n").lower()
    if choice3 == "red":
      print("It's a room full of firel. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! you win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Gome Over.")
  else:
    print("You got attacked byan angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")
  
#////////////////////////////////////////////
