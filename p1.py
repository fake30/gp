import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello world")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            print(key, "key is pressed")
        elif event.type == pygame.KEYUP:
            key = pygame.key.name(event.key)
            print(key, "key is released")
