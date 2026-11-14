n=int(input("Enter a number: "))
if n<0:
    print("Invalid input! Please enter a positive number.") 
else:
    a=0
    b=1
    sum=0
    even_count=0
    odd_count=0

    print("Fibonacci sequence:", end=" ")

    for i in range(n):
        if i==0:
            term=0
        elif i==1:
            term=1
        else:
            term=a+b
            a=b
            b=term

        print(term, end=" ")

        if term%2==0: 
            even_count+=1
        else:
            odd_count+=1

print("\nEven Numbers: ",even_count)
print("Odd Numbers: ",odd_count)