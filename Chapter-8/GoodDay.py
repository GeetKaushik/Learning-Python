def GoodDay(name = "Hooman"): #default argument
  print(f"Good Day, {name}")

name1 = input("Enter your name: ")
GoodDay(name1)
GoodDay() #If there is no argument it will take the default argument