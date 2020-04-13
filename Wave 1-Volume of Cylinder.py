import math

# read the radius and height of the cylinder from the user
radius = input("Enter a radius of the cylinder: ")
height = input("Enter a height of the cylinder: ")

# define the radius and height
radius = float(radius)
height = float(height)

# calculate the volume of the cylinder
volume = (math.pi*radius**2)*height
volume = float(volume)

# concatenation
print("The volume of the cylinder is: " + str(round(volume, 1)))
