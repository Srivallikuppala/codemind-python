def prm(n):
    if n==1:
        return False
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True
n=int(input())
c=0
if prm(n)==True:
    while n!=0:
        d=n%10
        if prm(d)==False:
            c=1
            break
        n=n//10
else:
    c=1
if c==0:
    print("Mega Prime")
else:
     print("Not Mega Prime")