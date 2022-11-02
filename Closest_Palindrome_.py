def pa(n):
    c=0
    r=0
    m=n
    while n>=1:
        c=n%10
        r=(r*10)+c
        n=n//10
    if r==m:
        return True
    else:
        return False
n=int(input())
ma=0
mi=0
for i in range(1,n,1):
    if pa(i)==True:
        ma=i
for i in range(n+1,n*n,1):
    if pa(i)==True:
        mi=i
        break
#print(n,ma,mi)
if n-ma>mi-n:
    print(mi)
elif n-ma<mi-n:
    print(ma)
else:
    print(ma,mi)
