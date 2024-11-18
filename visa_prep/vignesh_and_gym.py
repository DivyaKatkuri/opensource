x,y,z=map(int,input().split())
cost=x+y
if cost<=1:
    prinr(1)
elif cost<=z:
    print(2)
elif x<=z:
    print(1)
else:
    print(0)
