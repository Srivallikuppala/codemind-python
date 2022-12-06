def rev(n):
    r=0
    re=0
    m=n
    while n!=0:
        r=n%10
        n=n//10
        re=(re*10)+r
    return re
def pr(n):
    for i in range(2,n//2+1):
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