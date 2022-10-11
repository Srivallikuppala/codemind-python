n=int(input())

a=0
b=1
c=a+b
p=0
while n>=a:
    if n==a:
        p=1
        break
  
    a=b
    b=c
    c=a+b
if p==1:
    print("True")
else:
    print("False")