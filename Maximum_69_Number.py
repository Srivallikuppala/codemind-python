def re(n):
    r=0
    while n:
        x=n%10
        r=(r*10)+x
        n=n//10
    return r

n=int(input())
m=re(n)
#print(m)
r1=0
c=0
while m:
    x1=m%10
    if x1==6 and c==0:
        x1=9
        c=1
    
    r1=(r1*10)+x1
    m=m//10
print(r1)