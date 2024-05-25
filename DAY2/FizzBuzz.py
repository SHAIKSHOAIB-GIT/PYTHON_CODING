# FizzBuzz problem when a number divisble by 3 print fizz
# when a number divsible by 5 print buzz if number divisible by both print fizzbuzz
 
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 3 == 0:
        print("fizz")
    else:
        print(number)             