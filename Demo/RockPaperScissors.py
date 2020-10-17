import random as ran


def RockPaperScissor():

    print ("Please choose one of the: Rock, Paper , Scissor")
    userAction = input()

    userScore = 0
    deviceScore = 0
    while(userAction!=action):
        if(userAction=="Rock"):
            if(action=="Paper"):
                print ("Paper cover the Rock, You get 1 point")
                userScore += 1
                print(userScore, deviceScore)
                forcontinue(userScore,deviceScore)
            elif(action=="Scissor"):
                print("Rock destroy the Scissor, You get 1 point")
                userScore += 1
                print(userScore, deviceScore)
                forcontinue(userScore,deviceScore)

        elif(userAction=="Paper"):
            if (action == "Rock"):
                print("Paper cover the Rock, You get 1 point")
                userScore += 1
                print(userScore, deviceScore)
                forcontinue(userScore,deviceScore)
            elif (action == "Scissor"):
                print("Scissor cut the Paper, You loose!")
                deviceScore += 1
                print(userScore, deviceScore)
                forcontinue(userScore,deviceScore)

        else:
            if (action == "Paper"):
                print("Scissor cut the Paper, You loose")
                userScore += 1
                print(userScore, deviceScore)
                forcontinue(userScore,deviceScore)
            elif (action == "Rock"):
                print("Rock destroy the Scissor, You loose!")
                deviceScore += 1
                print (userScore , deviceScore)
                forcontinue(userScore,deviceScore)
    print ("Cancel.Try Again!")
    print(userScore, deviceScore)
    forcontinue(userScore,deviceScore)

def forcontinue(user,device):
    print("To continue...press Y")
    ans = input()
    if (ans == "Y"):
        RockPaperScissor()
    else:
        print("Game over!   Final Score: You Have:" + str(user) + " Device Have: " + str(device))
        print("Thank you for Playing")
        exit()



print ("Start")
print ("Device generated action: ")

list = ['Rock','Paper','Scissor']
action = ran.choice(list)
print (action)
RockPaperScissor()





