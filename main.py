import pygame
import sys
import random
import time


pygame.init()
pygame.mixer.init()
# pozadi_hudba = pygame.mixer.Sound("assets\hudba\pozadi_hudba.wav")
sirka, vyska = 1600, 900
screen = pygame.display.set_mode((sirka, vyska)) # nastavení velikosti okna
pozadi = pygame.image.load("assets/background_krbec.jpg") # nahrání pozadí 
obrazky_2 = []
nasobek = 1
jeho_projekty = 0
count = 0


obrazky = []

def list_obrazku(slozka, pocet_obrazku):
    global obrazky
    global obrazky_2

    # počet obrázků je číslo kolik obrázků je v složce :) 
    for pocet in range(pocet_obrazku):
        # print(f"assets\{slozka}\cislo{pocet}.png") na kontrolu cesty
        obrazek = pygame.image.load(f"assets\{slozka}\cislo{pocet}.png")
        obrazek = pygame.transform.scale(obrazek, (sirka, vyska))
        obrazky.append(obrazek)
        for i in range(0, pocet_obrazku-1):
            obrazky_mensi = pygame.transform.scale(pygame.image.load(f"assets/{slozka}/cislo{i}.png"), (300, 300))
            obrazky_2.append(obrazky_mensi)
    return obrazky_2 #vrací seznam s adresami obrázků pro další použítí






print(obrazky)


def animace(pocet_obrazku, poloha_x, poloha_y):
    for cislo in range(pocet_obrazku):
        snimek = obrazky_2[cislo]
        screen.blit(pozadi,(0,0))

        snimek_rect = snimek.get_rect()
        snimek_rect.midbottom = (poloha_x, poloha_y) 
        screen.blit(snimek, snimek_rect)
        pygame.display.update()
        time.sleep(0.2)

screen.blit(pozadi, (0, 0))
# pygame.draw.rect(screen, (255, 255, 100), (145, 210, 170, 500), 0) #hlava pana krbce ohraniceni - pro klikani

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(event.pos)

            if event.pos[0] > 145 and event.pos[0] < 300 and event.pos[1] > 210 and event.pos[1] < 730:
                # print("vevnitr", event.pos) tohle bylo použito k určení rozměrů, kde se nachází postava pana krbce

                jeho_projekty += 1 * nasobek
                print(jeho_projekty)
                animace(len(list_obrazku("animace_hlavniho_obrazku", 15)), 700, 300)
               

    pygame.display.flip()