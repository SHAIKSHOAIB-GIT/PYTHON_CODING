# Iam going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails"
import random

test_seed = int(input("create a seed number:"))
random.seed(test_seed)

# frist method
random_coin = random.randint(0, 1)
if random_coin == 1:
    print("Heads")
else:
    print("Tails")    


# second method 

heads_or_tails = ["Heads", "Tails"]
random_coin = random.choice(heads_or_tails)
print(random_coin)