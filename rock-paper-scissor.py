
import random
input_choices = ['rock', 'paper', 'scissors']
a=input("Enter your choice (rock, paper, or scissors): ").lower()
if a not in input_choices:
    print("Invalid choice. Please choose rock, paper, or scissors.")
    a=input("Enter your choice (rock, paper, or scissors): ").lower()

computer_choice = random.choice(input_choices)

print(f"Computer chose: {computer_choice}")
if a == computer_choice:
    print("It's a tie!")
elif (a == 'rock' and computer_choice == 'scissors') or \
     (a == 'paper' and computer_choice == 'rock') or \
     (a == 'scissors' and computer_choice == 'paper'):
    print("You win!")
else:
    print("You lose!")