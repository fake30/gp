import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Image Display")  # Optional: Set a title for the window

# Load the image (use raw string or double backslashes for Windows paths)
img = pygame.image.load(r'C:\Users\HP\Desktop\Game Programing\p4/rahul.jpg')

# Define background color (gray)
bg = (127, 127, 127)

# Main loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Fill the screen with the background color
    screen.fill(bg)

    # Get the rectangle area of the image and center it
    rect = img.get_rect()
    rect.center = (400, 300)

    # Draw the image on the screen
    screen.blit(img, rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
