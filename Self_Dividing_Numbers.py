n=int(input())
m=int(input())
for i in range(n,m+1):
    k=i
    c=0
    d=0
    while k!=0:
        d=k%10
        k=k//10
        if d!=0 and i%d==0:
            c=0
        else:
            c=1
            break
    if c==0:
        print(i,end=' ')