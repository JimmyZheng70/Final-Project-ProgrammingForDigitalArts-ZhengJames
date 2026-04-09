# Interactive Breakout Color Switch Game - Final Project

## Repository
https://github.com/JimmyZheng70/Final-Project-ProgrammingForDigitalArts-ZhengJames

## Description
Run a Breakout like game in which the ball bounces off the player and hits the squares, going on infinitely until the player dies. For a twist, the ball is switched to the different colors of red and cyan, and the player must match the color by pressing space or else die if touching the wropng colors.

## Features
- Movement of Player
	- Through keydowns of either the left/right arrows or A/D keys when doing the While Loop.
- Ball Moving
	- Through calling a function for its movements and updating in the while loop.
- Ball Bounce
	- On Collision that makes the ball bounce on walls, blocks, and players.
- Score System/Board
  - Give points whenever the blocks are destroyed in the destroy block function, store those points inside of a variable and call/update the point counter that is displayed during the runtime of the game.
- Destroy Blocks When colliding to ball.
  - Use On Collision and if the ball interacts with the block, destroy that block.
- Switching Player Colors
  - Player Input with using spacebar, switching the colors without any lag.
- Switching Ball Color
  - When the Ball bounces off the Player, siwtches the ball's color.
- Matching Colors when colliding
  - Have if statements in the functions to tell if it is the right color when the player and ball collide, and kill the player if it is not matching colors.
- Reset Level once all blocks are gone.
  - Have a determined count of the blocks and if the block total is equal to zero, reset the blocks and restart the level.
- Game Over
  - Create a game over by pausing all movement and inputs, and stop the game, allowing for the player to restart by pressing a key.

## Challenges
- Finding out how to find the collision of objects in pygame and doing anything with it as well.
- The movement of the ball, in which can go in any direction in a straightline, changing it each time it bounces off a wall.
- Switch between colors of the ball and player, and find a way to tell the code to identify whcih color are either the objects are and determine if the ball is bounced or kills the player.

## Outcomes
Ideal Outcome:
- An ideal outcome of the project is to have the ball move in a straight line/ random direction, and have the ability for it to bounce off walls, blocks, and the player.

Minimal Viable Outcome:
- The minimal outcome is hopefully that the game works and that the player can move at the bare minimum, without restarting the level if things get too complicated.

## Milestones

- Week 1
  1. Research and complete the Brainstorming of the project
  2. Set up pygame and initialize pygame run.
  3. Set up a player model
  4. Have left and right movement of the player.
  5. Set up the read.md and requirements.txt files to update weekly.

- Week 2
  1. Create a Ball.
  2. Have the ball move.
  3. Get the ball to bounce between blocks, walls, and player
  4. Create blocks.
  5. Give collision to blocks and destroy them when hit by ball.
  6. Update anything to the read.md and requirements.txt files.

- Week 3
  1. Gain points when destroying the ball
  2. Set up death if the ball goes out of bounds under the player.
  3. Make a color switch of the ball whenever the ball hits the player.
  4. Make players switch their colors input.
  5. Update anything to the read.md and requirements.txt files.

- Week 4
  1. Have a way for the ball and the player must match colors to be hit, and if not, it leads to death.
  2. Have a scoreboard ui.
  3. Game over screen and option to restart.
  4. When restarting, resets the scoreboard and the blocks.
  5. Pause menu
  6. Add antyhing else such as details.
  7. Update anything to the read.md and requirements.txt files.

- Week 5 (Final)
  1. Fix/Clean code
  2. Record demo
  3. Finish writing the Read.md
  4. Put any lasting imports used in the requirements.txt file