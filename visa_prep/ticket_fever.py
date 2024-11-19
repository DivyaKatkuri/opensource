n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    res=a-b
    print(max(res,0))
