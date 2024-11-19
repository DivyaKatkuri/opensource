a,n=map(int,input().split())
cur=a*100
if cur>=n:
    print(0)
else:
    rem=n-cur
    new=(rem+99)//100
    print(new)
