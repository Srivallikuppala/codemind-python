n=input()
count=0
for i in n:
    if(ord(i)>=48 and ord(i)<=57):
        count=count+(ord(i)-48)
print(count)