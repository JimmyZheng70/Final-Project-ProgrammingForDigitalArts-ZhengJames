import pygame
# TODO: Create a player rectangle at the bottom, allow player to control that rectangle, finish the resizability of the game, and anything else this week.

class Player():
    def __init__(self):
        pass

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