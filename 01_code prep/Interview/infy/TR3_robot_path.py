def track_robot(steps):
    x, y = 0, 0
    directions = ['E', 'S', 'W', 'N']  
    current_direction = 0
    
    for m in steps:
        if m == '.':
            if directions[current_direction] == 'E':
                x += 1
            elif directions[current_direction] == 'S':
                y -= 1
            elif directions[current_direction] == 'W':
                x -= 1
            elif directions[current_direction] == 'N':
                y += 1
        elif m == '<':
            current_direction = (current_direction - 1) % 4
        elif m == '>':
            current_direction = (current_direction + 1) % 4
    
    return [x, y]  

steps = "..<..<."
final_step = track_robot(steps)
print(final_step) 

