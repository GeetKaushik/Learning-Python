a = (1,2,3,4,5,1,1,1,1)
# a[0] = 0 #this will give error
print(a)
print(type(a))

print(a.count(1)) # Return number of occurrences of value.

b = [0,1,2,3,4,5]
c = tuple(b)
print(type(b))
print(type(c))

d = [1]*10
d = (0,)*10
print(d)

#Unpacking
e = (1,2,3)
a1,a2,a3 = e
print(a3)