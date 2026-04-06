n=int(input("enter a number:"))
summ=0
for i in range(1,n):
    if n%i==0:
        summ=summ+i
if summ==n:
    print("perfect number")
else:
    print("not a perfect number")
