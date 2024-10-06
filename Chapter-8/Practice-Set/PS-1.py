  #? Write a program using functions to find greatest of three numbers

def greatestOfThree(a,b,c):
  if a >= b and a >= c: print(f"{a} is greatest")
  elif b >= a and b >= c: print(f"{b} is greatest")
  elif c >= a and c >= b: print(f"{c} is greatest")
  else : print("None of them is greatest")

greatestOfThree(1,2,3)
greatestOfThree(1,22,3)
greatestOfThree(111,22,3)