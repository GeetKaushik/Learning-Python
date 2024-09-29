# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

dictionary = {
  "Pani" : "Water",
  "Fal" : "Fruits",
  "Sabji" : "Vegetables",
  "Pankha" : "Fan",
  "Billi" : "Cat",
  "Kursi" : "Chair"
}

usrInp = input("Enter your word: ")

print("Translation:",dictionary.get(usrInp))