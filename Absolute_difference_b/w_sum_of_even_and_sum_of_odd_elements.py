n=int(input())
a=list(map(int,input().split()))
e=o=0
for i in range(0,n):
    if a[i]%2==0:
        e+=a[i]
    else:
        o+=a[i]
if e>o:
    print(e-o)
else:
    print(o-e)