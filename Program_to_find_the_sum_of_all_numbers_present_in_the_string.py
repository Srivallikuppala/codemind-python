n=input()
sum=''
k=0 
for i in n:
    if ord(i)>47 and ord(i)<58:
        sum=sum+i
s=int(sum)
while s>0:
    d=s%10
    k=k+d
    s=s//10
print(k)