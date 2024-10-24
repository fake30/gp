import pygame
import random
import math
from pygame import mixer

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Simple 2D Shooting Game")


score_val = 0
font = pygame.font.Font('freesansbold.ttf', 20)
game_over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score: " + str(score_val), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over():
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_text, (250, 250))

player_image = pygame.image.load('player.png')  
player_X = 370
player_Y = 480
player_X_change = 0

enemy_image = []
enemy_X = []
enemy_Y = []
enemy_X_change = []
enemy_Y_change = []
num_of_enemies = 10

for _ in range(num_of_enemies):
    enemy_image.append(pygame.image.load('enemy.png'))  
    enemy_X.append(random.randint(0, 200))
    enemy_Y.append(random.randint(50, 150))
    enemy_X_change.append(1.5)
    enemy_Y_change.append(20)

bullet_image = pygame.image.load('bullet.png')  
bullet_X = 0
bullet_Y = 480
bullet_Y_change = 3
bullet_state = "ready"  

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))
    return distance < 27  
def player(x, y):
    screen.blit(player_image, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_image[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x + 16, y + 10))  

running = True
while running:
    screen.fill((0, 0, 0))  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_X_change = -2
            if event.key == pygame.K_RIGHT:
                player_X_change = 2
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_X = player_X
                    fire_bullet(bullet_X, bullet_Y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_X_change = 0

    player_X += player_X_change
    player_X = max(0, min(player_X, 736))  

    for i in range(num_of_enemies):
        if enemy_Y[i] > 440:
            for j in range(num_of_enemies):
                enemy_Y[j] = 2000  
            game_over()
            break

        enemy_X[i] += enemy_X_change[i]

        if enemy_X[i] <= 0:
            enemy_X_change[i] = 1.5
            enemy_Y[i] += enemy_Y_change[i]
        elif enemy_X[i] >= 736:
            enemy_X_change[i] = -1.5
            enemy_Y[i] += enemy_Y_change[i]

        collision = is_collision(enemy_X[i], enemy_Y[i], bullet_X, bullet_Y)
        if collision:
            bullet_Y = 480  
            bullet_state = "ready"
            score_val += 1
            enemy_X[i] = random.randint(0, 735)
            enemy_Y[i] = random.randint(50, 150)

        enemy(enemy_X[i], enemy_Y[i], i)

    if bullet_Y <= 0:
        bullet_Y = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bullet_X, bullet_Y)
        bullet_Y -= bullet_Y_change

    player(player_X, player_Y)
    show_score(10, 10)
    pygame.display.update()  
