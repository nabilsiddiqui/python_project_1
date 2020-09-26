# This tells about what type of calculator is this .

print("This is a scientifc calculator")

# A and B are the variables that defines the numbers entered by the user
# C is the operation that the user will select
# Since python recognizes everything as string so we have to convert the numbers into integer

c = int(input("Choose an operation: \n1.Addition \n2.Substraction \n3.Multiplication \n4.Division \n"))

if c == 1 or c == 2 or c == 3 or c == 4:
    a = int(input("Enter the number: "))
    b = int(input("Enter another number: "))

if c == 1:
    print(a+b)
elif c == 2: 
    print(a-b)
elif c == 3: 
    print(a*b)
elif  c == 4: 
    print(a/b)
else:
    print("Wrong input! Try again.")

print("\n~Let's add more than two numbers\n")
d = int(input("Enter another number: "))
if c == 1:
    print(a+b+d)
elif c == 2:
    print(a-b-d)
elif c == 3:
    print(a*b*d)
elif  c == 4:
    print(a/b/d)


