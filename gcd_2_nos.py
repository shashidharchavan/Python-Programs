from re import I


n1=int(input("Enter 1st no:"))
n2=int(input("ENter 2nd no:"))
res=n1*n2

if n1>n2:
    max=n1
else:
    max=n2

while(True):
    if max%n1==0 and max%n2==0:
        lcm=max
        break
    max+=1

print(f"LCM={lcm}")
print(f"GCD={res/lcm}")