from pyfiglet import Figlet
import os
import sys
import random

def main():
    height = 50
    width = 80
    wall = "█"
    not_visited = "n"
    hall = " "
    player = "Θ"
    prev_locations = []


    while True:    
        play_game, difficulty = start_game()
        if play_game == False:
            clear_screen()
            f = Figlet(font="bubble", justify="center", width=80)
            print(f.renderText("Thanks for Playing"))
            sys.exit()
        if difficulty == "easy":
            height = 10
            width = 20
        elif difficulty == "medium":
            height = 20
            width = 40
        elif difficulty == "hard":
            height = 30
            width = 60
        clear_screen()
        
        
        maze = maze_maker(height, width, wall, not_visited) # Returns blank maze with unvisited squares and a wall all around
        maze = maze_builder(maze, height, width, wall, not_visited, hall, prev_locations) # Builds maze with walls and corridors           
        maze = remove_unvisited(maze, not_visited, wall) # Takes out unvisited squares that are leftover after building maze.
        maze, top, bottom = entrance_exit(maze) # selects a start and end location
        maze_start = [0,top]
        maze_finish = [len(maze) - 1, bottom]
        player_position = [0,top]
        
        maze[player_position[0]][player_position[1]] = player
        
        win = game_loop(maze, player_position, maze_start, maze_finish, player, hall)
        if win == True:
            clear_screen()
            g = Figlet(font="bubble", justify="center", width=80)
            print(g.renderText("You Won\nCongratulations!"))
            sys.exit() 

def clear_screen():
    return os.system("cls" if os.name=="nt" else "clear")


def pick_start(height,width):
    # pick a starting square in maze
    
    loc_h = random.randint(1,height - 2)
    loc_v = random.randint(1,width - 2)

    return loc_h, loc_v


def maze_maker(height, width, wall, not_visited):
    #This creates a blank maze with the outer walls and unvisited squares

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
    #sometimes there's a few univisted squares left.  This turns them into walls after maze is constructed

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
    #Code for creating maze itself

    loc_h, loc_v = pick_start(height, width)
    maze = mark_walls(maze, loc_h, loc_v, wall, not_visited, hall)

    while True:
        direction_choices = check_edge(loc_h, loc_v, height, width)
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
    #creates walls around new hall block

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


def check_edge(loc_h, loc_v, height, width):
    #check to make sure we're not near an edge and if we are, remove that as an option so there's no out of range issues and no issues for maze maker

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
    #This makes sure you can't go to a block that's been visited before or through a wall to a block that's been visited.
    #Leaves only options that work for maze maker

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
    #After all invalid directions have been removed, this picks the direction to create new hall piece.

    return random.choice(direction)


def entrance_exit(maze):
    #create an entrance at top wall of maze and exit at bottom end.  Also makes sure the adjacent block into maze is not a wall.

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
    #This actually adjusts the movement to the next block after the direction has been chosen by the map pick direction.
    #It also appends previous locations to a list so that it can be tracked back if you end up in a dead end.

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


def game_loop(maze, player_position, maze_start, maze_finish, player, hall):
    #This is the game loop after maze has been created.  Once player has decided to start game, this function is called and is the main playing function
    legal = None

    while True:
        while True:
            win = check_win(player_position, maze_finish)
            if win == True:     #Checks if the player has arrived on the exit block
                return True
            clear_screen()      #Clears screen after every move made
            print_maze(maze)    #Prints maze in current format with all positions including player, walls, halls and entrance/exit.
            print("\n")
            key_pressed = input('"Press w - enter" - To Move UP\n"Press s - enter" - To Move DOWN\n"Press a - enter" - To Move LEFT\n"Press d - enter" - TO Move RIGHT\n\nMOVE: ').strip().lower()
            match key_pressed:  #Check for move chosen
                case "w":
                    legal = check_legal(maze, player_position, maze_start, maze_finish, player, "w")
                    if legal == True:
                        maze[player_position[0]][player_position[1]] = hall
                        player_position[0] = player_position[0] - 1
                        maze[player_position[0]][player_position[1]] = player
                    break
                case "s":
                    legal = check_legal(maze, player_position, maze_start, maze_finish, player, "s")
                    if legal == True:
                        maze[player_position[0]][player_position[1]] = hall
                        player_position[0] = player_position[0] + 1
                        maze[player_position[0]][player_position[1]] = player
                    break
                case "a":
                    legal = check_legal(maze, player_position, maze_start, maze_finish, player, "a")
                    if legal == True:
                        maze[player_position[0]][player_position[1]] = hall
                        player_position[1] = player_position[1] - 1
                        maze[player_position[0]][player_position[1]] = player
                    break
                case "d":
                    legal = check_legal(maze, player_position, maze_start, maze_finish, player, "d")
                    if legal == True:
                        maze[player_position[0]][player_position[1]] = hall
                        player_position[1] = player_position[1] + 1
                        maze[player_position[0]][player_position[1]] = player
                    break
                case _:
                    continue
                
                #stays in loop until check_win return True


def check_legal(maze, player_position, maze_start, maze_finish, player, move):
    #Checks if move chosen by player is legal.  Returns False if it isn't(edge of board, wall, etc) or True if it is
    
    if move == "w":
        if player_position[0] == 0:
            return False
        elif player_position[0] == 1 and player_position[1] == maze_start[1]:
            return False
        elif maze[player_position[0] - 1][player_position[1]] != " ":
            return False
        else:
            return True
    if move == "s":
        if player_position[0] == len(maze) - 2 and player_position[1] != maze_finish[1]:
            return False
        elif maze[player_position[0] + 1][player_position[1]] != " ":
            return False
        else:
            return True
    if move == "a":
        if player_position[1] == 1:
            return False
        elif maze[player_position[0]][player_position[1] - 1] != " ":
            return False
        else:
            return True
    if move == "d":
        if player_position[1] == len(maze[0]) - 2:
            return False
        elif maze[player_position[0]][player_position[1] + 1] != " ":
            return False
        else:
            return True


def check_win(player_position, maze_finish):
    #checks if the player's position matches the block for maze exit

    if player_position[0] == maze_finish[0] and player_position[1] == maze_finish[1]:
        return True
    else:
        return False


def start_game():
    #Start Screen.  Player can choose to play or quit
    
    while True:
        clear_screen()
        f = Figlet(font="epic", justify="center", width=80)
        print(f.renderText("Welcome to Mazed"))
        print("\n\n") 
        try:
            answer = input("What do you want to do?\n\n(1) Start Easy Difficulty Game\n\n(2) Start Medium Difficulty Game\n\n(3) Start Hard Difficulty Game\n\n(4) Quit\n\n")
            if answer == "1":
                return True, "easy"
            if answer == "2":
                return True, "medium"
            if answer == "3":
                return True, "hard"
            elif answer == "4":
                return False, "none"
            else:
                continue
        except ValueError:
            pass


def print_maze(maze):
    # Print maze as is

    for c in range(0, len(maze)):
        for d in range(0, len(maze[c])):
            print(maze[c][d], end="")
        print("")


if __name__ == "__main__":
    main()