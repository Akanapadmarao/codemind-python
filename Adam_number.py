n=input()
n1=int(n)**2
a=n[::-1]
a1=int(a)**2
a2=str(a1)
a3=a2[::-1]
a4=int(a3)
if n1==a4:
    print("True")
else:
    print("False")
