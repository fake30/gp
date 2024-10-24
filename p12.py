import pygame
import time
import random

# Game settings
speed_of_snake = 8
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 460

# Colors
midnight_blue = pygame.Color(25, 25, 112)
mint_cream = pygame.Color(245, 255, 250)
crimson_red = pygame.Color(220, 20, 60)
lawn_green = pygame.Color(124, 252, 0)
orange_red = pygame.Color(255, 69, 0)

# Initialize the game
pygame.init()
display_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SNAKE')
game_clock = pygame.time.Clock()

# Snake settings
position_of_snake = [100, 50]
body_of_snake = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Fruit settings
position_of_fruit = [
    random.randrange(1, (SCREEN_WIDTH // 10)) * 10,
    random.randrange(1, (SCREEN_HEIGHT // 10)) * 10
]
spawning_of_fruit = True

# Initial direction
initial_direction = 'RIGHT'
snake_direction = initial_direction
player_score = 0

# Display score
def display_score(choice, font_color, font_style, font_size):
    score_font_style = pygame.font.SysFont(font_style, font_size)
    score_surface = score_font_style.render('Your Score: ' + str(player_score), True, font_color)
    score_rectangle = score_surface.get_rect()
    display_screen.blit(score_surface, score_rectangle)

# Game over function
def game_over():
    game_over_font_style = pygame.font.SysFont('times new roman', 50)
    game_over_surface = game_over_font_style.render('Your Score is: ' + str(player_score), True, crimson_red)
    game_over_rectangle = game_over_surface.get_rect()
    game_over_rectangle.midtop = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
    display_screen.blit(game_over_surface, game_over_rectangle)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Game loop
game_run = True
while game_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_direction = 'UP'
            if event.key == pygame.K_DOWN:
                snake_direction = 'DOWN'
            if event.key == pygame.K_LEFT:
                snake_direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                snake_direction = 'RIGHT'

    # Validate the movement
    if snake_direction == 'UP' and initial_direction != 'DOWN':
        initial_direction = 'UP'
    if snake_direction == 'DOWN' and initial_direction != 'UP':
        initial_direction = 'DOWN'
    if snake_direction == 'LEFT' and initial_direction != 'RIGHT':
        initial_direction = 'LEFT'
    if snake_direction == 'RIGHT' and initial_direction != 'LEFT':
        initial_direction = 'RIGHT'

    # Update snake position
    if initial_direction == 'UP':
        position_of_snake[1] -= 10
    if initial_direction == 'DOWN':
        position_of_snake[1] += 10
    if initial_direction == 'LEFT':
        position_of_snake[0] -= 10
    if initial_direction == 'RIGHT':
        position_of_snake[0] += 10

    # Growing the snake
    body_of_snake.insert(0, list(position_of_snake))
    if position_of_snake[0] == position_of_fruit[0] and position_of_snake[1] == position_of_fruit[1]:
        player_score += 1
        spawning_of_fruit = False
    else:
        body_of_snake.pop()

    # Respawn fruit if eaten
    if not spawning_of_fruit:
        position_of_fruit = [
            random.randrange(1, (SCREEN_WIDTH // 10)) * 10,
            random.randrange(1, (SCREEN_HEIGHT // 10)) * 10
        ]
        spawning_of_fruit = True

    # Fill the background
    display_screen.fill(mint_cream)

    # Draw snake
    for position in body_of_snake:
        pygame.draw.rect(display_screen, lawn_green, pygame.Rect(position[0], position[1], 10, 10))

    # Draw fruit
    pygame.draw.rect(display_screen, orange_red, pygame.Rect(position_of_fruit[0], position_of_fruit[1], 10, 10))

    # Check for boundaries collision
    if position_of_snake[0] < 0 or position_of_snake[0] > SCREEN_WIDTH - 10:
        game_over()
    if position_of_snake[1] < 0 or position_of_snake[1] > SCREEN_HEIGHT - 10:
        game_over()

    # Check for self-collision
    for block in body_of_snake[1:]:
        if position_of_snake[0] == block[0] and position_of_snake[1] == block[1]:
            game_over()

    # Display the score
    display_score(1, midnight_blue, 'times new roman', 20)

    # Update the display
    pygame.display.update()

    # Control the speed of the snake
    game_clock.tick(speed_of_snake)

# Quit the game
pygame.quit()
