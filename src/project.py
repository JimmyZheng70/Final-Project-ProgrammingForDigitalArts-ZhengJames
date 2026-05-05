import pygame
# TODO: 
# Resize the ball and player to match the large screen

# Player
class Player():
    def __init__(self, screen, pink=(255, 0, 255), blue=(15, 10, 255)):
        self.height = 10
        self.width = 100
        self.x = 300
        self.y = screen.get_height() - 40
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height) # Creates the shape of the player
        self.speed = 30
        self.direction = 0 # -1 for left and 1 for right
        self.screen = screen # get the screen of the game
        self.color = None # Change later to make it change color
        self.pink = pink
        self.blue = blue
        self.change_color = 1
    
    # Call this in main to run Player class
    def update(self,direction=0, player_color=1):
        self.player_color(player_color)
        self.movement(direction)
        self.draw()

    # Switches player's color
    def player_color(self, player_color=1):
        self.change_color = player_color
        if self.change_color == 1:
            self.color = self.pink
        elif self.change_color == -1:
            self.color = self.blue
    
    # Define Movement of the Player
    def movement(self, direction=0):
        self.direction = direction
        if self.direction == -1:
            self.shape.x -= self.speed # Moves Left
        elif self.direction == 1:
            self.shape.x += self.speed # Move Right

        # Stop player from going out of bounds
        if self.shape.left < 0:
            self.shape.left = 0 # Left Out of Bounds
        if self.shape.right > self.screen.get_width():
            self.shape.right = self.screen.get_width() # Right Out of Bounds

        self.shape.y = self.screen.get_height() - 40 # Set the Player near the bottom of the screen
    
    # Draws out the Player model
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.shape)

    # Reset Player's position and color
    def reset(self):
        self.shape.x = self.x
        self.change_color = 1

# Ball
class Ball():
    def __init__(self, x, y, screen, player, block, max_score=0, pink=(255, 0, 255), blue=(15, 10, 255)):
        # Ball Measurements
        self.radius = 13
        self.speed_x = 20 # Speed of Ball in X directions
        self.speed_y = 20 # Speed of Ball in Y directions
        self.max_speed = 20
        self.origin_speed_x = 0 # Store the original speed of ball, x
        self.origin_speed_y = 0 # Store the original speed of ball, y
        self.direction = 0 # Direction of the ball moving
        self.color = None # Color of ball, future code will need to chnage the color
        self.pink = pink
        self.blue = blue
        self.is_pink = True
        self.is_blue = False
        self.screen = screen
        self.x = x
        self.y = y
        self.ball = pygame.Rect(self.x, self.y, self.radius, self.radius) # The Ball's Shape
        self.player = player # Referenc to Player class
        self.block = block # Reference to Block class
        self.score = 0
        self.max_score = max_score
        self.gameover = False

    # Update Method to run the Ball
    def update(self):
        self.ball_color()
        self.draw()
        self.movement()
        self.scoreboard(score=0)
        return self.gameover

    # Setting the Ball to default Pink and siwtches color to blue otherwise
    def ball_color(self):
        if self.is_pink == True:
            self.color = self.pink
        elif self.is_blue == True:
            self.color = self.blue

    # Movement of the Ball
    def movement(self):
        collision_thresh = 7
        # If it hits the wall, bounces out.
        if self.ball.left < 0:
            self.speed_x *= -1
            self.color_switch()
        elif self.ball.right > self.screen.get_width():
            self.speed_x *= -1
            self.color_switch()
        elif self.ball.top < 0:
            self.speed_y *= -1
            self.color_switch()
        elif self.ball.bottom > self.screen.get_height(): # Game Over if it hits the bottom
            self.gameover = True
        
        # Bounces off the player if in contact
        if self.ball.colliderect(self.player.shape):
            # If the color of player does not match with the ball, kills the player.
            if self.is_pink == True and self.player.change_color == -1:
                self.gameover = True
            elif self.is_blue == True and self.player.change_color == 1:
                self.gameover = True
            
            self.color_switch() # Siwtches color of ball when bounced

            # Enables the ball to feel more different depending on the movement of the pk]layer when colliding.
            if abs(self.ball.bottom - self.player.shape.top) < collision_thresh and self.speed_y < 0:
                self.speed_y *= -1
                self.speed_x += self.player.direction
                if self.speed_x > self.max_speed:
                    self.speed_x = self.max_speed

        # Checks collision with Blocks
        for block in self.block.block[:]:
            if self.ball.colliderect(block):
                self.color_switch()
                self.speed_y *= -1
                self.block.block.remove(block)
                self.score += 10 # Add points for score
                self.max_score += 10

        # Ball Movement Calculations
        self.ball.x -= self.speed_x
        self.ball.y -= self.speed_y

    # Called to switch the color of the Ball
    def color_switch(self):
        if self.is_pink == True:
            self.is_pink = False
            self.is_blue = True
        elif self.is_blue == True:
            self.is_blue = False
            self.is_pink = True

    # Drawing the Ball on the screen
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.ball.x + self.radius, self.ball.y + self.radius), self.radius)
    
    # Scoreboard on the screen.
    def scoreboard(self, score=0):
        score = self.score
        return score
    
    # Reset the Ball and the scoreboard
    def reset(self):
        if self.gameover:
            self.gameover = False
            self.ball.x = 350
            self.ball.y = 630
            self.speed_x = self.max_speed
            self.speed_y = self.max_speed
            self.is_blue = False
            self.is_pink = True
            self.score -= self.score
    
    # Stop the movement of the ball, and also store the data which direction the ball was going
    def pause(self):
        self.origin_speed_x = self.speed_x
        self.origin_speed_y = self.speed_y
        self.speed_x = 0
        self.speed_y = 0

    # Return to original direction and speed of the ball
    def unpause(self):
        self.speed_x = self.origin_speed_x
        self.speed_y = self.origin_speed_y
    
    # Starts New level, resetting ball to origin
    def next_level(self):
        self.ball.x = 350
        self.ball.y = 630
        self.speed_x = self.max_speed
        self.speed_y = self.max_speed
        self.is_blue = False
        self.is_pink = True

