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

#Write your code below this line 👇
# rock v paper = w rock
# rock v scissors = w scissors
# paper v scissors = w scissors
# rock v rock = draw
# scissors v scissors = draw
# paper v paper = draw
import random

images = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = int(random.randint(0, 2))

if user >= 3 or user < 0:
  print("You typed an invalid number.")
else:
  print(images[user])
  print(f"Computer chose: {computer}")
  print(images[computer])
  
  if user == 0 and computer == 2:
    print("You win!")
  elif computer == 0 and user == 2:
    print("You lose!")
  elif computer > user:
    print("You lose!")
  elif user > computer:
    print("You win!")
  elif computer == user:
    print("It's a draw")