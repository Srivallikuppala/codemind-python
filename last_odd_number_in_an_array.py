n=int(input())
a=list(map(int,input().split()))
f=0
for i in range(0,n):
    if a[i]%2!=0:
        f=a[i]
print(f)