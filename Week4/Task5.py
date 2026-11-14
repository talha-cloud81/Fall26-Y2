import random
secret=random.randint(1,100)
attempts=0
guess=0
print("Number Guessing Game")
for i in range(7):
    guess=int(input("Guess the number between 1 and 100:"))
    if guess==secret:
        print("You guessed the number correctly!")
        break
    elif guess!=secret:
        print("You guessed the number wrong")
        if guess<secret:
            print("The secret number is higher than ",guess)
            attempts+=1
            print("You have ",7-attempts, "attempts left.")
        elif guess>secret:
            print("The secret number is lower than ",guess)
            attempts+=1
            print("You have ",7-attempts, "attempts left.")
            if attempts==7:
                print("You have used all your attempts")
                print("You did not guess the number correctly. The number was ",secret)