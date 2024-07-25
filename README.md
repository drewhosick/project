# Mazed
## Video Demo: [Mazed](https://youtu.be/WdXMzM6Ltt4)
### Description:

A maze creator and game all-in-one.
    
Not only can you try to navigate a maze in this game but, more importantly, this code creates a random maze for you every time you play.  Given three options(small, medium, large), a maze is created using a maze generator algorithm called randomized depth-first search or "recursive backtracker".  I used the explanation of how it should work at [this Wikipedia page](https://en.wikipedia.org/wiki/Maze_generation_algorithm) on Maze Generation Algorithms.
    
While I did use the ideas on here, I am very proud that I was able to write the code itself to accomplish the required goals to generate the maze.  I've been wanting to create a randomized maze program for years previously but had no idea how to actually accomplish it.  The idea of breaking down the different tasks into functions really made it an easier task.

## Functions Explained

### start_game():

Literally starts the game with a screen that has the game title and the option to choose different maze sizes(difficulties)

### maze_maker():

This creates only a blank maze with unvisited squares as a sort of 2d list(lists within a list).  Each item is a block in the maze that can become a wall, hallway or entrance/exit.  maze_maker then creates walls all around the maze.

### maze_builder() and remove(unvisited)

Where the magic happens.  Calls a function pick_start to pick the starting location.  That starting location can only be within the walls of the maze in an unvisited square.

Once that's done it marks the square as a hall and marks walls around it.

After that a loop begins which first looks for which directions the next hall will be.  It checks for the edge so it won't eat into an outer wall and removes that option(move towards that direction) if it is in the last legal square beside the outer edge wall.

After it is removed it then looks for visited squares around it and removes those as options to go to.  Not only does it look for a visited square in all 4 directions but it also looks for a visited square an extra step away in all 4 directions if there's a wall in that same direction.  This way no halls can be created through an existing wall into another hall.

Whatever directions remain are sent back and one is chosen randomly to move to that square, make it a hall and surrounding 4 blocks are turned into walls if they are unvisited(which means the previous hall block will not then turn into a wall and is kept as is)

A list of the previous locations is also kept since this is a recursive backtracker algorithm.  Eventually you will end up not being able to move forward when all 4 directions are unavailable as unvisited squares.  Then the current hall location will be recursed until one of the directions offers a previously unvisited square.

This will keep happening until all squares have been visited.

Please note sometimes a few blocks are left unvisited after the loop recurses all the way back to the start and has not found a new block that is unvisited on its path back.  I have yet to find out why this is happening but I've created another function that goes to clean up those few unvisited blocks if there are any left and make them into adjacent walls.  It doesn't affect gameplay at all other than making the maze a little smaller.  Most of the time I've seen only a few in a fairly large maze.

### entrance_exit()

Entrance and exit are created with this function by allowing a randome selection of a legal entrance on the top wall and exit on the bottom wall.  As long as it's not the outer corners and there's a hall adjacent to the potential choice, it is a legal entrance/exit.

Player position is the set to the same spot as entrance.

### game_loop()

The game loop is then called and the player must select w(up) s(down) a(left) d(right) and press enter to move.  It will only allow you to move if it's a legal move(no wall in the way, cannot move back to entrance, you can move into exit).  After the move is complete it will check if you are in a winning condition.  If not, it will redraw the maze with the new location and the loop continues.  Otherwise it breaks out of the loop to show a congratulations message.

## Other files

You'll notice other files in the project folder.

The test_project.py file is obviously the pytest required for the project.  It tests four functions.

This README.md file

test_maze_code1.py and testing_maze_code2.py are both files with maze algorithms written into them.  I was originally worried about using the current algorithm to create my maze so I started with a different algorithm called Fractal Tessellation but I found that I didn't like how the maze looked a little too repetitive and then I ran into some issues with that algorithm and decided to just do it "right" with my current version.  It's what I always wanted to accomplish anyways and I'm happy I did.  I used some of the code I wrote and then copied the basics into the full .py file and worked from there.  I just wanted to keep the originals with all the details I had at the time.

requirements.txt includes all the libraries I used to create this project that had to be installed from pip.

### I hope you like my project and feel free to reach out if you have questions