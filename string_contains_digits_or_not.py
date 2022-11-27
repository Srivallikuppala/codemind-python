n=int(input())
f=0
for i in range(n):
    f=0
    x=input()
    x=list(x)
    for j in x:
        if j.isdigit():
            
            f=1
            break
    if f==1:
        print('Yes')
    else:
        print('No')