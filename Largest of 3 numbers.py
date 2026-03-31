a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))
if a >= b and a >= c :
    print("largest:", a)
elif b >= a and b >= c:
    print("largest:", b)
else:
    print("largest:", c)
