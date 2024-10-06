# Chapter - 8 : Functions and Recursions

## In this chapter we will learn about *functions* and *recusion*
---


## Introduction to Functions

A function in Python is a reusable block of code that performs a specific task. Functions help organize your code, make it more readable, and avoid repetition.

### Basic Syntax

```python
def function_name(parameters): # Function Defination
    # Code block
    return value  # Optional
     
function_name(arguments) #Function Call
```
### Example
```python
def greet(name): # Function Defination
  return f"Hello, {name}"

greet("Geet") #Function Call
```
---
---
## Recursion

Recursion is a programming technique where a function calls itself to solve smaller instances of the same problem. It is commonly used in problems like factorials, Fibonacci numbers, and tree traversal.

**Important Points:**
1.	Base Case: The condition that stops the recursion.
2.	Recursive Case: The part of the function where it calls itself with a smaller problem.

### Example: Factorial Using Recursion

The factorial of a number n is the product of all positive integers less than or equal to n. It is defined as:

	•	0! = 1
	•	n! = n * (n-1)! for n > 0

Here’s how to implement factorial using recursion:
```python
def factorial(n):
    if n == 0:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Example usage
print(factorial(5))  # Output: 120
```

