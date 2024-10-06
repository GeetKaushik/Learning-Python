''' [ Rock, Paper and Scissors Game ] '''

import random
CHOICE = { "r" : "Rock", "p" : "Paper", "s" : "Scissors" }

print("[ Rock, Paper and Scissors Game ]")
print("Game Starts! 🟩")
while True:
  # Choices
  computer = random.choice(["r","p","s"])
  you = input("Enter your choice (r for Rock, p for Paper, s for Scissors, q to Quit): ")
  # Control Cases
  if you.lower() == "q":
    print("Game Over! 🟥")
    break
  if you not in CHOICE:
    print("Invalid Choice 🟨")
    continue
  
  # Choices made
  print("="*20)
  print("Computer:",CHOICE[computer])
  print("You:",CHOICE[you])

  # Logic
  if (computer == "r" and you == "p")\
    or (computer == "p" and you == "s")\
    or (computer == "s" and you == "r"): print("You Win 🎊")
  elif computer == you: print("Its a Draw 🏳️")
  else: print("You Loose 😢")
  print("="*20)

