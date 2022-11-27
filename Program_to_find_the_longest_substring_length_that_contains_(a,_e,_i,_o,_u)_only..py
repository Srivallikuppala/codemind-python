n=input()
m=list(n)
c=0
max=0
for i in m:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        c+=1
        if max<=c:
            max=c
    else:
        c=0
print(max)