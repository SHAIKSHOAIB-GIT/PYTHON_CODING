# bulding Rock,Paper,Scissor Game
# Rock Paper Scissors ASCII Art
import random

Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
image = [Rock,Paper,Scissors]

start = int(input("enter your move: 0 for Rock,1 for Paper,3 for Scissors:"))
if start>=3 or start<0:
    print("enter 0,1,3 only")
else:
    print(image[start])

print("computer choose:")
go = random.randint(0,2)
print(image[go])

if start>=3 or start<0:
    print("you lose")
elif start < go:
    print("you lose")
elif start > go:
    print("you win")      
elif start == go:
    print("draw")      

