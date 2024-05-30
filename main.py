import pygame
import sys
import random
import time
from pygame import draw


pygame.init()
pygame.mixer.init()
pozadi = pygame.image.load("assets/background_krbec.jpg") # nahrání pozadí
pozadi_secret_1 = pygame.image.load("assets/k_animaci\kamna/cislo0.png")
pozadi_secret_2 = pygame.image.load("assets/k_animaci\kamna/cislo1.png")
cesta_k_fontu = "assets/cesta_k_fontu/Ubuntu_Sans_Mono/static/UbuntuSansMono-Bold.ttf"
secret_audio = pygame.mixer.Sound("assets/audio/hello_there.mp3")
secret_audio2 = pygame.mixer.Sound("assets/audio/final_final.mp3")
after_click_audio = pygame.mixer.Sound("assets/audio/hejhou.mp3")
pozadi_hudba = pygame.mixer.Sound("assets/audio/pozadi_hudba.mp3")

sirka, vyska = 1600, 900
obrazky = [] 
obrazky_2 = []
nasobek = 1
jeho_projekty = 0
count = 0
switch = 0
font_text = pygame.font.Font(cesta_k_fontu, 36)
text = font_text.render(f'Jeho projekty: {jeho_projekty}', True, (255, 255, 255))
obchod_text = font_text.render('Obchod', True, (255, 255, 255))
pozadi_secret_1 = pygame.transform.scale(pozadi_secret_1, (sirka, vyska))
pozadi_secret_2 = pygame.transform.scale(pozadi_secret_2, (sirka, vyska))
pozadi_hudba.play(loops=-1)
obchod_button = pygame.Rect(800, 30, 100, 120) 
krbec_button = pygame.Rect(130, 270, 198, 390)



obraz = pygame.display.set_mode((sirka, vyska)) # nastavení velikosti okna

def refresh_obrazu():
    obraz.blit(pozadi, (0, 0))
    obraz.blit(text, (10, 10))
    obraz.blit(obchod_text, (10, 10))
    pygame.draw.rect(obraz, (255, 0, 0), obchod_button)
    pygame.display.flip()



def update_text():
    return font_text.render(f'Jeho projekty: {jeho_projekty}', True, (255, 255, 255))

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
    return obrazky_2 #vrací seznam s adresami obrázků pro další použítí (zárověň menší naformátování)
list_obrazku("animace_hlavniho_obrazku", 15) #načtení obrázků pro animaci

def obchod():
    global jeho_projekty
    global nasobek

    
    refresh_obrazu()

def animace(pocet_obrazku, poloha_x, poloha_y):
    global text
    global snimek
    for cislo in range(pocet_obrazku):
        snimek = obrazky_2[cislo]
        obraz.blit(pozadi,(0,0))
        text = update_text()
        obraz.blit(text, (10, 10))
        snimek_rect = snimek.get_rect()
        snimek_rect.midbottom = (poloha_x, poloha_y) 
        obraz.blit(snimek, snimek_rect)
        pygame.display.update()
        time.sleep(0.1)

    refresh_obrazu()


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        # print(event.pos) kontrola pozic
        if obchod_button.collidepoint(event.pos):  # Pokud bylo kliknuto na tlačítko
            # print("trefa_shop") kontrola pozic
            pozadi_hudba.stop()
            time.sleep(0.5)

        if krbec_button.collidepoint(event.pos):      
            # print("trefa_krbec") kontrola pozic
            after_click_audio.play()
            jeho_projekty += 1 * nasobek
            animace(14, 700, 700)
              
        if event.pos[0] > 5 and event.pos[0] < 100 and event.pos[1] > 783 and event.pos[1] < 890:
            

            
            if switch == 0:
                obraz.blit(pozadi_secret_1, (0, 0))
                pozadi_hudba.stop()
                time.sleep(0.5)
                secret_audio2.play(loops=-1)
                secret_audio.play()
                switch += 1
                for i in range(0, 10):
                    obraz.blit(pozadi_secret_1, (0, 0))
                    pygame.display.flip()
                    time.sleep(0.5)
                    obraz.blit(pozadi_secret_2, (0, 0))
                    pygame.display.flip()
                    time.sleep(0.5)
            else:
                secret_audio2.stop()
                time.sleep(0.2)
                pygame.display.flip()
                switch -= 1
                pozadi_hudba.play(loops=-1)
        refresh_obrazu()