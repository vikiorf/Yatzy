
dices = [0,0,0,0,0]

scoreOne = 0
scoretwo = 0

def main ():
   ## while (true):
   #     input("please enter your name: ")
   #     lista = [0,1,2,3]
   #     for x in lista:
   #         print (x)
   #     lista = "hej"
   #     print (lista)
    print("Hejsan")

def roll ():
    print ("Not Defined")



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

