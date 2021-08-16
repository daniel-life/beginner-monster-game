# Daniel Cheong Jun Jie 200157E group 1
import random

wins = 0
loses = 0
draws = 0
points = 10
player = True
computer = random.randint(0, 2)
while True:
    if points == 0:
        print("You have no mote points left! end of game!")
        break
    else:
        print("You have", points, "points.")
        rounds = int(input("Enter the amount of points you want to use: "))
        if rounds > points:
            print("You do not have enough points! enter your points again!")
            continue
        elif rounds == -1:
            print("You have quit the game!")
            break
        else:
            for i in range(3):
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
                        print("You have entered an invalid option. You lose the game!")
                        loses += 1
                computer = random.randint(0, 2)
    print("You have", wins, "wins,", draws, "draws and", loses, "loses.")
    if wins > (draws + loses):
        print("You have won the game with", rounds, "points added.")
        points += rounds
    elif loses > (draws + wins):
        print("You have lost the game with", rounds, "points deducted.")
        points -= rounds
    else:
        print("You have drawn the game. Your points remain unchanged.")
    wins = 0
    draws = 0
    loses = 0



