from pyfiglet import Figlet
import os
import sys
import random

def main():
    height = 20
    width = 40
    wall = "█"
    not_visited = "n"
    hall = " "
    player = "Θ"
    prev_locations = []


    while True:    
        play_game = start_game()
        if play_game == False:
            clear_screen()
            f = Figlet(font="bubble", justify="center", width=80)
            print(f.renderText("Thanks for Playing"))
            sys.exit()
        clear_screen()
        
        
        maze = maze_maker(height, width, wall, not_visited) # Returns blank maze with unvisited squares and a wall all around
        maze = maze_builder(maze, height, width, wall, not_visited, hall, prev_locations) # Builds maze with walls and corridors           
        maze = remove_unvisited(maze, not_visited, wall) # Takes out unvisited squares that are leftover after building maze.
        maze, top, bottom = entrance_exit(maze) # selects a start and end location
        maze_start = [0,top]
        maze_finish = [len(maze) - 1, bottom]
        player_position = [0,top]
        
        maze[player_position[0]][player_position[1]] = player
        
        game_loop(maze, player_position, maze_start, maze_finish, player)
        
        sys.exit()  

def clear_screen():
    return os.system("cls" if os.name=="nt" else "clear")


def pick_start(height,width):
    
    # pick a starting square in maze
    loc_h = random.randint(1,height - 2)
    loc_v = random.randint(1,width - 2)

    return loc_h, loc_v


def maze_maker(height, width, wall, not_visited):
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


def remove_unvisited(maze, not_visited, wall):
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


def entrance_exit(maze):
    while True:
        top = random.randint(1, len(maze[0]) - 2)
        if maze[1][top].isspace():
            maze[0][top] = " "
            break
        else:
            continue
    while True:
        bottom = random.randint(1, len(maze[0]) - 2)
        if maze[len(maze) - 2][bottom].isspace():
            maze[len(maze) - 1][bottom] = " "
            break
        else:
            continue

    return maze, top, bottom


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


def game_loop(maze, player_position, maze_start, maze_finish, player):
    #moves character in maze
    while True:
        while True:
            clear_screen()
            print_maze(maze)
            print("\n")
            key_pressed = input('"Press w - enter" - To Move UP\n"Press s - enter" - To Move DOWN\n"Press a - enter" - To Move LEFT\n"Press d - enter" - TO Move RIGHT\n\nMOVE: ').strip().lower()
            match key_pressed:
                case "w":
                    legal = check_legal(maze, player_position, maze_start, maze_finish, player, "w")
                    #check if going up is a legal move(not start and not wall)
                case "s":
                    ...
                    #check if going down is a legal move(not wall) and check if win
                case "a":
                    ...
                    #check if going left is a legal move(not wall)
                case "d":
                    ...
                    #check if going right is a legal move(not wall)
                case _:
                    continue
        
        #stay in loop until check_win return True
        #call check_win after every move to check if win condition
    print_maze(maze)


def check_legal(maze, player_position, maze_start, maze_finish, player, move):
    if move == "w":
        if player_position[0] == 0:
            return False
        elif player_position[0] == 1 and player_position[1] == maze_start[1]:
            return False
        elif maze[player_position[0] - 1][player_position[1]] != " ":
            return False
        else:
            return True

def check_win():
    #check if character is in winning location
    ...


def start_game():
    while True:
        clear_screen()
        f = Figlet(font="epic", justify="center", width=80)
        print(f.renderText("Welcome to Mazed"))
        print("\n\n") 
        try:
            answer = input("What do you want to do?\n\n(1) Start Game\n\n(2) Quit\n\n")
            if answer == "1":
                return True
            elif answer == "2":
                return False
            else:
                continue
        except ValueError:
            pass


def print_maze(maze): # Print maze as is
    for c in range(0, len(maze)):
        for d in range(0, len(maze[c])):
            print(maze[c][d], end="")
        print("")


if __name__ == "__main__":
    main()