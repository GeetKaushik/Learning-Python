# Typecasting

a = 1
b = "1"
c = int(b) # valid string is typecasted to number
d = float(b) # valid string is typecasted to flaot
e = float(a) # valid number is typecasted to flaot
#and so on if conversion is valid...

print(type(b))
print(type(c))
print(type(d))
print(type(e))