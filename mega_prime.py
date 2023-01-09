import math
n=int(input())
sq=int(math.sqrt(n))
count=0
for i in range(2,sq):
    if(n%i==0):
        count=count+1
        break
if(count!=0):
    print("Not Mega Prime")
else:
    temp=n
    k=0
    while temp>0:
        d=temp%10
        if(d==2 or d==3 or d==5 or d==7):
            d=d
        else:
            print("Not Mega Prime")
            k=1
            break
        temp=temp//10
    if(k!=1):
        print("Mega Prime")