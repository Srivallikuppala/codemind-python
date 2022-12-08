n=int(input())
a=list(map(int,input().split()))
c=0
r=[]
for i in range(n):
    if a[i]%2==0:
        r.append(a[i])
for i in range(n):
    if a[i]%2!=0:
        r.append(a[i])
for i in range(n):
    print(r[i],end=' ')