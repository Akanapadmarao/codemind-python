n=int(input())
a,b,c=0,1,0
while c<n:
    c=a+b
    a=b
    b=c
if n==c:
    print("True")
else:
    print("False")