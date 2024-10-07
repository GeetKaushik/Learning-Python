# Chapter - 9 : File I/O

## 1. Introduction to File I/O
- File I/O (Input/Output) refers to the process of reading from and writing to files.
- Python provides built-in functions to handle files.

## 2. Opening a File
- Use the `open()` function to open a file.
- Syntax:
  ```python
  file = open('filename.txt', 'mode')
  ```
- Modes:
  - `'r'`: Read (default mode)
  - `'w'`: Write (creates a new file or truncates an existing file)
  - `'a'`: Append (adds content to the end of the file)
  - `'b'`: Binary mode (for non-text files)
  - `'x'`: Exclusive creation (fails if the file exists)

## 3. Reading from a File
- Methods to read from a file:
  - `read()`: Reads the entire file.
  - `readline()`: Reads the next line from the file.
  - `readlines()`: Reads all lines and returns a list.

### Example:
```python
with open('file.txt', 'r') as file:
    content = file.read()
    print(content)
```

## 4. Writing to a File
- Use `write()` to write a string to the file.
- Use `writelines()` to write a list of strings.

### Example:
```python
with open('file.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.writelines(['Line 1\n', 'Line 2\n'])
```

## 5. Closing a File
- Always close a file after completing operations using `close()` method.
- Using `with` statement automatically closes the file.

### Example:
```python
file = open('file.txt', 'r')
# Perform file operations
file.close()
```

## 6. Exception Handling
- Handle exceptions while working with files using `try-except` blocks.
  
### Example:
```python
try:
    with open('file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
```

## 7. Working with JSON Files
- Use `json` module for reading and writing JSON files.
- Methods:
  - `json.load()`: Read from a JSON file.
  - `json.dump()`: Write to a JSON file.

### Example:
```python
import json

# Writing to a JSON file
data = {'name': 'Geet', 'age': 22}
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)

# Reading from a JSON file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)
    print(data)
```