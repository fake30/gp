import pygame
from pygame.locals import *
from sys import exit

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving with Mouse")

# Load the image (assuming you have a 'player.png' in the same directory)
img = pygame.image.load('player.png')

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Get mouse position
    mx, my = pygame.mouse.get_pos()

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Draw the image at the mouse position
    screen.blit(img, (mx, my))

    # Update the display
    pygame.display.update()
