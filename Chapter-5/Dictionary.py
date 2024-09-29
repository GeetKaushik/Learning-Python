emptyDict = {} #Empty Dictionary
emptyDict2 = dict() #Empty Dictionary
marks = {
  "Geet" : 100,
  "Sanu" : 90,
  "Mukul" : 80,
  "Ishan" : 70,
}

print(marks, type(marks))
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Geet" : 90, "Gowthami" : 80})
print(marks)
print(marks.get("Geet")) # returns None is Key is not present
print(marks["Geet"]) # Gives an error if Key is not present
print(marks.pop("Ishan"))
print(marks.popitem())
print(marks.popitem())