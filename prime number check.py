n=int(input("enter a number:"))
c=0
if n<2:
    print("not a prime")
else:
    for i in range(1,n+1):
        if n%i == 0:
            c=c+1
    if c==2:
        print("prime number")
    else:
        print("not a prime number")
            
