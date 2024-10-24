import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Draw Rectangle with Mouse")
screen.fill((127, 127, 127))

x = y = 0
w = h = 0
drawmode = True
running = True
rect = None

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            drawmode = True
        elif event.type == MOUSEBUTTONUP:
            x1, y1 = pygame.mouse.get_pos()
            w = x1 - x
            h = y1 - y
            drawmode = False
            rect = pygame.Rect(x, y, w, h)

    if not drawmode and rect:
        screen.fill((127, 127, 127))
        pygame.draw.rect(screen, (255, 0, 0), rect)
    pygame.display.flip()

pygame.quit()