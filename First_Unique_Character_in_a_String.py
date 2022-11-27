n=input()
m=list(n)
c=0
f=0
for i in range(0,len(m)):
    c=0
    for j in range(0,len(m)):
        if m[i]==m[j]:
            c+=1
    if c==1:
        f=1
        r=i
        break
if f==1:
    print(i)
else:
    print('-1')