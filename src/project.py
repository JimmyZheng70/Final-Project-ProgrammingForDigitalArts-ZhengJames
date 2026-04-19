import pygame
# TODO: Create the Ball and its mechanics, cretae blocks and make them be destroyed, resize the ball and player to match the large screen

class Player():
    def __init__(self, screen, color=(255, 0, 255)):
        self.height = 10
        self.width = 100
        self.x = 300
        self.y = screen.get_height() - 40
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 20
        self.direction = 0
        self.screen = screen
        self.color = color # Change later to make it change color
    
    def update(self,direction=0):
        self.movement(direction)
        self.draw()

    def movement(self, direction=0):
        self.direction = direction
        if self.direction == -1:
            self.shape.x -= self.speed
        elif self.direction == 1:
            self.shape.x += self.speed

        # Stop player from going out of bounds
        if self.shape.left < 0:
            self.shape.left = 0
        if self.shape.right > self.screen.get_width():
            self.shape.right = self.screen.get_width()

        self.shape.y = self.screen.get_height() - 40
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.shape)

class Ball():
    def __init__(self, x, y, screen, color=(255, 0, 255)):
        # Ball Measurements
        self.radius = 13
        self.speed_x = 15 # Speed of Ball
        self.speed_y = 15
        self.direction = 0 # Direction of the ball moving
        self.color = color # Color of ball, future code will need to chnage the color
        self.screen = screen
        self.x = x
        self.y = y
        self.ball = pygame.Rect(self.x, self.y, self.radius, self.radius)

    def update(self):
        self.draw()
        self.movement()

    def movement(self):
        if self.ball.left < 0:
            self.speed_x *= -1
        elif self.ball.right > self.screen.get_width():
            self.speed_x *= -1
        elif self.ball.top < 0:
            self.speed_y *= -1
        elif self.ball.bottom < 0:
            pass # Make Game Over When hit

        self.ball.x -= self.speed_x
        self.ball.y -= self.speed_y

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.ball.x + self.radius, self.ball.y + self.radius), self.radius)

class Blocks():
    def __init__(self):
        self.width = 20
        self.height = 10
        self.color = (255, 255, 255)

    def update(self):
        self.make_block()
        self.draw()

    def make_block(self):
        self.block = []

        block = []
    
    def draw(self):
        pygame.draw.rect(self.width, self.height, self.width, self.height)

def main():
    pygame.init()
    pygame.display.set_caption("Final Project")

    clock = pygame.time.Clock()
    dt = 0

    smallscreen = (800, 700)
    fullscreen = (1920, 1080)
    screen = pygame.display.set_mode(smallscreen, pygame.RESIZABLE)

    player = Player(screen)
    ball = Ball(350, 630, screen)
    block = Blocks()

    is_fullscreen = False
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE and is_fullscreen == False:
                is_fullscreen = True
                screen = pygame.display.set_mode(fullscreen, pygame.RESIZABLE)
            elif event.type == pygame.VIDEORESIZE and is_fullscreen == False:
                is_fullscreen = False
                screen = pygame.display.set_mode(smallscreen, pygame.RESIZABLE) # Fix later
            
        # Movement
        key = pygame.key.get_pressed()
        direction_input = 0
        if key[pygame.K_LEFT]:
            direction_input = -1
        elif key[pygame.K_RIGHT]:
            direction_input = 1
        
        player.update(direction_input)
        ball.update()
        block.update()
        pygame.display.update()

        dt = clock.tick(20)
    pygame.quit()

if __name__ == "__main__":
    main()