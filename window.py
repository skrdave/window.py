import pygame,sys
from pygame.locals import QUIT

pygame.init()
screen =pygame.display.set_mode((600,600))
pygame.display.set_caption("Helllo world!")

screen.fill((25,77,197))



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()