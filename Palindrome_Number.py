def pal(n):
    r=0
    re=0
    m=n
    while n!=0:
        r=n%10
        re=(re*10)+r
        n=n//10
    if m==re:
        return True
    else:
        return False
for i in range(int(input())):
    x=int(input())
    if pal(x):
        print("True")
    else:
        print("False")