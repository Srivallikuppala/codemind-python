n=int(input())
s=0
m=1
while n!=0:
    d=n%10
    s+=d
    m=m*d
    n=n//10
if s==m:
    print("Spy Number")
else:
    print("Not Spy Number")