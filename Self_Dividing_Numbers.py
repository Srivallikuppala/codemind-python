def s(n):
    m=n
    d=0
    f=0
    while n!=0:
        d=n%10
        if d==0 or m%d!=0:
            f=1
            break
        n=n//10
    if f==0:
        return True
    else:
        return
n=int(input())
m=int(input())
for i in range(n,m+1):
    if s(i):
        print(i,end=' ')
