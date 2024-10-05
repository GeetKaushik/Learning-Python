  #? Write a program to find the greatest of 4 numbers entered by the user

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

if(a>=b and a>=c and a>=d): print(a,"is Greatest")
elif(b>=a and b>=c and b>=d): print(b,"is Greatest")
elif(c>=a and c>=b and c>=d): print(c,"is Greatest")
elif(d>=a and d>=b and d>=c): print(d,"is Greatest")
