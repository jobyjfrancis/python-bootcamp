print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("You're at a cross road. Where do you want to go?")
left_or_right = input('''\t Type "left" or "right"\n''').lower()
if left_or_right == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    wait_or_swim = input('''\t Type "wait" to wait for a boat. Type "swim" to swim across\n''').lower()
    if wait_or_swim == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        red_or_yellow_or_blue = input('''\t One red, one yellow and one blue. Which colour do you choose?\n''')
        if red_or_yellow_or_blue == "yellow":
            print("You found the treasure! You Win!")
        elif red_or_yellow_or_blue == "red":
            print("It's a room full of fire. Game Over.")
        elif red_or_yellow_or_blue == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("Invalid option!!!")
    elif wait_or_swim == "swim":
        print("You get attacked by an angry trout. Game Over.")
    else:
        print("Invalid option!!!")
elif left_or_right == "right":
    print("You fell into a hole. Game Over.")
else:
    print("Invalid option!!!")


