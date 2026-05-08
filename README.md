# Final-Project-ProgrammingForDigitalArts-ZhengJames
The repository for my final project coded in Python.

# PROJECT TITLE

## Demo
Demo Video: <URL>

## GitHub Repository
GitHub Repo: <https://github.com/JimmyZheng70/Final-Project-ProgrammingForDigitalArts-ZhengJames>

## Description
My final project is a Breakout like game in which the player has a paddle that can move left and right, boucning the ball to destroy the blocks, earning points. One major difference is the unique mechanic with color switching, which makes the ball switch to either blue or pink with each bounce, and the player must match the color by switching to the same color in order to not die. This game requires not only tracking, but also memory and reaction speed to be successful in the game.

Player's move either left or right by pressing the Left/Right arrow or the A/D keys. To accomnplish this, I used pyagame, with getting the get_pressed in order to get the player's input. One reason why the player uses get_pressed and not event type is because get_pressed allows the key to be held down to move, but using event type can only do once. During tetsing, it was originally with event down, but I had to repetively pressed the key to move, which was too annoying, hence it using the get_pressed pyagame. Additioanlly, the logic behind it was placed inside the Player class, with it telling the direction of either left or right of the screen through checking if its value is 1 or -1. The logic also checked if the player is out of bounds and blocked them from going out. This also worked for both resizes of the screen for out of bounds.

The Ball, which is coded inside its own class, moves by subtracting the position of its shape to its speed, leading it to more up with the subtraction when starting. For the bounce off the walls, the Ball class compares where it is on screen, and goes to the opposite direction through multiplying with -1, changing the direction, to either left or right for the side walls, and down for the top wall. For the bottom wall, it will instead go through. The ball also checks inside the movement method, as it was the easiest way to check for other objects, if its hits a block, player, or reaches the bottom. If it hits a block, it will destroy the block and gives the point, sending that number into the main class. Also it will bounce off the player, and the bounce direction can be somewhat manipulated by the player's own movement. The ball itself takes in the parameters for the player and blocks class to make the game function easier.

Blocks are created first with through having a nested loop, accounting for the rows and columns of the screen, and will draw out a rectangular shape in each columns, then moving onto rows, doing this 4 times in the columns, then  times for the rows.

Color switching, 

Pause originally was going to stop in each of the classes, but decided to use boolean True/False for the player input and grabbing the pause methods from the Ball's Movement.

Reset Game

Audio

Originally I had this feature where the user can resize the window of the game, but in the end I decided to remove it due to complications with adjusting the size of the other objects such as the player.