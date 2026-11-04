# Functions & Math: Create a function called calculate_total that takes two numbers as arguments, adds them together, and returns the result.
def calculate_total(var1, var2):
    result = var1 + var2
    return result

# Conditionals: Assign a string to a variable (for example, "Maria"). Write an if/else block that prints "Welcome back!" if the variable matches that exact name, and "Access denied" if it does not.
name = "Maria"
if(name == "Maria"):
    print("Welcome back")
else:
    print("Access denied")

# Loops & Collections: Create a list containing the numbers 10, 20, and 30. Write a for-each loop that iterates through the list and prints each number multiplied by 2.
arr = [10,20,30]
for values in arr:
    print(values*2)