  #? Write a python function which converts inche to cm

def inch_to_cm(inch):
  return round(inch * 2.54,2)
def feet_to_inch(feet):
  return feet*12
def feet_to_cm(feet):
  return inch_to_cm(feet_to_inch(feet))

print(feet_to_cm(5.8))