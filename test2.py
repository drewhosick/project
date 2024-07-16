import random


def create_maze():
    # Maze Tessalation Method.  
    # Build a small maze and copy three times

    maze = [
        ["#", "#", "#", "#", "#"],
        ["#", " ", "#", " ", "#"],
        ["#", "#", "#", "#", "#"],
        ["#", " ", "#", " ", "#"],
        ["#", "#", "#", "#", "#"]
    ]

    select = random.choice(["top","left","right","bottom"]) # leave one remaining full wall and remove others

    match select:
        case "top":
            maze[2][1] = " "
            maze[2][3] = " "
            maze[3][2] = " "
        case "left":
            maze[1][2] = " "
            maze[2][3] = " "
            maze[3][2] = " "
        case "right":
            maze[1][2] = " "
            maze[2][1] = " "
            maze[3][2] = " "
        case "bottom":
            maze[1][2] = " "
            maze[2][1] = " "
            maze[2][3] = " "
    
    maze = doubler(maze)
    maze = doubler(maze)

    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            print(maze[i][j], end="")
        print()
    

def doubler(maze):
    for i in range(0, len(maze)):
        for j in range(1, len(maze[i])):
            maze[i].append(maze[i][j])
    for k in range(1, len(maze)):
            maze.append(list(maze[k]))

    return(maze)

def cut_walls(maze): 
    width = len(maze[0])
    wall = []
    for l in range(0, width):
        if l % 4 != 0:
            wall.append(l)

    middle = int((len(maze) - 1) / 2)
    

    options = ["top","left","right","bottom"]
    select = random.choice(options)
    options.remove(select)

    if "top" in options:
        wall_c = wall[0:3]
        for wall_piece_t in wall[0:3]:
            if maze[wall_piece_t][middle - 1] == "#" or maze[wall_piece_t][middle + 1] == "#":
                wall_c.remove(wall_piece_t)
        passage_t = random.choice(wall_c)
        
        maze[passage_t][middle] = " "

    if "bottom" in options:
        wall_c = wall[-3:]
        for wall_piece_b in wall[-3:]:
            if maze[wall_piece_b][middle - 1] == "#" or maze[wall_piece_b][middle + 1] == "#":
                wall_c.remove(wall_piece_b)
        passage_b = random.choice(wall_c)
        
        maze[passage_b][middle] = " "

    if "left" in options:
        wall_c = wall[0:3]
        for wall_piece_l in wall[0:3]:
            if maze[middle - 1][wall_piece_l] == "#" or maze[middle + 1][wall_piece_l] == "#":
                wall_c.remove(wall_piece_l)
        passage_l = random.choice(wall_c)
        maze[middle][passage_l] = " "

    if "right" in options:
        wall_c = wall[-3:]
        for wall_piece_r in wall[-3:]:
            if maze[middle - 1][wall_piece_r] == "#" or maze[middle + 1][wall_piece_r] == "#":
                wall_c.remove(wall_piece_r)
        passage_r = random.choice(wall_c)
        
        maze[middle][passage_r] = " "
     
    return maze





create_maze()