  #? Write a recursive function to calculate the sum of first n natural numbers

def rSum(n):
  if n <= 1: return 1
  return rSum(n-1) + n

print(rSum(3))
print(rSum(5))
