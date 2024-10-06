  #? Write a python function to print first n lines of the following pattern:
  # ***
  # **
  # *   for n = 3

def triangle1(n):
  if n == 0 : 
    return
  print("*"*n)
  triangle1(n-1)

triangle1(3)

'''
t(3) return
*** and t(2) return
**  and t(1) return
*   and t(0) return
return
'''