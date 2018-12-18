
dices = [0,0,0,0,0]

scoreOne = 0
scoretwo = 0

import random

def main ():
    while (True):
        input("Please enter your name: ")
        lista = [0,1,2,3]
        #for x in lista:
            #print (x)
        lista = "Hej"
        #print (lista)  

        print(roll())

def roll ():    
    
    dices=[random.randint(1, 6) for _ in range(6)]
    return dices

def winner ():
    print ("Not Defined")

def sum ():
    print ("Not Defined")



if __name__ == "__main__": main()

