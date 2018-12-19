
dices = [0,0,0,0,0]

import random

def main ():
    turncount = 1
    t = 1
    scoreOne = 0
    scoreTwo = 0
    playerOne = input("Spelare 1: ")
    playerTwo = input("Spelare 2: ")

    while (turncount <= 6):
        if (t == 1):
            dices = roll()
            print(dices)            

            scoreOne += sumTot(dices)
            print(playerOne + " poäng : " + str(scoreOne))

        elif (t == 2):
            dices = roll()
            print(dices)
            turncount += 1            

            scoreTwo += sumTot(dices)
            print(playerTwo + " poäng : " + str(scoreTwo))

        t = turn(t)
def roll ():    
    
    dices=[random.randint(1, 6) for _ in range(6)]
    return dices

def turn (t):
    if (t == 2):
        return  1
        
    elif (t == 1):
        return 2        

def winner ():
    if (scoreOne > scoreTwo):
        print("Spelare 1 vann med : " + scoreOne())
    if (scoreTwo > scoreOne):
        print("Spelare 2 vann med : " + scoreTwo()) 
    else:
        print("Oavgjort")

def single ():
    t = 1
    single = 1
    if turn(t) == 2:
        single + 1
    return single

def sumTot (dices):
    sum = 0
    turncount = 1

    if (turncount <= 12):
        sum += SumOfSingle(dices, single)
    return sum
    turncount += 1
    
def SumOfSingle(dices, single):
    return sum([x for x in dices if x == single])

if __name__ == "__main__": main()

