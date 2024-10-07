
#* READ : "r" : (default mode)
# f = open("Chapter-9/File.txt")
# data = f.read()
# print(data)
# f.close()

# # This is safer and avoids forgetting to manually close the file.
# with open("Chapter-9/File.txt", 'r') as f:
#     content = f.read()
#     print(content)
# File is automatically closed after this block

# with open("Chapter-9/new2.txt") as f:
  # lines = f.readlines()
  # print(lines, type(lines))

  # l1 = f.readline()
  # print(l1,type(l1))
  
  # l2 = f.readline()
  # print(l2,type(l2))

  # l3 = f.readline()
  # print(l3,type(l3))

  # l4 = f.readline()
  # print(l4,type(l4))

  # l5 = f.readline()
  # print(l5 == "",type(l5))

  # line = f.readline()
  # while line != "":
  #   print(line)
  #   line = f.readline()

#* Write : "w"
# st = "This is string one two three four"
# with open("./Chapter-9/new1.txt","w") as f:
#   f.write(st)

#* append : "a"

with open("./Chapter-9/File.txt","a") as f:
  f.write("\n")
  for i in range(5):
    f.write(f"{i} ")
