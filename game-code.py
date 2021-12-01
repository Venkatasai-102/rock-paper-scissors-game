import random

"""
THE ROCK-PAPER-SCISSORS GAME
type:
r-for rock
p-for paper
s-for scissors

rules:
r wins if r and s comes
p wins if p and r comes
s wins if s and p comes
"""

n = int(input("how many chances would you like to play to finish the game: "))
c = input("would you like to have the first chance?(y/n): ")

ls = ["r", "p", "s"]

score_you = 0
score_comp = 0


def chance():
    return random.choice(ls)


if c == "y":
    while n:
        ch = input("enter your choice: ")
        cm = chance()
        print("the choice of computer is:", cm)
        if ch == "r":
            if cm == "p":
                print("Computer got one point!!")
                score_comp += 1
            elif cm == "s":
                print("You got one point!!")
                score_you += 1
        elif ch == "p":
            if cm == "r":
                print("You got one point!!")
                score_you += 1
            elif cm == "s":
                print("Computer got one point!!")
                score_comp += 1
        else:
            if cm == "r":
                print("Computer got one point!!")
                score_comp += 1
            elif cm == "p":
                print("You got one point!!")
                score_you += 1
                
        n -= 1

else:
    while n:
        cm = chance()
        print("the choice of computer is:", cm)
        ch = input("enter your choice: ")
        if ch == "r":
            if cm == "p":
                print("Computer got one point!!")
                score_comp += 1
            elif cm == "s":
                print("You got one point!!")
                score_you += 1
        elif ch == "p":
            if cm == "r":
                print("You got one point!!")
                score_you += 1
            elif cm == "s":
                print("Computer got one point!!")
                score_comp += 1
        else:
            if cm == "r":
                print("Computer got one point!!")
                score_comp += 1
            elif cm == "p":
                print("You got one point!!")
                score_you += 1

        n -= 1

if score_you > score_comp:
    print("Hurray!! you won the match!!")
else:
    print("You lost!!")
