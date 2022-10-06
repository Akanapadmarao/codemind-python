num=int(input())
sum=0
product=1
while num:
    d=num%10
    sum=sum+d
    product=product*d
    num=num//10
if(sum==product):
    print("Spy Number")
else:
    print("Not Spy Number")