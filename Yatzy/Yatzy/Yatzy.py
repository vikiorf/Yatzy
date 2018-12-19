
dices = [0,0,0,0,0]

import random

def main ():
    turncount = 1
    turn = 1
    scoreOne = 0
    scoreTwo = 0
    playerOne = input("Spelare 1: ")
    playerTwo = input("Spelare 2: ")

   # while (turncount <= 10):
        if (turn == 1):
            dices = roll()
            print(dices)
            turn += 1
            turncount += 1

            scoreOne += sumTot(dices)
            print(playerOne + " poäng : " + str(scoreOne))

        elif (turn == 2):
            dices = roll()
            print(dices)
            turn -= 1
            turncount += 1

            scoreTwo += sumTot(dices)
            print(playerTwo + " poäng : " + str(scoreTwo))

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

def sumTot (dices):
    sum = 0
    for x in dices:
        sum += x
    return sum
    
if __name__ == "__main__": main()

