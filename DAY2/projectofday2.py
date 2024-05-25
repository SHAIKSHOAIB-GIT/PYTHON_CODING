# Random Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','^','^','&','*','(',')','+']

print("Welcome to the Mypassword Generator!")
nr_letters = int(input("How many letters would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

pws = []  
for x in range(1, nr_letters+1):
    char_letters= random.choice(letters)
    pws += char_letters
  
for y in range(1, nr_numbers+1):
    char_numbers= random.choice(numbers)
    pws += char_numbers
 
for z in range(1, nr_symbols+1):
    char_symbols= random.choice(symbols)
    pws += char_symbols

random.shuffle(pws)
print(pws)