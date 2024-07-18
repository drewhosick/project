import random

def main():
    height = 20
    width = 40
    wall = "█"
    not_visited = "n"
    hall = " "
    prev_locations = []

    # returns blank maze with unvisited squares and a wall all around
    maze = maze_maker(height, width, wall, not_visited, hall) 
    maze = maze_builder(maze, height, width, wall, not_visited, hall, prev_locations)
        
    maze = remove_unvisited(maze, height, width, not_visited, wall)
    
    #cut entrance and exit

    # Print maze as is
    for c in range(0, len(maze)):
        for d in range(0, len(maze[c])):
            print(maze[c][d], end="")
        print("")


def maze_maker(height, width, wall, not_visited, hall):
    maze = []

    for a in range(0, height):
        single_list = []
        for b in range(0, width):
            single_list.append(not_visited)
        maze.append(single_list)
  
    for e in range(0, len(maze[0])):
        maze[0][e] = wall
    for f in range(0, len(maze[len(maze) - 1])):
        maze[len(maze) - 1][f] = wall
    for g in range(0, len(maze)):
        maze[g][0] = wall
        maze[g][len(maze[len(maze) - 1]) - 1] = wall

    return maze


def remove_unvisited(maze, height, width, not_visited, wall):
    maze_rebuild = []

    for a in maze:
        single_list = a
        new_list = []
        for b in single_list:
            if b == not_visited:
                new_list.append(wall)
            else:
                new_list.append(b)
        maze_rebuild.append(new_list)
    
    return maze_rebuild


def maze_builder(maze, height, width, wall, not_visited, hall, prev_locations):
    

    loc_h, loc_v = pick_start(height, width)
    maze = mark_walls(maze, loc_h, loc_v, wall, not_visited, hall)

    while True:
        direction_choices = check_edge(maze, loc_h, loc_v, height, width)
        direction_choices = check_visited(maze, loc_h, loc_v, direction_choices)
        if len(direction_choices) != 0:
            direction_chosen = pick_direction(direction_choices)
        else:
            if len(prev_locations) != 0:
                previous = prev_locations[-1:]
                previous = previous[0]
                loc_h = int(previous[0])
                loc_v = int(previous[1])
                prev_locations = prev_locations[0:-1]
                continue
            else:
                return maze
            
        loc_h, loc_v, prev_locations, direction_chosen = move(loc_h, loc_v, prev_locations, direction_chosen)
        maze = mark_walls(maze, loc_h, loc_v, wall, not_visited, hall)
    

def pick_start(height,width):
    
    # pick a starting square in maze
    loc_h = random.randint(1,height - 2)
    loc_v = random.randint(1,width - 2)

    return loc_h, loc_v


def mark_walls(maze, loc_h, loc_v, wall, not_visited, hall):
    maze[loc_h][loc_v] = hall
    if maze[loc_h + 1][loc_v] != hall:
        maze[loc_h + 1][loc_v] = wall
    if maze[loc_h - 1][loc_v] != hall:
        maze[loc_h - 1][loc_v] = wall
    if maze[loc_h][loc_v + 1] != hall:
        maze[loc_h][loc_v + 1] = wall
    if maze[loc_h][loc_v - 1] != hall:
        maze[loc_h][loc_v - 1] = wall
    return maze


def check_edge(maze, loc_h, loc_v, height, width):
    direction = ["up", "down", "left", "right"]
    if loc_h == height - 2:
        direction.remove("down")
    if loc_h == 1:
        direction.remove("up")
    if loc_v == width - 2:
        direction.remove("right")
    if loc_v == 1:
        direction.remove("left")
    
    return direction


def check_visited(maze, loc_h, loc_v, direction):

    if "up" in direction:
        if maze[loc_h - 2][loc_v] == " " or maze[loc_h - 1][loc_v] == " " or maze[loc_h - 1][loc_v + 1] == " " or maze[loc_h - 1][loc_v - 1] == " ":
            direction.remove("up")
    if "down" in direction:
        if maze[loc_h + 2][loc_v] == " " or maze[loc_h + 1][loc_v] == " " or maze[loc_h + 1][loc_v + 1] == " " or maze[loc_h + 1][loc_v - 1] == " ":
            direction.remove("down")
    if "left" in direction:
        if maze[loc_h][loc_v - 2] == " " or maze[loc_h][loc_v - 1] == " " or maze[loc_h - 1][loc_v - 1] == " " or maze[loc_h + 1][loc_v - 1] == " ":
            direction.remove("left")
    if "right" in direction:
        if maze[loc_h][loc_v + 2] == " " or maze[loc_h][loc_v + 1] == " " or maze[loc_h - 1][loc_v + 1] == " " or maze[loc_h + 1][loc_v + 1] == " ":
            direction.remove("right")
        

    return direction


def pick_direction(direction):
    return random.choice(direction)


def move(loc_h, loc_v, prev_locations, direction_chosen):
    prev_locations.append([str(loc_h),str(loc_v)])

    if direction_chosen == "up":
        loc_h = loc_h - 1
    elif direction_chosen == "down":
        loc_h = loc_h + 1
    elif direction_chosen == "left":
        loc_v = loc_v - 1
    elif direction_chosen == "right":
        loc_v = loc_v + 1

    return loc_h, loc_v, prev_locations, direction_chosen


if __name__ == "__main__":
    main()