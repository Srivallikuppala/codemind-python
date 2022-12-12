n=int(input())
a=list(map(int,input().split()))
e=[]
o=[]
for i in a:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
for k in o:
    print(k,end=' ')
for j in e:
    print(j,end=' ')