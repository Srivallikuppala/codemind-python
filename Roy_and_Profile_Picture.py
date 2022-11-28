l=int(input())
n=int(input())
#print(l)
for i in range(n):
    w,h=map(int,input().split())
  #  print(w,h)
    if w<l or h<l:
        print("UPLOAD ANOTHER")
    elif w==h:
        print("ACCEPTED")
    elif w>l or h>l:
        print("CROP IT")
