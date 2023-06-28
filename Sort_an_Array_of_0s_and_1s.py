n=int(input())
ar=list(map(int,input().split()))
r=[]
for i in ar:
    if i==0:
        r.append(i)
x=len(ar)-len(r)
while x:
    r.append(1)
    x-=1
print(*r)
        