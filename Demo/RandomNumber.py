import random as ran


def findRandom(rnd):
    print("Please guess the any number between 0 to 20 which you thought Device Generate:")
    userran = int(input())


    if (userran < rnd):
        print("Your number is smaller than Device generated Number. Please try again!")
        findRandom(rnd)
    elif (userran > rnd):
        print("our number is greater than Device generated Number. Please try again!")
        findRandom(rnd)
    else:
        print("You find the correct answer:" +str(rnd))





print(" A Random Number generated by Device: ")
rnd = ran.randint(0,20)

print (rnd)
findRandom(rnd)



