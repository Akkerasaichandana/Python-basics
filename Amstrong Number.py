n = int(input("enter a number:"))
temp = n
summ = 0
while n>0:
    digit = n%10
    summ = summ+digit*digit*digit
    n=n//10
if temp == summ:
    print("Amstrong Number")
else:
    print("Not a Amstrong Number")

    
    
