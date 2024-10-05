# Chapter - 6 : Loops in Python

## In this Chapter we will learn about loops in python

## 1. `for` Loop

A `for` loop is used for iterating over a sequence (such as a list, tuple, dictionary, set, or string).

### Syntax:
```python
for element in sequence:
    # code block
```
### Example:
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

## 2. `while` Loop

A `while` loop allows code to execute repeatedly as long as a condition is true.

### Syntax:
```python
while condition:
    # code block
```

### Example:
```python
i = 0
while i < 5:
    print(i)
    i += 1
```

## 3. Nested Loops

Loops inside loops are called nested loops.

### Example:
```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

## - `break` Statement

Used to exit the loop before it has looped through all items.

### Example:
```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

## - `continue` Statement

Skips the rest of the code inside the loop for the current iteration.

### Example:
```python
for i in range(5):
    if i == 3:
        continue
    print(i)
```

## - `else` with Loops

The `else` block in a loop is executed after the loop completes its iteration normally.

### Example:
```python
for i in range(5):
    print(i)
else:
    print("Loop finished")
```

This `else` block will not be executed if the loop is terminated by a `break` statement.