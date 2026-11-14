even=0
odd=0
total=0
positive_count=0
largest=0
while True:
    num=int(input("Enter a number or 0 to stop: "))
    if num==0:
        break
    if num<0:
        continue
    if num>0:
        positive_count+=1
        if num%3==0:
            even+=1
        else:
            odd+=1
        total+=num
        if num>largest:
            largest=num
if positive_count==0:
    print("No positive numbers were entered.")
else:
    print("Total positive numbers: ",positive_count)
    print("Sum of positive numbers: ",total)
    print("Largest positive number: ",largest)
    print("Even numbers: "  ,even)
    print("Odd numbers: "  ,odd)