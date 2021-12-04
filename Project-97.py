import random
print("Number Guessing Game")
number=random.randint(1,9)
chances=0
numberOfChancesLeft=5
print("Guess A Number (Between 1 and 9) , You Have 5 Chances")
while chances<5:
    guess=int(input('Enter Your Guess '))
    chances+=1
    numberOfChancesLeft-=1
    if guess==number:
        print("Congratulation , You Won With",numberOfChancesLeft,"Chances Left")
        break
    elif guess<number:
        print("Your Guess Was Too Low: Guess A Higher Number Than",guess,", You Have Chances",numberOfChancesLeft,"Left")
    else :
        print("Your Guess Was Too High: Guess A Lower Number Than",guess,", You Have Chances",numberOfChancesLeft,"Left")
if chances==5 and not guess==number:
    print("You Lose The Number Is:",number)