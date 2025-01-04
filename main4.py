def mirrored_triangle(height):
    for i in range(1, height + 1):
        # Print spaces for the mirrored effect
        print(" " * (height - i), end="")
        # Print the stars for the current row
        print("*" * i)

# Input: Height of the triangle
try:
    height = int(input("Enter the height of the mirrored triangle: "))
    if height > 0:
        mirrored_triangle(height)
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")