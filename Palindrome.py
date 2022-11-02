def pa(n):
    c=0
    m=n
    rev=0
    while n>=1:
       r=n%10
       rev=(rev*10)+r
       n=n//10
    if m==rev:
        print("True")
    else:
        print("False")
        
n=int(input())
x=pa(n)