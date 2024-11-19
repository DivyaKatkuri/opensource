a,b,c=map(int,input().split())
tot=a*b
time=c*24*60
if tot<=time:
    print("YES")
else:
    print("NO")
