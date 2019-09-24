PI = 3.14159

radius = 0

# asks the user for the radius of the hypothetical circle
radius_input = input("Enter the radius you desire: ")

# doubles the radius of the hypothetical circle
double_radius = 2 * float(radius_input)

radius = float(radius_input)

# calculates the circumference of the hypothetical circle
circumference = 2 * PI * radius

print("Your circumference is " + str(circumference))

# calculates the area of the hypothetical circle
area = PI * radius * radius

print("Your area is " + str(area))

# calculates the circumference in reference to the doubled radius
double_radius_circumference = 2 * PI * double_radius

# calculates the area in reference to the doubled radius
double_radius_area = PI * double_radius * double_radius

# calculates how many times larger the circumference would be with the doubled radius to the regular radius
circumference_increase = double_radius_circumference / circumference

# calculates how many times larger the area would be with the doubled radius to the regular radius
area_increase = double_radius_area / area

print("If your radius was " + str(double_radius) + ", the circumference would be " +
      str(circumference_increase) + " times bigger")

print("If your radius was " + str(double_radius) + ", the area would be " +
      str(area_increase) + " times bigger")
