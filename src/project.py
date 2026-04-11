import pygame
# TODO: Create a player rectangle at the bottom, allow player to control that rectangle, finish the resizability of the game, and anything else this week.

class Player():
    def __init__(self, screen):
        self.height = 5
        self.width = 20
        self.x = 5
        self.y = 5
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 10
        self.direction = 0
        self.screen = screen
    
    def movement(self):
        self.direction = 0
        key = pygame.key.get_pressed()
        if key(pygame.K_LEFT):
            self.shape.x -= self.speed
            self.direction = -1
        elif key(pygame.K_RIGHT):
            self.shape.x += self.speed
            self.direction = 1
    
    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.shape)
        

def main():
    pygame.init()
    pygame.display.set_caption("Final Project")

    smallscreen = (800, 600)
    fullscreen = (1920, 1080)
    screen = pygame.display.set_mode(smallscreen, pygame.RESIZABLE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()