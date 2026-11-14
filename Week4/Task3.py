sum=0
fnum=int(input("Enter the first number: "))
lnum=int(input("Enter the last number:"))
for i in range(fnum, lnum+1):
    if i<2:
        continue

    prime=True
    for num in range (2,i):
        if i%num==0:
            prime=False
            break

    if prime:
        print(i,"is a prime number")
        sum+=i
print("The sum of prime numbers between", fnum, "and", lnum, "is:", sum)