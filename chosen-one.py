import sys 
import math 


n=int(input())
p=[0]*(n+1)
s=[0]*(n+2)
a=[]
if n==1:
    print(int(input())+1)
    sys.exit()
a=list(map(int,input().split(" ")))
for i in range(n):
    p[i+1]=math.gcd(a[i],p[i])
for j in range(n,0,-1):
    s[j]=math.gcd(s[j+1],a[j-1])
for i in range(1,n+1):
    cur = math.gcd(p[i-1],s[i+1])
    if a[i-1] % cur != 0:
        print(cur)
        sys.exit()