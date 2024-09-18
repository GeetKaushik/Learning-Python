str1 = "Hello \\ \"'$'\" World"
str2 = "morning"

print(len(str1)) #length of string : returns Integer
print(str1.endswith("rld")) # Does string ends with the argument provided : returns Boolean
print(str1.startswith("He")) # Does string starts with the argument provided : returns Boolean
print(str1.startswith("he")) # Does string starts with the argument provided : returns Boolean : It is case sensitive
print(str2.capitalize()) # Capitalizes first character of string : returns String
print(str2.lower()) # lower cases all character : returns String
print(str2.upper()) # upper cases all character : returns String
print(str1.find("World")) # find first occurance of argument : returns Integer : Case Sensitive
print(str1.replace("World", "Python")) # Replaces all occurance of word with other word : returns String : Case Sensitive

# Escape sequence characters
'''
  \n : new line
  \t : tab
  \" : "
  \' : '
  \\ : \
  etc.
'''