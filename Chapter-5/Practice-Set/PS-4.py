
#? Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique

dc = {}

dc.update({input("Name: ") : input("Language: ")})
dc.update({input("Name: ") : input("Language: ")})
dc.update({input("Name: ") : input("Language: ")})
dc.update({input("Name: ") : input("Language: ")})

print(dc)
print(type(dc))


