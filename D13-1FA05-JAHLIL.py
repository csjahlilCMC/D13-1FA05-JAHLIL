import math
 
# Ask the user for the coordinates
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Compute the distance using sqrt() and pow()
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Display the result
print(f"The distance between the two points is: {distance:.2f}")

# Reflection Comment:
# Using a library is much more practical because it's efficient, already tested, 
# makes your files look clean, and runs faster. From this activity, we calculated 
# a complex value, such as a square root, in Python using a simple built-in function 
# instead of coding it from scratch, as it saves time and prevents bugs.

# Short Note:
# The distance formula is important because it calculates the exact straight-line
# distance between two points on a coordinate plane.