  #? Write a program to print multiplication table of a given number using for loop

n = int(input("Enter number: "))
print(f"Multiplication Table of {n} using for loop")
for i in range(1,11):
  print(f"{n} x {i} = {n*i}")

print(f"Multiplication Table of {n} using while loop")
i = 1
while i <= 10:
  print(f"{n} x {i} = {n*i}")
  i += 1