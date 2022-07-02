n=int(input("Enter a num:"))
l=len(str(n))
sum=0
temp=n

while(n!=0):
    rem=n%10
    sum=sum+rem**l
    n=n//10

if(temp==sum):
    print("Armstrong")
else:
    print("NA")