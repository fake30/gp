import pygame

pygame.init()

# Set up display
screen = pygame.display.set_mode((400, 300))
done = False

# Define colors
white = (255, 255, 255)
bg = (127, 127, 127)

# Main loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Fill the background
    screen.fill(bg)

    # Set font and render text
    font = pygame.font.SysFont("Arial", 36)
    txtsurf = font.render("Hello, World", True, white)

    # Blit the text in the center of the screen
    screen.blit(txtsurf, (200 - txtsurf.get_width() // 2, 150 - txtsurf.get_height() // 2))

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
