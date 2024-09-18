str1 = 'Hello1'
str2 = "World2"
str3 = '''HelGo3''' # For multiline String
str4 = """Hello4""" # For multiline String

# Slicing
lenOfStr1 = len(str1)
sl1 = str1[1:4] #This will return all characters in String form from 1 to 4 excluding 4
sl21 = str2[: 4] #This also works it will take 0 by default before colon. Thus 0 to 4
sl22 = str2[0:] #This also works it will take length of String here, 6 by default after colon. Thus 0 to 6
sl3 = str3[3] #This will return a character in String form at index 3
sl4 = str4[2:5]
negsl = str4[-4:-1] # Negative slicing works in similar way taking negtive index from last
'''
    H  e  l  l  o  4
  [ 0  1  2  3  4  5 ] # Positive indexing
  [-6 -5 -4 -3 -2 -1 ] # Negative indexing
'''
print(sl1)
print(sl21)
print(sl22)
print(type(sl3))
print(sl4)
print(negsl)

str5 = "0123456789"
sk = str5[1:9:2] #[origin : destination(excluded) : skip number]
print(sk)