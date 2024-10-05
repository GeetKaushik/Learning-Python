  #? Write a program to print multiplication table of n using for loops in reversed order.

n = int(input("Enter number: "))
print(f"Multiplication Table of {n} using for loop")
for i in range(10,0,-1):
  print(f"{n} x {i} = {n*i}")