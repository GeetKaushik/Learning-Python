  #? Write a program to calculate the factorial of a given number using for loop

n = int(input("Enter a number: "))
f = 1
if n == 1 or n == 0: print(f"Factorial of {n} is 1")
elif n < 0: print(f"Factorial of {n} is undefined")
else:
  for i in range(1,n+1):
    f *= i
  print(f"Factorial of {n} is {f}")