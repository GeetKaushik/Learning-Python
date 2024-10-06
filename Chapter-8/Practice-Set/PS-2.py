  #? Write a python program using function to convert Celsius to Fahrenheit and vice versa

DIG = "\u00B0"
def cToF(c):
  f = ((9/5)*c) + 32
  return round(f,2)
def fToC(f):
  c = ((f - 32)*5)/9
  return round(c,2)

print(f"{fToC(80)}{DIG}C")
print(f"{cToF(26.67)}{DIG}F")

print(f"{fToC(90)}{DIG}C")
print(f"{cToF(32.22)}{DIG}F")

print(f"{fToC(100)}{DIG}C")
print(f"{cToF(37.78)}{DIG}F")