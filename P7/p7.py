import pygame
from pygame.locals import *
from sys import exit

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((700, 600))
pygame.display.set_caption("Moving with Mouse")

# Load the image (use correct path for the image)
img = pygame.image.load("pygame1.jpg")

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Get mouse position
    mx, my = pygame.mouse.get_pos()

    # Fill the screen with white background
    screen.fill((255, 255, 255))

    # Adjust image blitting so the image's center follows the mouse
    img_rect = img.get_rect()
    img_rect.center = (mx, my)

    # Draw the image at the mouse position
    screen.blit(img, img_rect)

    # Update the display
    pygame.display.update()
