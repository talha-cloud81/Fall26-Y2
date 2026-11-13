passed=0
failed=0
highest=0
total=0
for i in range(1,11):
    mark=int (input("Enter a number: "))
    while mark<0 or mark>100:
        print("Invalid mark")
        mark=int (input("Enter a number: "))
    if mark>=90 and mark<100:
        print("Grade A")
    elif mark>=80 and mark<90:
        print("Grade B")
    elif mark>=70 and mark<80:
        print("Grade C")
    elif mark>=60 and mark<70:
        print("Grade D")
    else:
        print("Grade F")

    if mark>=50 and mark<=100:
        passed+=1
    else:
        failed+=1

    if mark>highest:
        highest=mark

    total+=mark
    average=float(total/10)

print("Number of students passed: ",passed)
print("Number of students failed: ",failed)
print("Highest mark: ",highest)
print("Average mark: ",average)