n=int(input())
a=0
b=1
c=a+b
t=0
while n>t:
    print(a,end=" ")
    a=b
    b=c
    c=a+b
    t+=1
