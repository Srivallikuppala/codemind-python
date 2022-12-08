def pr(n):
    if n==1:
        return False
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
#print(n)
if pr(n)==False:
    c=1
else:
    while n!=0:
        c=0
        d=n%10
        if pr(d)==False:
            c=1
            break
        n=n//10
if c==1:
    print("Not Mega Prime")
else:
    print("Mega Prime")