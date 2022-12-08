n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
c=0
for i in range(n):
    if x<=a[i] and y>=a[i]:
        continue
    else:
        c+=a[i]
print(c)