n=int(input())
a=list(map(int,input().split()))
x=0
for i in a:
    if i!=0 and i!=1:
        x=1
        break
if x==1:
    print("False")
else:
    print("True")