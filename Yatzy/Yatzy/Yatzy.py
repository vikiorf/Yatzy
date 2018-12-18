
dices = [0,0,0,0,0]

scoreOne = 0
scoretwo = 0
playerOne = ""
playerTwo = ""


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
    
        #lista = [0,1,2,3]
        #for x in lista:
            #print (x)
        #lista = "Hej"
        #print (lista)

def roll ():    
    
    dices=[random.randint(1, 6) for _ in range(6)]
    return dices

def winner ():
    if (scoreOne > scoretwo):
        print("Spelare 1 vann med : " + p1sum())
    if (scoretwo > scoreOne):
        print("Spelare 2 vann med : " + p2Sum()) 
    else:
        print("Oavgjort")

def sum ():
    if (turn == playerOneT):
        for x in savedDice:
            score += savedDice
    if (turn == playerTwoT):
        for x in savedDice:
            score += savedDice  

if __name__ == "__main__": main()

