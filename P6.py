import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Key Press Display")

# Define colors
white = (255, 255, 255)
bg = (127, 127, 127)

# Set up font
font = pygame.font.SysFont("Arial", 36)

# To store all pressed keys
pressed_keys = []

# Main loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        # Check for key press events
        if event.type == pygame.KEYDOWN:
            # Add the pressed key to the list
            pressed_keys.append(pygame.key.name(event.key))
    
    # Fill the screen with the background color
    screen.fill(bg)
    
    # Display all pressed keys
    y_offset = 0
    for key in pressed_keys:
        txtsurf = font.render(key, True, white)
        screen.blit(txtsurf, (20, 20 + y_offset))
        y_offset += 40  # Adjust position for the next key
    
    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
