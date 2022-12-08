n=int(input())
a=list(map(int,input().split()))
x=sum(a)//len(a)
f=0
for i in range(0,n):
    if a[i]==x:
        f=1
        break
if f==1:
    print("True")
else:
    print("False")