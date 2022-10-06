import math
n=int(input())
a= math.pow(n, 2)
s=0
while a:
    d=a%10
    s=s+d
    a=a//10
if(s==n):
    print("Neon Number")
else:
    print("Not Neon Number")