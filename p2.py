import pygame
import sys

pygame.init()

# Set up the display window
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello World")

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print("x={}, y={}".format(pos[0], pos[1]))
