print("Electricity Bill Calculator!")
bill=0
units=0
customer=1
total=0
while True:
    units=int(input("Enter the number of units consumed or -1 to exit: "))
    if units==-1:
        break
    if units<0:
        print("Invalid input")
        continue
    elif units==0:
        print("You have not consumed any units")
    elif units<=100:
        bill=units*10
    elif units<=200:
        bill=(100*10)+((units-100)*15)
    elif units<=300:
        bill=(100*10)+(100*15)+((units-200)*20)
    else:
        bill=(100*10)+(100*15)+(100*20)+((units-300)*25)
    print("Your electricity bill is: ",bill)
    customer+=1
    total+=bill

print("Total customers served: ",customer-1)
print("Total Revenue: ",total)