def facto(n):
  if n == 0 or n == 1: return 1 #base case
  return n*facto(n-1) #recursive call

print(facto(5))
print(facto(6))
# print(facto(998)) #* just a finding max recursively deep call can go
# print(facto(999)) #! just a finding it will throw a error
