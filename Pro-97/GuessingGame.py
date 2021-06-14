import random 
randomNo = random.randint(1,9)
print(randomNo)
chances = 5
print("Welcome to the Number Guessing game!")
while chances>0 :
    number = input("Enter a number between 1 and 9:- ")
    if(number == randomNo):
        print("Congats!!! You won the Game.")
        chances = 0
    else:
        #if (number > randomNo):
        if(chances <= 5):
            print("Wrong Answer.Try once again")
            chances-=1
            if (chances==0):
                print("You Lost. Your all the chances have been used up. Sorry! Better luck next time")
