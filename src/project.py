import pygame
# TODO: Gain points when destroying the ball
# Set up death if the ball goes out of bounds under the player
# Make a color switch of the ball whenever the ball hits the player
# Make players switch their colors input
# Resize the ball and player to match the large screen
# Make bounce of player more interesting

# Player
class Player():
    def __init__(self, screen, pink=(255, 0, 255), blue=(15, 10, 255)):
        self.height = 10
        self.width = 100
        self.x = 300
        self.y = screen.get_height() - 40
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height) # Creates the shape of the player
        self.speed = 20
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

# Ball
class Ball():
    def __init__(self, x, y, screen, player, block, pink=(255, 0, 255), blue=(15, 10, 255)):
        # Ball Measurements
        self.radius = 13
        self.speed_x = 15 # Speed of Ball in X directions
        self.speed_y = 15 # Speed of Ball in Y directions
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
        # Get references from other classes
        self.player = player
        self.block = block
        self.score = 0
        self.scorefont = pygame.font.SysFont(None, 12)
        self.gameover = False

    # Update Method to run the Ball
    def update(self):
        self.ball_color()
        self.draw()
        self.movement()
        self.scoreboard(score=0)
        return self.gameover

    def ball_color(self):
        if self.is_pink == True:
            self.color = self.pink
        elif self.is_blue == True:
            self.color = self.blue

    # Movement of the Ball
    def movement(self):
        # If it hits the wall, bounces out.
        if self.ball.left < 0:
            self.speed_x *= -1
        elif self.ball.right > self.screen.get_width():
            self.speed_x *= -1
        elif self.ball.top < 0:
            self.speed_y *= -1
        elif self.ball.bottom > self.screen.get_height():
            self.gameover = True
        
        # Bounces off the player if in contact, Color Switch potential later.
        if self.ball.colliderect(self.player.shape):
            # If the color of player does not match with the ball, kills the player.
            if self.is_pink == True:
                self.is_pink = False
                self.is_blue = True
            elif self.is_blue == True:
                self.is_blue = False
                self.is_pink = True
            self.speed_y *= -1

        # Checks collision with Blocks
        for block in self.block.block[:]:
            if self.ball.colliderect(block):
                self.speed_y *= -1
                self.block.block.remove(block)
                self.score += 100 # Add points for score

        # Ball Movement Calculations
        self.ball.x -= self.speed_x
        self.ball.y -= self.speed_y

    # Drawing the Ball on the screen
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.ball.x + self.radius, self.ball.y + self.radius), self.radius)
    
    # Scoreboard on the screen.
    def scoreboard(self, score=0):
        score = self.score
        return score

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

# MAIN
def main():
    pygame.init()
    pygame.display.set_caption("Final Project")

    clock = pygame.time.Clock()
    dt = 0

    # Screens
    smallscreen = (800, 700)
    fullscreen = (1920, 1080)
    screen = pygame.display.set_mode(smallscreen, pygame.RESIZABLE)

    # Classes
    player = Player(screen)
    block = Blocks(screen)
    ball = Ball(350, 630, screen, player, block)

    is_fullscreen = False
    running = True
    change_color = 1
    game_over = False
    score = 0
    # Running the Game
    while running:
        screen.fill((0, 0, 0)) # Fills the game as black background
        for event in pygame.event.get(): # For exiting or resizing the game.
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE and is_fullscreen == False:
                is_fullscreen = True
                # If chanegd to fullsize, then also adjust the screens for the Ball, Blocks, and Player
                screen = pygame.display.set_mode(fullscreen, pygame.RESIZABLE)
            elif event.type == pygame.VIDEORESIZE and is_fullscreen == False:
                is_fullscreen = False
                screen = pygame.display.set_mode(smallscreen, pygame.RESIZABLE) # Fix later
            
        # Movement
        key = pygame.key.get_pressed()
        direction_input = 0
        if key[pygame.K_LEFT]:
            direction_input = -1 # Goes Left
        elif key[pygame.K_RIGHT]:
            direction_input = 1 # Goes Right
        
        if key[pygame.K_SPACE]:
            change_color *= -1
        
        # Update
        if game_over == False:
            player.update(direction_input, change_color)
            game_over = ball.update()
        else:
            player.draw()

        block.update()

        font = pygame.font.SysFont(None, 56)
        text = font.render("Score: " + str(score), True, (0, 255, 0))
        screen.blit(text, (130, 255))

        pygame.display.update()

        dt = clock.tick(20)
    pygame.quit() # Stops the game when player leaves

if __name__ == "__main__":
    main()