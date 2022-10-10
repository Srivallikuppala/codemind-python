def dig(n):
    d=0
    r=0
    while n>0:
        d=n%10
        n=n//10
        r=(d*d)+r
    return r    
n=int(input())
while n>=9:
    n=dig(n)

if n==1 or n==7:
    print("True")
else:
    print("False")