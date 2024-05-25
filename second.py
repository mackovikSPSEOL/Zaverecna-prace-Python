import pygame
import sys

pygame.init()
width, height = 1600, 900
screen = pygame.display.set_mode((width, height))
pozadi = pygame.image.load("assets/background_krbec.jpg")

def animace_obrazku(slozka):
    obrazky = []
    pocet_obrazku = 15
    for pocet in range(pocet_obrazku):
        obrazek = pygame.image.load(f"assets/{slozka}/cislo{pocet}.png")
        obrazek = pygame.transform.scale(obrazek, (width, height))
        obrazky.append(obrazek)
    return obrazky

animace_hlavy = animace_obrazku("animace_hlavniho_obrazku")
index_animace = 0
rect_animace = animace_hlavy[0].get_rect(topleft=(0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect_animace.collidepoint(event.pos):
                index_animace += 1
                if index_animace >= len(animace_hlavy):
                    index_animace = 0
                rect_animace = animace_hlavy[index_animace].get_rect(topleft=(0, 0))
    screen.blit(pozadi, (0, 0))
    screen.blit(animace_hlavy[index_animace], (0, 0))

    pygame.display.flip()