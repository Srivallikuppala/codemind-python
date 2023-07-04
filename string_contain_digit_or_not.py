n=input()
c=0
k=0
for i in n:
    if(ord(i)>=48 and ord(i)<=57):
        c=c+1
        k=1
if(k==1):
    print("Contains",c,"digit")
else:
    print("Doesn't contain digit")