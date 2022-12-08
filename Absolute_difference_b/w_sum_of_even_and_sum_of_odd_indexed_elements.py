n=int(input())
a=list(map(int,input().split()))
e=0
o=0
#print(a)
for i in range(0,n):
    if i%2==0:
        e+=a[i]
    else:
        o+=a[i]
if e>=o:
    print(e-o)
else:
    print(o-e)