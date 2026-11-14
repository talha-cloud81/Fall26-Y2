username="talha"
password="talha@675"
attempts=0
for i in range(3):
    user=input("Enter your username:")
    passw=input("Enter your Password:")
    if user==username and passw==password:
        print("Login Successful!")
        break
    else:
        attempts+=1
        print("Invalid! Username or password. Try Again")
        print("Attempts remaining:",3-attempts)
        if attempts==3:
            print("You have maximum number of failed attempts. Account locked!")