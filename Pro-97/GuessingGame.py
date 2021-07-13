import random 
randomNo = random.randint(1,9)
#print(randomNo)
chances = 4
print("Welcome to the Number Guessing game!")
while chances<=4 :
    number = int(input("Enter a number between 1 and 9:- "))
    if(number == randomNo):
        print("Congats!!! You won the Game.")
        break
    else:
        if(chances <= 4 and chances>=1):
            print("Wrong Answer.Try once again")
        elif (chances<=0):
            print("You Lost. Your all the chances have been used up. Sorry! Better luck next time")
            print("Your actual no. was" , randomNo)
            break
        chances-=1
