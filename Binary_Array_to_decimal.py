n=int(input())
a=list(map(int,input().split()))
x=0
for i in a:
    if i==1:
        x=x+int(pow(2,n-1))
    n-=1
print(x)