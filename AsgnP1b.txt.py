# Daniel Cheong Jun Jie 200157E group 1
import random

wins = 0
loses = 0
draws = 0
computer = random.randint(0, 2)
for turns in range(3):
    player = int(input("Enter 0(fire), 1(grass) or 2(water): "))
    if player == computer:
        print("Its a draw!")
        draws += 1
        computer = random.randint(0, 2)
    else:
        if player == 0:
            if computer == 1:
                print("You are fire and computer chose grass. You win!")
                wins += 1
            else:
                print("You are fire and computer chose water. You lose!")
                loses += 1
        elif player == 1:
            if computer == 0:
                print("You are grass and computer chose fire. You lose!")
                loses += 1
            else:
                print("You are grass and computer chose water. You win!")
                wins += 1
        elif player == 2:
            if computer == 0:
                print("You are water and computer chose fire. You win!")
                wins += 1
            else:
                print("You are water and computer chose grass. You lose!")
                loses += 1
        else:
            print("You have entered an invalid option. You lose!")
            loses += 1
    computer = random.randint(0, 2)
if wins > loses:
    print("You have won the game! congratulations!")
elif loses > wins:
    print("You have lost the game. Better luck next time!")
else:
    print("You had drawn the game. Your points remain unchanged.")
