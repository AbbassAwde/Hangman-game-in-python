import random
from collections import Counter

# from operator import gt

List = ["apple", "banana", "mango", "pineapple", "kiwi", "orange", "lemon", "strawberry"]

choice = random.choice(List)
#print(choice)

chances = len(choice) + 2
letterGuessed = ''  # list to store the letters guessed by user
correct = 0
flag = 0  # updated when the word guessed correctly

for i in range(len(choice)):
    print("_", end="")
print()

while chances > 0 and flag == 0:
    print()
    print(f"you have {chances} chances left to predict")
    chances -= 1
    guess = input("enter a letter: ")

    # Validation of the guess
    if not guess.isalpha():
        print('Enter only a LETTER')
        continue
    elif guess in letterGuessed:
        print('You have already guessed that letter')
        continue

    if guess in choice:
        k = choice.count(guess)  # k stores the number of times the guessed letter occurs in the word
        for _ in range(k):
            letterGuessed += guess

    for char in choice:
        if char in letterGuessed and Counter(letterGuessed) != Counter(choice):
            print(char, end='')
            correct += 1

        elif Counter(letterGuessed) == Counter(choice):
            print("The word is ", end='')
            print(choice)
            flag = 1
            print("You Won!")
            break  # break from for loop
            break  # break from while loop

        else:
            print("_", end='')

if chances == 0 and Counter(letterGuessed) != Counter(choice):
    print()
    print("You Lose. Try Again.")
    print(f"The word was {choice}.")
