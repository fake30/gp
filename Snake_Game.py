import pygame, random

# Initialize pygame
pygame.init()

# Set up display
size = 400
win = pygame.display.set_mode((size, size))
pygame.display.set_caption("Snake Game")

# Colors
black, green, red = (0, 0, 0), (0, 255, 0), (213, 50, 80)

# Snake settings
clock = pygame.time.Clock()
block_size, speed = 20, 10

# Function to display the snake
def snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(win, green, [block[0], block[1], block_size, block_size])

# Function to display messages
def message(msg, color):
    font_style = pygame.font.SysFont("bahnschrift", 25)
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [size / 6, size / 3])

# The main game function
def game():
    x, y = size // 2, size // 2
    dx, dy = 0, 0
    snake_list, snake_len = [], 1
    food = [random.randrange(0, size - block_size, block_size), random.randrange(0, size - block_size, block_size)]
    running = True
    game_over = False

    while running:
        while game_over:
            win.fill(black)
            message("Game Over! Press C-Play Again or Q-Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                        game_over = False
                    if event.key == pygame.K_c:
                        game()  # Restart the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -block_size, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = block_size, 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -block_size
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, block_size

        x += dx
        y += dy

        # Check if snake hits the boundaries
        if x < 0 or x >= size or y < 0 or y >= size:
            game_over = True

        # Check if snake hits itself
        if [x, y] in snake_list:
            game_over = True

        # Update the snake's position
        snake_list.append([x, y])
        if len(snake_list) > snake_len:
            del snake_list[0]

        # Check if snake eats the food
        if [x, y] == food:
            food = [random.randrange(0, size - block_size, block_size), random.randrange(0, size - block_size, block_size)]
            snake_len += 1

        # Draw everything
        win.fill(black)
        snake(snake_list)
        pygame.draw.rect(win, red, [food[0], food[1], block_size, block_size])
        pygame.display.update()

        clock.tick(speed)

    pygame.quit()

# Start the game
game()
