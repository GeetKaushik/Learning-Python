# Chapter - 6 : Conditional expressions

## In this chapter we will learn about conditional expressions such as if,elif,else,etc.

1. `if` - if condition is true do something
    - Example: 
    ```py
    a = 10
    if a > 1: #this is true then :-
      print("Yay! 🚀") #run this statement 👈
    ```
2. `elif` - commonly known as else if in other languages do something if this statement is true instead of first one
    - Example:
    ```py
    b =  10
    if b > 10: # this is not true then :-
      print("Doing something...")
    elif b == 10: # check this, if this is true then:-
      print("Yay! 🚀") # run this statement 👈
    ```
3. `else` - if none of the condition above is true then run else i.e., this condition
    - Example:
    ```py
    if c > 10: # this is not true then :-
      print("Doing something...")
    elif c < 10: # check this, if this is not true then:-
      print("Also doing something")
    else: # if none of the above works then:-
      print("Yay! 🚀") # run this statement 👈
    ```
- `else` and `elif` cannot be used alone you need `if` for them
- If one condition is true in if - else ladder it will not check further.
    - Example:
    ```py
    if False:
      # do something 1
    else if True: # it will exit from if-else ladder from here
      # do something 2
    else if True: # these conditions will not be checked
      # do something 3
    else if True: # these conditions will not be checked
      # do something 4
    else: # these conditions will not be checked
      # do something 5
    ```