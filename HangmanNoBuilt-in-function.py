import random

print("                                 Welcome to the Hangman game. Enjoy!")
List = ["pochinki", "rozhok", "prison", "midstein", "militarybase", "georgpool", "school", "quarry", "myltapower",
        "sciencecenter", "shelter"]

computer_choice = random.choice(List)
for i in computer_choice:
    print("_", end="")

num_of_chances = len(computer_choice) + 2
display = []
for i in range(len(computer_choice)):
    display += "_"
answer = ""
letterGuessed = ''
win = False

while num_of_chances > 0 and not win:
    print(f"\nYou have {num_of_chances} chances left to guess.")
    player_choice = input("Enter the guessed letter: ")

    if player_choice in letterGuessed:
        print(f"You guess {player_choice}. You have already guess this letter.")
        continue

    for position in range(len(computer_choice)):
        letter = computer_choice[position]
        if player_choice == letter:
            display[position] = letter
            letterGuessed += letter

    if player_choice not in computer_choice:
        print(f"You guess a wrong letter. You lose a life.")
        num_of_chances -= 1

    for i in display:
        answer += i
    print(answer)
    answer = ""

    if "_" not in display:
        win = True
        print("You Win!")

    if num_of_chances == 0 and not win:
        print("You lose. Try again.")
        break
