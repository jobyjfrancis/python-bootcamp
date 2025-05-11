import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

user_input = int(input(f"what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if user_input >= 3 or user_input < 0:
    print("Invalid option")
else:
    print(choices[user_input])
    computer_selection = random.choice(choices)
    print(f"\nComputer chose:")
    print(computer_selection)

    if user_input == 0 and computer_selection == scissors:
        print("You win!")
    elif user_input == 0 and computer_selection == paper:
        print("Computer win!")
    elif user_input == 0 and computer_selection == rock:
        print("Stalemate!")

    if user_input == 1 and computer_selection == rock:
        print("You win!")
    elif user_input == 1 and computer_selection == scissors:
        print("Computer win!")
    elif user_input == 1 and computer_selection == paper:
        print("Stalemate!")

    if user_input == 2 and computer_selection == paper:
        print("You win!")
    elif user_input == 2 and computer_selection == rock:
        print("Computer win!")
    elif user_input == 2 and computer_selection == scissors:
        print("Stalemate!")