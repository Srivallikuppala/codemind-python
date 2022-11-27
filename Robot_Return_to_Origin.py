n=input()
n=list(n)
c=0
for i in n:
    if i=='R' or i=='U':
        c+=1
    elif i=='L' or i=='D':
        c-=1
if c==0:
    print('True')
else:
    print('False')