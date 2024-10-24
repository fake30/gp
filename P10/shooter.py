import random
import pygame
import sys

# Constants
WIDTH = 600
HEIGHT = 800
MAX_BULLETS = 3

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Variables
level = 1
lives = 3
score = 0
animation_frame = 0
frame_delay = 10
frame_counter = 0

class Actor(pygame.sprite.Sprite):
    def __init__(self, image_name, pos=(0, 0)):
        super().__init__()
        self.image = pygame.image.load(image_name + ".png")
        self.rect = self.image.get_rect(topleft=pos)
        self.vx = 1  # Velocity in x direction
        self.vy = 2  # Velocity in y direction

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def colliderect(self, other):
        return self.rect.colliderect(other.rect)

# Load assets
background = Actor("background")
player = Actor("player", (200, 580))
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
bombs = pygame.sprite.Group()

def draw():
    screen.fill((0, 0, 0))
    background.draw(screen)
    player.draw(screen)
    enemies.draw(screen)
    bullets.draw(screen)
    bombs.draw(screen)
    draw_text()
    pygame.display.flip()

def update(delta):
    global frame_counter
    frame_counter += 1
    if frame_counter >= frame_delay:
        frame_counter = 0
        update_animation_frames()

    move_player()
    move_bullets()
    move_enemies()
    create_bombs()
    move_bombs()
    check_for_end_of_level()

def move_player():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player.move(5, 0)
    if keys[pygame.K_LEFT]:
        player.move(-5, 0)
    if player.rect.x > WIDTH:
        player.rect.x = WIDTH
    if player.rect.x < 0:
        player.rect.x = 0

def move_enemies():
    global score
    enemies_to_remove = []
    bullets_to_remove = []
    for enemy in enemies:
        enemy.move(enemy.vx, 0)
        if enemy.rect.x > WIDTH or enemy.rect.x < 0:
            enemy.vx = -enemy.vx
            enemy.image = pygame.image.load("enemy2.png") if enemy.image.get_at((0, 0)) == pygame.image.load("enemy1.png").get_at((0, 0)) else pygame.image.load("enemy1.png")

        for bullet in bullets:
            if bullet.colliderect(enemy):
                enemies_to_remove.append(enemy)
                bullets_to_remove.append(bullet)
                score += 1

    for enemy in enemies_to_remove:
        enemies.remove(enemy)
    for bullet in bullets_to_remove:
        bullets.remove(bullet)

    for enemy in enemies:
        if enemy.colliderect(player):
            pygame.quit()
            sys.exit()

def draw_text():
    font = pygame.font.SysFont(None, 36)
    level_text = font.render("Level " + str(level), True, (255, 0, 0))
    score_text = font.render("Score " + str(score), True, (255, 0, 0))
    lives_text = font.render("Lives " + str(lives), True, (255, 0, 0))

    screen.blit(level_text, (0, 0))
    screen.blit(score_text, (100, 0))
    screen.blit(lives_text, (200, 0))

def on_key_down(event):
    global bullets
    if event.key == pygame.K_SPACE and len(bullets) < MAX_BULLETS:
        bullet = Actor("bullet", pos=(player.rect.centerx, player.rect.top))
        bullets.add(bullet)

def move_bullets():
    global bullets
    for bullet in list(bullets):
        bullet.move(0, -6)
        if bullet.rect.y < 0:
            bullets.remove(bullet)

def create_bombs():
    if random.randint(0, 100 - level * 6) == 0:
        if len(enemies) > 0:
            enemy = random.choice(enemies.sprites())
            bomb = Actor("bomb", pos=enemy.rect.topleft)
            bombs.add(bomb)

def move_bombs():
    global lives
    for bomb in list(bombs):
        bomb.move(0, 10)
        if bomb.colliderect(player):
            bombs.remove(bomb)
            lives -= 1
            if lives <= 0:
                pygame.quit()
                sys.exit()

def check_for_end_of_level():
    global level
    if len(enemies) == 0:
        level += 1
        create_enemies()

def create_enemies():
    global enemies
    enemies.empty()
    for x in range(0, WIDTH, 60):
        for y in range(0, 200, 60):
            enemy = Actor("enemy1", (x, y))
            enemy.vx = level * 2
            enemies.add(enemy)

def update_animation_frames():
    global animation_frame
    pass

# Game loop
create_enemies()
running = True
while running:
    delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            on_key_down(event)

    update(delta)
    draw()