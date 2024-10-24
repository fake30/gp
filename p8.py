import pygame
from pygame.locals import *
from sys import exit

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Move Rectangle with Keyboard")

# Initialize the rectangles
rect1 = pygame.Rect(50, 60, 200, 80)  # Static red rectangle
rect2 = rect1.copy()  # Blue rectangle to be moved

# Control loop
running = True
x = 0
y = 0

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        # Check for key presses
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                x = -5
                y = 0
            elif event.key == K_RIGHT:
                x = 5
                y = 0
            elif event.key == K_UP:
                x = 0
                y = -5
            elif event.key == K_DOWN:
                x = 0
                y = 5

    # Move rect2 based on x and y values
    rect2.move_ip(x, y)

    # Fill the screen with a gray background
    screen.fill((127, 127, 127))

    # Draw the static red rectangle (rect1)
    pygame.draw.rect(screen, (255, 0, 0), rect1, 1)

    # Draw the moving blue rectangle (rect2)
    pygame.draw.rect(screen, (0, 0, 255), rect2, 5)

    # Update the display
    pygame.display.update()

    # Reset movement after each frame
    x = 0
    y = 0

# Quit Pygame
pygame.quit()
