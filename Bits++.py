c=0
for i in range(int(input())):
    x=input()
    if x.count('+')>=1:
        c+=1
    else:
        c-=1
print(c)    