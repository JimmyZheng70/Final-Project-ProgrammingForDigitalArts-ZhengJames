import pygame

def main():
    pygame.init()
    pygame.display.set_caption("Final Project")

    smallscreen = (800, 600)
    fullscreen = (1920, 1080)
    screen = pygame.display.set_mode(smallscreen, pygame.RESIZABLE)

    running = True
    while running:
        pass
    pygame.quit()

if __name__ == "__main__":
    main()