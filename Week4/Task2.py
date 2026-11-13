balance=50000
choice=0
print("Welcome to the ATM")
while True:
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")
    print("Please selesct an option:")
    choice=int(input())

    if choice==1:
        print("Apka balance yay hai:",balance)
    elif choice==2:
        amount=int(input("Enter an amount"))
        if amount>balance:
            print("Ghareeb")
        else:
            balance-=amount
            print("Remaining Balance:",balance)
    elif choice==3:
        amount=int(input("Enter an mount to deposit:"))
        balance+=amount
        print("New balance:",balance)
    elif choice==4:
        print("Dafa hojao")
        exit()