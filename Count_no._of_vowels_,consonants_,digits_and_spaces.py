n=input()
x=list(n)
v=c=d=s=0
for i in n:
    if i.isalpha():
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            v+=1
        else:
            c+=1
    elif i.isdigit():
        d+=1
    elif i==' ':
        s+=1
print('Vowels:',v)
print('Consonants:',c)
print('Digits:',d)
print('White spaces:',s)