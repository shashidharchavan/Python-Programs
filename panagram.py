
s=input("Enter a str:")
a="abcdefghijklmnopqrstuvwxyz"

for i in a:
    if i in s.lower():
        res=True
    else:
        res=False
if(res):
    print("Panagram")
else:
    print("Not panagram")

