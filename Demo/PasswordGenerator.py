import random
import string

def randomPassword(charCount, numCount):
    SpecialSym = ['$', '@', '#', '%']
    passi = ''.join((random.choice(string.ascii_letters) for i in range(charCount)))
    passi += ''.join((random.choice(string.digits) for i in range(numCount)))
    passi += ''.join((random.choice(SpecialSym)))

    passi += ''.join((random.choice(string.ascii_uppercase) for i in range(length-len(passi))))
    passi += ''.join((random.choice(string.ascii_lowercase) for i in range(length - len(passi))))


    sample = list(passi)
    random.shuffle(sample)
    finalString = ''.join(sample)

    return finalString

print("Please specify the your password length you want")
length= int(input())

if length < 6:
    print("Password should be a minimum of 6 characters long!")
else:
    print("Please enter how many char password should contain")
    chari = int(input())
    print("Please enter how many number password should contain ")
    numi= int(input())

    password = randomPassword(chari,numi)
    print("The Random password is:" +password)

