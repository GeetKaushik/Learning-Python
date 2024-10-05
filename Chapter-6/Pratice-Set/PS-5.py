  #? Write a program which finds out whether a given name is present in a list or not.

list1 = ["Geet", "Gowthami", "Sanu", "Mukul"]
name = input("Enter your name: ")

if(name in list1):
  print(f"Congratulations 🎊 {name}, Your name is in the list 😄")
else:
  print(f"Sorry {name}, Your name is not in the list 😢")