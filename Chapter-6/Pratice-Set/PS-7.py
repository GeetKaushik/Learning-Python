  #? Write a program to find out whether a given post is talking about "Geet" or not.

key = "Geet"

msg = input("Enter the message: ")

if key.lower() in msg.lower():
  print(f"They are talking about {key}")
else:
  print(f"No they are not talking about {key}")