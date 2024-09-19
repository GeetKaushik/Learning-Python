planets = ["Mercury", "Venus", 3, 4.00, "Jupiter", True]
print(planets)
planets[2] = "Earth"
print(planets)

planets.append("Uranus") # adds a new element at the end of the list : returns None
print(planets)

numbers = [1,9,8,3,4,2,5,6,7]
characters = ["a","e","b","c","d"]
planets2 = ["Mercury", "mercury", "Venus", "venus", "earth","Earth"]
planets2.sort() #It will sort string lexicographically
characters.sort() #It will sort string lexicographically
numbers.sort() # Works only on sortable list
numbers.sort(reverse=True) # sort list in descending order
print(numbers)
print(characters)
print(planets2)


numbers.insert(4,10) # Insert element [10] at index [4] : returns None
print(numbers)

print(numbers.pop(4)) # Remove element at index [4] : returns the element
print(numbers.pop()) # Default: Removes the last element of the list : returns the element
print(numbers)
