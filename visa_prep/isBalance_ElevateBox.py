n=int(input())
a=list(map(int, input().split()))
b=[abs(sum(a[:i])-sum(a[i+1:])) for i in range(n)]
print(" ".join(map(str,b)))
