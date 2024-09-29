
#? Can we have a set with 18 (int) and ' 18' (str) as a value in it?

s1 = {18,'18'}
print(s1)

#* Answer: Yes, Because in Set 18(int) and '18'(str) are treated as two different entities

#? Can we have a set with 20 (int), 20.0 (float) and '20' (str) as a value in it?
s2 = {20,20.0,'20'}
print(s2)

#* Answer: No, Because in Python sees 20(int) and 20.0(float) as equal and does keeps the one coming first in the set


#? What is the type of s3 = {} here?
s3 = {}
print(type(s3))

#* Answer: Dictionary