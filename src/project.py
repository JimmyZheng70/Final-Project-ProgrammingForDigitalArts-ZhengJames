import pygame
# TODO: Create a player rectangle at the bottom, allow player to control that rectangle, finish the resizability of the game, and anything else this week.

class Player():
    def __init__(self, screen, color=(0, 0, 255)):
        self.height = 10
        self.width = 100
        self.x = 300
        self.y = screen.get_height() - 30
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 10
        self.direction = 0
        self.screen = screen
        self.color = color # Change later to make it change color
    
    def movement(self):
        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.shape.x -= self.speed
            self.direction = -1
        elif key[pygame.K_RIGHT]:
            self.shape.x += self.speed
            self.direction = 1

        # Stop player from going out of bounds
        if self.shape.left < 0:
            self.shape.left = 0
        if self.shape.right > self.screen.get_width():
            self.shape.right = self.screen.get_width()
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.shape)
        

def main():
    pygame.init()
    pygame.display.set_caption("Final Project")

    clock = pygame.time.Clock()
    dt = 0

    smallscreen = (800, 600)
    fullscreen = (1920, 1080)
    screen = pygame.display.set_mode(smallscreen, pygame.RESIZABLE)

    player = Player(screen)

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
        
        player.movement()
        player.draw()
        pygame.display.update()

        dt = clock.tick(20)
    pygame.quit()

if __name__ == "__main__":
    main()