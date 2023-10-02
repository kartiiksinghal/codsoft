#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("------------------------Codsoft Task-1------------------------")
print("Calculator")
'''Design a simple calculator with basic arithmetic operations.
   Prompt the user to input two numbers and an operation choice.
   Perform the calculation and display the result'''


# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main loop
while True:
    print("Available Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == '5':
        print("Toodles ;-)")
        break

    a = input("Enter first number: ")
    b = input("Enter second number: ")

    # Input validation using if-else statements
    if not a.isdigit() or not b.isdigit():
        print("Invalid input. Please enter valid numbers.")
        continue
    a = float(a)
    b = float(b)

    # Perform the selected operation
    if choice == '1':
        result = add(a, b)
        operation = '+'
    elif choice == '2':
        result = subtract(a, b)
        operation = '-'
    elif choice == '3':
        result = multiply(a, b)
        operation = '*'
    elif choice == '4':
        if b == 0:
            result = "Cannot divide by zero"
        else:
            result = divide(a, b)
        operation = '/'
    else:
        print("Invalid choice. Please select a valid operation.")
        continue

    # Display the result
    print(f"{a} {operation} {b} = {result}\n")


# In[ ]:




