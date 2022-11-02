def pa(n):
    c=0
    r=0
    m=n
    while n>=1:
        c=n%10
        r=(r*10)+c
        n=n//10
    return r
n=int(input())
x=n*n
n=pa(n)
n=n*n
if x==pa(n):
    print("True")
else:
    print("False")