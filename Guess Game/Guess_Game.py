import random

point=0
count=0
print("****The Guessing Game*****")

def positive(num):
    if(num<0):
        return -num
    else:
        return num
        
def cho1():
    choice=input("Do you want to Play Again: ")
    if(choice=='y' or choice=='n'):
        return choice
    else:
        print("Invalid Input")
        return cho1()
        
def cho():
    choice=input("Do You want to Start the Game:")
    if(choice=='n' or choice=='y'):
        return choice
    else:
        print("Invalid Input!! Try Again")
        return cho()
    
print("\n\nEnter 'y' for YES\nEnter 'n' for No\n\n")
choi=cho()

while(choi=='y'):
    count=count+1
    rand=random.randint(0,50)
    a=int(input("\nEnter your Guess:"))
    diff=positive(a-rand)
    if(diff==0):
        print("**The  Guess is Correct**")
        point=point+50
        print("Your Current Score: "+str(point))
    elif(diff<=10):
        print("The Number was: "+str(rand))
        print("You were Little Far!!")
        print("Your Point is Incremented by 10 points")
        point=point+10
        print("Current Score: "+str(point))
    elif(diff<=5):
        print("The Number was: "+str(rand))
        print("You Guessed it Almost Correct")
        print("Your Point is Incremented by 25 points")
        point=point+25
    else:
        print("The Number was: "+str(rand))
        print("You were so Far!!")
        print("No Increment in Your Points")
        print("Better Luck Next time")
    choi=cho1()
        
print("\nYou Played "+str(count)+" times")
print("\n\nYour Final Score: "+str(point))
