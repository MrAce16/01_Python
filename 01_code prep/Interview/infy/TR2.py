# def track_robot(steps):
#     directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Directions: Right, Up, Left, Down
#     current_position = [0, 0]  # Starting at origin
#     current_direction = 0  # Starting facing right (East)
    
#     for m in steps:
#         if m == "L":
#             current_direction = (current_direction + 1) % 4  # Turn left
#         elif m == "R":
#             current_direction = (current_direction - 1) % 4  # Turn right
#         elif m == "F":
#             # Move forward in the current direction
#             current_position[0] += directions[current_direction][0]
#             current_position[1] += directions[current_direction][1]
    
#     return current_position

# # Test case
# steps = ["F", "R", "F", "L", "F"]
# final_position = track_robot(steps)
# print(final_position)


# mark.nelson@imaginelearning.com


def track_robot(steps):
	x,y = 0,0
	directions = ['E','S','w','N']
	current_direction = 0
	for m in steps:
		if m == '.':
			if directions[current_direction] =='E':
				x +=1
			elif directions[current_direction] =="S":
				y -=1
			elif directions[current_direction] =="W":
				x -=1
			elif directions[current_direction] =="N":
				y +=1
		elif m == '<':
			current_direction = (current_direction -1)%4
		elif m == '>':
			current_direction = (current_direction +1)%4
		return (x,y)
				
steps = "..<..<."
final_step= track_robot(steps)
print(final_step)
