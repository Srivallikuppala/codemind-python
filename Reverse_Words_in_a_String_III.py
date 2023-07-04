s=input()
str=s.split()
res=[]
for i in str:
    res.append(i[::-1])
print(*res)