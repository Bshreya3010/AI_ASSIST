# Refactoring means improving code readability and structure without changing its behavior.
# It helps make the code easier to understand, maintain, and modify.

# Example: an even/odd number checker before and after refactoring.

# Before refactoring
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(num, "is even")
# else:
#     print(num, "is odd")

# After refactoring
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Refactoring improvements:
# 1. Uses a clearer variable name: number instead of num
# 2. Uses f-strings for cleaner and simpler output
# 3. Keeps the logic the same while making the code easier to read
# 4. Improves code quality without changing the program's result
