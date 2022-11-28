n=int(input())
a=0
b=1
c=a+b
for i in range(n):
    print(a,end=' ')
    a=b
    b=c
    c=a+b
