
#? The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score. You need to write a progtam to update the Hi-score whenever the game() function breaks the Hi-score.

import random
def clear():
  with open("./Chapter-9/Practice-Set/hiscore.txt","w") as f:
    f.flush()

def game(n):
  print("Game Start 🟩")
  print("="*20)

  # Logic
  rolls = []
  for i in range(n):
    rolls.append(random.randint(1,6))
  score = sum(rolls)
  print("Rolls:",rolls)
  print("Your Score:",score)

  # Fetching Data
  with open("./Chapter-9/Practice-Set/hiscore.txt","r") as f:
    hiscore = f.read()
    if hiscore == "": hiscore = 0
    else: hiscore = int(hiscore)
    print("Hi-score:",hiscore)

  if(score > hiscore):
    with open("./Chapter-9/Practice-Set/hiscore.txt","w") as f:
      f.write(str(score))

  print("="*20)
  print("Game Over 🟥")

game(5)
# clear()