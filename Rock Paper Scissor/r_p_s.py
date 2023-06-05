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


us=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

#us=user_input

if us == 0:
  print(rock)
elif us == 1:
  print(paper)
else:
  print(scissors)

print("\n Computer choose:\n")

comp=random.randint(0,2)

#comp=computer_input

if comp == 0:
  print(rock)
elif comp == 1:
  print(paper)
else:
  print(scissors)
if us == comp:
  print("draw")
elif us == 0 and comp == 1:
  print("You lose")
elif us == 0 and comp == 2:
  print("You win")
elif us == 1 and comp == 0:
  print("You win")
elif us == 1 and comp == 2:
  print("You lose")
elif us == 2 and comp == 0:
  print("You lose")
else:
  print("You win")
  


