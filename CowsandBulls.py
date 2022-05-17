import random
def getNum(num):
    return [int(i) for i in  str(num)]
def noRepeatingNum(num):
    randomNumbers= getNum(num)
    if len(randomNumbers) == len(set(randomNumbers)):
        return True
    else:
        return False

def generateNum():
    while True:
        num=random.randint(1000,9999)
        if noRepeatingNum(num):
            return num

def numOfBullCow(num,guess):
    bull_cow=[0,0]
    randomNumbers= getNum(num)
    userGuess= getNum(guess)

    for i,j in zip(randomNumbers,userGuess):
        if j in randomNumbers:
            if j==i:
                bull_cow[0]+=1
            else:
                bull_cow[1]+=1
    return bull_cow

testNum=0
num= generateNum()
tries= int(input("Please Enter Number of Attempts:"))

while tries >0 and testNum<tries:
    guess=int(input("Enter your guessed number:"))

    if not noRepeatingNum(guess):
        print("SHOULD NOT CONTAIN REPEAT NUMBERS. PLEASE TRY AGAIN.")
        continue
    if guess <1000 or guess >9999:
        print("ONLY 4 DIGIT NUMBERS ARE ACCEPTABLE. PLEASE TRY AGAIN.")
        continue
    bull_cow=numOfBullCow(num,guess)
    print(str(bull_cow[0]) + " bulls"+ " " + str(bull_cow[1]) + " cows.")
    

    if bull_cow[0]==4:
        print("Great!! You guessed right.")
        break

#Talls correct information that the numbers of their correct persons
#line numbers on the cows road

