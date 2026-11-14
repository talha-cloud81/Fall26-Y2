stock=100
sold=0

while stock>0:
    print("Current stock:", stock)
    sale=int(input("Enter the number of items sold: "))
    if sale==-1:
        break
    if sale>stock:
        print("Not enough stock available!")
        continue
    if sale<0:
        print("Invalid input! Please enter a positive number.")
        continue
    if sale<=stock:
        stock-=sale
        sold+=sale
print("Total items sold:", sold)
print("Remaining stock:", stock)