n=int(input())
t=n
a=0
for i in range (1,n):
    if n%i==0:
      a=a+i  
if a>t:
    print("True")
else:
    print("False")
    