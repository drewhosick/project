import random

def main():
    height = 10
    width = 20
    wall = "#"
    not_visited = "n"
    hall = "h"

    # returns blank maze with unvisited squares and a wall all around
    maze = maze_maker(height, width, wall, not_visited, hall) 
    #maze = maze_builder(maze, height, width, wall, not_visited, hall)

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
        

def maze_builder(maze, height, width, wall, not_visited, hall):
    ...
    #pick a random square to start

    #mark square a visited and make it an open corridor with walls on each side.

    #move in any direction choosing unvisited square.

    #repeat
    
    #if you arrive where you cannot move since it's walls all around then back up till you find a spot that has unvisited in one of the 4 directions

    #keep going till all squares are visited.

    #cut entrance and exit.
















if __name__ == "__main__":
    main()