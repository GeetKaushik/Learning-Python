
#? Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 - year old.

def table(n):
  table = f"🔢 Table of {n} 🔢\n"
  table += f"{'='*15}\n"
  for i in range(1,11):
    table += f"\t{n} x {i} = {n*i}\n"
  table += f"{'='*15}\n"
  return table

for i in range(2,21):
  with open(f"./Chapter-9/Practice-Set/Tables_2-20/Table_{i}.txt","w") as t:
    print("Generating...")
    t.write(table(i))
    # t.flush()
    print("Done ✅")
