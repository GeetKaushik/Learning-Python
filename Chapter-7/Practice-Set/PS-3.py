  #? Write a program to find whether a given number is prime or not.

n = int(input("Enter a number: "))

if n <= 1:
  print(f"{n} is not a prime number")
else:
  for i in range(2, int(n**0.5) + 1):  # Start from 2 and go up to the square root of n
    if n % i == 0: 
      print(f"{n} is not a prime number")
      break
  else:
    print(f"{n} is a prime number")