# Write a program to fill in a letter template given below with name and date.

name = input("Enter your name: ")
date = input("Enter Date: ")

letter = \
  f"""
  Dear <|Name|>,
  Life is great 😄
  <|Date|>
  """
print(letter)
print(letter.replace("<|Name|>",name).replace("<|Date|>",date))
