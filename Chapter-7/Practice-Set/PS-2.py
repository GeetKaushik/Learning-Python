  #? Write a program to greet all the person names stored in a list I' and which starts with S.

l = ["Harry", "Soham", "Sachin", "Rahul"]
for i in l:
  if(i.lower().startswith("s")): print(f"Hello, {i}")
