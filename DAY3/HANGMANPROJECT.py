import random

word_list = ["sam", "virat","dhoni","sten","bolt","samson","hyd"]
chosse_word = random.choice(word_list)
print(chosse_word)
display=[]
for letters in chosse_word:
    display+='_'
print(display)

word_len = len(chosse_word)
for given_letter in range(word_len):
    given_letter= input("guess the letter : ").lower()

    for position in range(len(chosse_word)):
        letters = chosse_word[position]
        if letters == given_letter:
            display[position]=letters

print(display)                                     