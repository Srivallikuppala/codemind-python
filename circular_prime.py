def rev(n):
    r=0
    re=0
    m=n
    while n!=0:
        r=n%10
        re=(re*10)+r
        n=n//10
    return re

def pr(n):
    if n==1 :
        return False
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
if pr(n):
    x=rev(n)
    if pr(x):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")