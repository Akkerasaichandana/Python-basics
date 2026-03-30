n=int(input("enter a number:"))
rev=0
temp = n
while (n>0):
    rev = rev*10+n%10
    n = n//10
if temp == rev:
    print("palindraome")
else:
    print("not a palindrome")
