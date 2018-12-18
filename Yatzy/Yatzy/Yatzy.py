
dices = [0,0,0,0,0]
scoreOne = 0
scoreTwo = 0

scoretwo = 0
playerOne = ""
playerTwo = ""
turn = ""

import random

def main ():

    a = True
    while (a == True):
        playerOne = input("Spelare 1: ")
        playerTwo = input("Spelare 2: ")
        if playerOne and playerTwo is "":
            a=True
        elif playerOne and playerTwo is not "":
            a = False    
            
    print(roll())
    dices = roll()
    print(dices)
    turn = "playerOneTurn"
    sumTot()
    print(scoreOne)


def roll ():    
    
    dices=[random.randint(1, 6) for _ in range(6)]
    return dices

def winner ():
    if (scoreOne > scoreTwo):
        print("Spelare 1 vann med : " + p1sum())
    if (scoreTwo > scoreOne):
        print("Spelare 2 vann med : " + p2Sum()) 
    else:
        print("Oavgjort")


def sumTot ():
    if (turn == "playerOneTurn"):
       scoreOne = 0
       for x in dices:
            scoreOneTotal += x

    if (turn == "playerTwo"):
        scoreTwo = 0
        for x in dices:
            scoreTwo += x
    
if __name__ == "__main__": main()

