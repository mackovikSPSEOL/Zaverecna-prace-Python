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
obrazky = [] 
obrazky_2 = []
nasobek = 1
jeho_projekty = 0
count = 0


    


def list_obrazku(slozka, pocet_obrazku):


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

def animace(pocet_obrazku, poloha_x, poloha_y):
    list_obrazku("animace_hlavniho_obrazku", 15)
    for cislo in range(pocet_obrazku):
        snimek = obrazky_2[cislo]
        screen.blit(pozadi,(0,0))

        snimek_rect = snimek.get_rect()
        snimek_rect.midbottom = (poloha_x, poloha_y) 
        screen.blit(snimek, snimek_rect)
        pygame.display.update()
        
        time.sleep(0.1)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

screen.blit(pozadi, (0, 0))
# pygame.draw.rect(screen, (255, 255, 100), (145, 210, 170, 500), 0) #hlava pana krbce ohraniceni - pro klikani

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        
        if event.pos[0] > 145 and event.pos[0] < 300 and event.pos[1] > 210 and event.pos[1] < 730:
                # print("vevnitr", event.pos) tohle bylo použito k určení rozměrů, kde se nachází postava pana krbce
          
            if count == 0:
                after_click_audio = pygame.mixer.Sound("assets/audio/hejhou.mp3").play()
                time.sleep(0.001)
                jeho_projekty += 1 * nasobek
                count -= 1

            print(jeho_projekty)
            animace(14, 700, 700)
            count += 1
            screen.blit(pozadi, (0, 0))           
               

    pygame.display.flip()