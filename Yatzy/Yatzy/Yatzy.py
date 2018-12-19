
dices = [0,0,0,0,0]

import random

def main ():

    
    turn = 1
    scoreOne = 0
    scoreTwo = 0
    playerOne = input("Spelare 1: ")
    playerTwo = input("Spelare 2: ")


    while (turnCount <= 12):

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
            turncount += 1            
            turn -= 1

            scoreTwo += sumTot(dices)
            print(playerTwo + " poäng : " + str(scoreTwo))


def roll ():    
    
    dices=[random.randint(1, 6) for _ in range(6)]
    return dices

def winner ():
    if (scoreOne > scoreTwo):
        print("Spelare 1 vann med : " + scoreOne())
    if (scoreTwo > scoreOne):
        print("Spelare 2 vann med : " + scoreTwo()) 
    else:
        print("Oavgjort")



def sumTot (dices):
    sum = 0
    turncount = 1
    single = 1

    

    if (turncount <= 12):
        sum += SumOfSingle(dices, single)
    
   # for x in dices:
   #     sum += x
    return sum
    turncount += 1
    
def SumOfSingle(dices, single):
    return sum([x for x in dices if x == single])

if __name__ == "__main__": main()

