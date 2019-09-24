# the amount of square feet of coverage a single paint-can can paint
COVERAGE = 400

# asks the user for the length of a room
length = float(input("What is the length of your room in feet?: "))

# asks the user for the width of the room
width = float(input("What id the width of your room in feet?: "))

# asks the user for the height of the room
height = float(input("What is the height of your room in feet?: "))

# asks the user for the desired amounts of coats to apply
coats = float(input("How many coats of paint are you going to use?: "))

# calculates the total surface area of the room minus the floor (oh perish the thought)
surface_area = (2*length*height) + (2*width*height) + length*width

# sees the total coverage of the paint, with the multiple coats applied
coverage_needed = surface_area*coats

# calculates the amount of paint cans required to meet the users needs
cans_of_paint_required = coverage_needed/COVERAGE

print("For a room that size, you would need to buy " + str(cans_of_paint_required) +
      " cans of paint to paint " + str(coats) + " coats.")