
#? Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'

word = "Z"
with open("./Chapter-9/Practice-Set/poems.txt") as f:
  data = f.read()
  if word.lower() in data.lower(): print(True)
  else: print(False)