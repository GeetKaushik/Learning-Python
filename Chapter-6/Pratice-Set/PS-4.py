  #? Write a program to find whether a given username contains more  than 10 characters or not.

usrname = input("Enter Username: ")

if(len(usrname) > 10):
  print(f"Username {usrname} is too long!!!")
else:
  print("Thats a Great name 😃")