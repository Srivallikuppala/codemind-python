p,r,t=map(int,input().split())
x=p*pow(1+r/100.,t)
print(format(x,".2f"))