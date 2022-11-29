n=int(input())
s=0
m=1
while n!=0:
    d=n%10
    m=m*d
    s+=d
    n=n//10
print(m-s)    