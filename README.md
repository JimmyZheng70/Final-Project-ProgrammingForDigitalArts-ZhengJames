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

The Ball 

Blocks

Color switching, 

The game also allows to resize the screen