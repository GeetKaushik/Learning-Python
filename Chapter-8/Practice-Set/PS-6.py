  #? Write a python function to remove a given word from a list ad strip it at the same time.


def rem(l, word):
  n = []
  for i in l:
    if  not (i == word):
      n.append(i.strip(word))
    l.remove(word)
    return l,n
  
l = ["Hello", "Good", "World", "Morning", "o" ]
print(rem(l,"o"))