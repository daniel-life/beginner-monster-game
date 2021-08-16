# Daniel Cheong Jun Jie 200157E group 1
import random

computer = random.randint(0, 2)
player = int(input("Enter 0(fire), 1(grass) or 2(water): "))
if player == computer:
    print("Its a draw!")
else:
    if player == 0:
        if computer == 1:
            print("You are fire and computer chose grass. You win!")
        else:
            print("You are fire and computer chose water. You lose!")
    elif player == 1:
        if computer == 0:
            print("You are grass and computer chose fire. You lose!")
        else:
            print("You are grass and computer chose water. You win!")
    elif player == 2:
        if computer == 0:
            print("You are water and computer chose fire. You win!")
        else:
            print("You are water and computer chose grass. You lose!")
