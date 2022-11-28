h,s,sp=map(int,input().split())
if h>50 and s>60 and sp>100:
    g=10
elif h>50 and s>60 and sp<=100:
    g=9
elif h<=50 and s>60 and sp>100:
    g=8
elif h>50 and s<=60 and sp>100:
    g=7
elif h>50 or s>60 or sp>100:
    g=6
else:
    g=5
print(g)