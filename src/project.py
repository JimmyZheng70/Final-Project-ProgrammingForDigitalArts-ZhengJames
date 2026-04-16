import pygame
# TODO: Create the Ball and its mechanics, cretae blocks and make them be destroyed, plus anything else if enough time.

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
    
    def move_left(self):
        self.direction = 0
        self.shape.x -= self.speed
        self.direction = -1

        # Stop player from going out of bounds
        if self.shape.left < 0:
            self.shape.left = 0

    def move_right(self):
        self.direction = 0
        self.shape.x += self.speed
        self.direction = 1

        if self.shape.right > self.screen.get_width():
            self.shape.right = self.screen.get_width()
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.shape)

class Ball():
    def __init__(self, x, y, screen, color=(255, 0, 255)):
        # Ball Measurements
        self.radius = 13
        self.center = (self.radius, self.radius)
        self.speed = 15 # Speed of Ball
        self.direction = 0 # Direction of the ball moving
        self.color = color # Color of ball, future code will need to chnage the color
        self.screen = screen
        self.x = x
        self.y = y

    def update(self):
        self.movement()

    def movement(self):
        pygame.draw.circle(self.screen, self.color, [self.x, self.y], self.radius)
        self.x -= self.speed
        self.y -= self.speed

    def bounce(self):
        pass

def main():
    pygame.init()
    pygame.display.set_caption("Final Project")

    clock = pygame.time.Clock()
    dt = 0

    smallscreen = (800, 700)
    fullscreen = (1920, 1080)
    screen = pygame.display.set_mode(smallscreen, pygame.RESIZABLE)

    player = Player(screen)
    ball = Ball(350, 650, screen)

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_left()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.move_right()
        
        player.draw()
        ball.update()
        pygame.display.update()

        dt = clock.tick(20)
    pygame.quit()

if __name__ == "__main__":
    main()