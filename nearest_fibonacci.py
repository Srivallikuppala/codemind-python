def fib(n):
    a=0
    b=1
    c=a+b
    f=0
    t=0
    while t!=n:
        if a==n:
           f=1
           break
        a=b
        b=c
        c=a+b
        t+=1
    if f==1:
        return True
    else:
        return False

n=int(input())
np=0
pp=n+1
for i in range(n-1,0,-1):
    if fib(i):
        np=i
        break
while fib(pp)==False:
    pp+=1
if pp-n<n-np:
    print(pp)
elif pp-n>n-np:
    print(np)
else:
    print(np,pp)