# Blocks
class Blocks():
    def __init__(self, screen):
        # Get the Blocks height and width, plus gaps to seperate them.
        self.width = 200
        self.height = 35
        self.gap = 8
        self.color = (255, 255, 255)
        self.cols = 7
        self.rows = 7
        self.block = [] # The blocks made to put into a list
        self.screen = screen
        self.make_block() # Makes the Block once when run
        self.shape = pygame.Rect()

    def update(self): # Create the Blocks on the screen
        self.draw()

    # Create the blocks and place them into a list for later use
    def make_block(self):
        for row in range(self.rows):
            for col in range(self.cols):
                block_x = col * (self.width + self.gap)
                block_y = row * (self.height + self.gap)
                self.shape = pygame.Rect(block_x, block_y, self.width, self.height)
                self.block.append(self.shape)
    
    # Draw out the ball
    def draw(self):
        for block in self.block:
            pygame.draw.rect(self.screen, self.color, block)
    
    # Reset blocks
    def reset(self):
        self.block = []
        self.make_block()

# MAIN
def main():
    pygame.init()
    pygame.display.set_caption("Final Project")

    clock = pygame.time.Clock()
    dt = 0

    # Screens
    smallscreen = (800, 700)
    fullscreen = (1920, 1080) ## MAY DELETE
    screen = pygame.display.set_mode(smallscreen, pygame.RESIZABLE) ### MAY DELETE

    # Classes
    player = Player(screen)
    block = Blocks(screen)
    ball = Ball(350, 630, screen, player, block)

    # Gameover text/font
    gameover_font = pygame.font.SysFont(None, 80)
    gameover_text = gameover_font.render("GAME OVER", True, (255, 0, 0))

    # Restart text/font
    restart_font = pygame.font.SysFont(None, 40)
    restart_text = restart_font.render("Press 'r' to Restart", True, (255, 0, 0))
    
    # Pause Text/Font
    pause_font = pygame.font.SysFont(None, 150)
    pause_text = pause_font.render("PAUSE", True, (0, 255, 0))

    # Variables
    is_fullscreen = False
    running = True
    change_color = 1
    game_over = False
    score = 0
    level = 1
    max_score_block = 0
    pause = False

    # Running the Game
    while running:
        screen.fill((0, 0, 0)) # Fills the game as black background

        # Pressing Key Once
        for event in pygame.event.get(): # For exiting or resizing the game.
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE and is_fullscreen == False: ##### MAY DELETE
                is_fullscreen = True
                # If chanegd to fullsize, then also adjust the screens for the Ball, Blocks, and Player
                screen = pygame.display.set_mode(fullscreen, pygame.RESIZABLE)
                player.screen = screen
                ball.screen = screen
                block.screen = screen
            elif event.type == pygame.VIDEORESIZE and is_fullscreen == False:
                is_fullscreen = False
                screen = pygame.display.set_mode(smallscreen, pygame.RESIZABLE) # Fix later
                player.screen = screen
                ball.screen = screen
                block.screen = screen
            
            # Player Inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and pause == False: # Change Player colors
                    change_color *= -1
                elif game_over and event.key == pygame.K_r: # Reset Game if player is dead
                    game_over = False
                    change_color = 1
                    score -= score
                    ball.reset()
                    player.reset()
                    block.reset()
                elif event.key == pygame.K_p and game_over == False: # Pause game
                    if pause == False:
                        pause = True
                        ball.pause()
                    else:
                        pause = False
                        ball.unpause()

        # Hold Key Down
        # Movement
        key = pygame.key.get_pressed()
        direction_input = 0
        if pause == False:
            if key[pygame.K_LEFT] or key[pygame.K_a]:
                direction_input = -1 # Goes Left
            elif key[pygame.K_RIGHT] or key[pygame.K_d]:
                direction_input = 1 # Goes Right
        
        # Update
        if game_over == False:
            player.update(direction_input, change_color)
            game_over = ball.update()
            score = ball.scoreboard(score)
        else:
            player.draw()

        block.update() # Updates the blocks

        # ScoreBoard UI
        score_font = pygame.font.SysFont(None, 30)
        score_text = score_font.render("Score: " + str(score), True, (0, 255, 0))
        screen.blit(score_text, (screen.get_width()//2+250, screen.get_height()//1.2+90))

        # Level Number UI
        level_font = pygame.font.SysFont(None, 30)
        level_text = level_font.render("Score: " + str(level), True, (0, 255, 0))
        screen.blit(level_text, (screen.get_width()//2-250, screen.get_height()//1.2+90))

        # Game Over UI
        if game_over == True:
            screen.blit(gameover_text, (screen.get_width()//2-176, screen.get_height()//2)) # Fix Position
            screen.blit(restart_text, (screen.get_width()//2-120, screen.get_height()//2+55))
        
        # Pause UI
        if pause == True:
            screen.blit(pause_text, (screen.get_width()//2-176, screen.get_height()//2))

        max_score_block = ball.max_score

        if max_score_block >= 280:
            print("Next Level")
            print(max_score_block)
            ball.max_score = 0
            ball.next_level()
            block.reset()
            player.reset()
            level += 1

        pygame.display.update()

        dt = clock.tick(20)
    pygame.quit() # Stops the game when player leaves

if __name__ == "__main__":
    main()