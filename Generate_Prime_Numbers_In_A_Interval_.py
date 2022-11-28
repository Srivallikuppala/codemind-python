def prime(n):
    c=0
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            c=1
            break
    if c==0:
        return True
    else:
        return False
n=int(input())
m=int(input())
for i in range(n+1,m):
    if prime(i):
       print(i) 