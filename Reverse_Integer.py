def rev(n):
    r=0
    m=n
    re=0
    while(n!=0):
        r=n%10
        n=n//10
        re=(re*10)+r
    return re
n=int(input())
if(n>=0):
    print(rev(n))
else:
    n=(-1)*n
    x=rev(n)
    x=(-1)*x
    print(x)