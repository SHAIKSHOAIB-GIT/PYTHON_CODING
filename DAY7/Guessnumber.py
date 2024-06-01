import random

easy_lives = 10
hard_lives = 5

def check(guess, number, truns):
    if guess > number:
        print("too high")
        return truns-1    
    elif guess < number:
        print("too low")  
        return truns-1
    else:
        print("you win")

def level():
    level =(input(f"choose diffculty levels easy 'y' or hard 'h': "))
    if level == "y" :
        return easy_lives
    else:
        return hard_lives
def game():  
    print("Guess the Number Game ")
    print("I'm thinking b/w 1 to 100 \n ")  
    number =random.randint(1,100)
    print(number)
    truns = level()

    not_continue_game = False
    while not not_continue_game:
        print(f"you have left {truns} lives")
        guess =int(input("enter a number : "))
        truns = check(guess, number, truns)
        if guess == number:
            not_continue_game = True
        elif truns == 0 :
            print(f"you loose")
            not_continue_game = True   
    
game()



    