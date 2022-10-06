n = int(input())  
num= len(str(n))  
square = n**2  
last_digits = square%pow(10,num)  
if last_digits == n:  
  print("Automorphic Number")  
else:  
  print("Not an Automorphic Number")  