import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Draw 3 Circles")

# Define colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
bg = (127, 127, 127)  # Background color (gray)

# Main loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Fill the screen with the background color
    screen.fill(bg)

    # Draw three circles with different radii and colors
    pygame.draw.circle(screen, red, (200, 150), 60, 2)   # Red circle
    pygame.draw.circle(screen, green, (200, 150), 80, 2) # Green circle
    pygame.draw.circle(screen, blue, (200, 150), 100, 2) # Blue circle

    # Update the display
    pygame.display.update()

# Save the screen as an image after exiting the loop
pygame.image.save(screen, "circle.png")

# Quit Pygame
pygame.quit()
