def d(n):
    r=0
    d=0
    while n!=0:
        r=n%10
        d=d+r
        n=n//10
    return d
n=int(input())
while n>9:
    n=d(n)
if n<=9:
    print(n)