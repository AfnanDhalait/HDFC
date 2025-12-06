# Sample Python Program
# Author: Your Name

# Function to greet a user
def greet_user(name):
    return f"Hello, {name}! Welcome to Python."

# Using the function
user_name = "John"
print(greet_user(user_name))

# Basic arithmetic function
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print("The sum is:", result)

# Working with lists
colors = ["Red", "Green", "Blue"]
colors.append("Yellow")
print("Color List:", colors)

# Simple dictionary (similar to JavaScript object)
person = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}

# Function using dictionary
def show_person_info(p):
    print(f"Name: {p['name']}")
    print(f"Age: {p['age']}")
    print(f"Student: {p['is_student']}")

show_person_info(person)

# Simple loop
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i)
