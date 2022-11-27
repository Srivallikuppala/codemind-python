n=int(input())
for i in range(n):
    f=0
    l=int(input())
    s=input()
    x=list(s)
    for i in x:
        if x.count(i)==1:
            f=1
            print(i)
            break
    if f==0:
        print('-1')