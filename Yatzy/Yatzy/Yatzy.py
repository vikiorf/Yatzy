
dices = [0,0,0,0,0]

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
            
    dices = roll()
    print(dices)    
    print(sumTot(dices))

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

