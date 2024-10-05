  #? Write a program to print the following star pattern.
  # *
  # **
  # *** for n = 3

# n = 3
# for i in range(1,n+1):
#   print("*"*i)


  #? Write a program to print the following star pattern.
  # ***** for n = 3
  #  ***
  #   *

# n = 3
# for i in  range(1,n+1):
#   print(" "*(n - i),end="")
#   print("*"*(2*i-1))

  #? Write a program to print the following star pattern.
  # ***** for n = 3
  #  ***
  #   *

# n = 3
# for i in range(n,0,-1):
#   print(" "*(n-i),end="")
#   print("*"*(2*i-1))


  #? Write a program to print the following star pattern.
  # * * * 
  # *   *   forn = 3
  # * * * 

# n = 3
# for i in range(1, n + 1):
#   if i == 1 or i == n:
#     print("* "*n)
#   else:
#     print("*",end="")
#     print(" "*(2*n-3),end="")
#     print("*")