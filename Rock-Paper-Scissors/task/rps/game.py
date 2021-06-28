import random


def who_is_win(user_, computer_):
    if user_ == computer_:
        return "draw"
    index_ = user_vars.index(user_)
    first_ = user_vars[:index_]
    second_ = user_vars[index_ + 1:]
    temp_ = second_ + first_
    if computer_ in temp_[:int(len(temp_) / 2)]:
        return "computer"
    elif computer_ in temp_[int(len(temp_) / 2):]:
        return "user"
    else:
        return "draw"


user_rating = 0
print("Enter your name: ", end="")
user_name = input()
print("Hello,", user_name, sep=" ")
user_vars = input().split(",")
if len(user_vars) < 2:
    user_vars = ["rock", "paper", "scissors"]
print("Okay, let's start")
with open("rating.txt", "r") as rating_file:
    for line in rating_file.readlines():
        if user_name == line.split(" ")[0]:
            user_rating = int(line.split(" ")[1])

while True:
    items = ["rock", "paper", "scissors"]
    combinations = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    user_choice = input()
    if user_choice == "!exit":
        print("Bye!")
        break
    if user_choice == "!rating":
        print("Your rating:", user_rating, sep=" ")
    computer_choice = random.choice(user_vars)
    if user_choice not in user_vars:
        print("Invalid input")
        continue
    result = who_is_win(user_choice, computer_choice)
    if result == "computer":
        print("Sorry, but the computer chose {}".format(computer_choice))
        continue
    elif result == "draw":
        print("There is a draw ({})".format(computer_choice))
        user_rating += 50
        continue
    elif result == "user":
        print("Well done. The computer chose {} and failed".format(computer_choice))
        user_rating += 100
        continue
    print("Invalid input")
