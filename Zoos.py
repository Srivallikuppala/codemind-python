n=input()
c1=0
c2=0
for i in n:
    if(ord(i)==122):
        c1=c1+1
    elif(ord(i)==111):
        c2=c2+1
if(c2==c1*2):
    print("Yes")
else:
    print("No")