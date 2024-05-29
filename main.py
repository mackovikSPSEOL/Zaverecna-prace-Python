import pygame
import sys
import random
import time


pygame.init()
pygame.mixer.init()
# pozadi_hudba = pygame.mixer.Sound("assets\hudba\pozadi_hudba.wav")
sirka, vyska = 1600, 900
obraz = pygame.display.set_mode((sirka, vyska)) # nastavení velikosti okna
pozadi = pygame.image.load("assets/background_krbec.jpg") # nahrání pozadí
pozadi_secret_1 = pygame.image.load("assets/k_animaci\kamna/cislo0.png")
pozadi_secret_2 = pygame.image.load("assets/k_animaci\kamna/cislo1.png")
obrazky = [] 
obrazky_2 = []
nasobek = 1
jeho_projekty = 0
count = 0
switch = 0
cesta_k_fontu = "assets/cesta_k_fontu/Ubuntu_Sans_Mono/static/UbuntuSansMono-Bold.ttf"
secret_audio = pygame.mixer.Sound("assets/audio/hello_there.mp3")
secret_audio2 = pygame.mixer.Sound("assets/audio/final_final.mp3")
font_text = pygame.font.Font(cesta_k_fontu, 36)
text = font_text.render(f'Jeho projekty: {jeho_projekty}', True, (255, 255, 255))

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
    return obrazky_2 #vrací seznam s adresami obrázků pro další použítí



def animace(pocet_obrazku, poloha_x, poloha_y):
    global text
    for cislo in range(pocet_obrazku):
        snimek = obrazky_2[cislo]
        obraz.blit(pozadi,(0,0))
        obraz.blit(text, (10, 10))
        text = update_text()
        snimek_rect = snimek.get_rect()
        snimek_rect.midbottom = (poloha_x, poloha_y) 
        obraz.blit(snimek, snimek_rect)
        pygame.display.update()
        time.sleep(0.1)

obraz.blit(pozadi, (0, 0))
pozadi_secret_1 = pygame.transform.scale(pozadi_secret_1, (sirka, vyska))
pozadi_secret_2 = pygame.transform.scale(pozadi_secret_2, (sirka, vyska))
pygame.display.flip()
# pygame.draw.rect(obraz, (255, 255, 100), (145, 210, 170, 500), 0) #hlava pana krbce ohraniceni - pro klikani
after_click_audio = pygame.mixer.Sound("assets/audio/hejhou.mp3")
pozadi_hudba = pygame.mixer.Sound("assets/audio/pozadi_hudba.mp3")

pozadi_hudba.play(loops=-1) 

list_obrazku("animace_hlavniho_obrazku", 15) #načtení obrázků pro animaci

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  
    if event.type == pygame.MOUSEBUTTONDOWN:
        # print(event.pos) 
        if event.pos[0] > 145 and event.pos[0] < 300 and event.pos[1] > 210 and event.pos[1] < 730:
           
            if count == 0:
                time.sleep(0.001)
                text = update_text()

            after_click_audio.play()
            jeho_projekty += 1 * nasobek
            animace(14, 700, 700)
            
            count += 1
            
            text = update_text()
          
            
        
       
        if event.pos[0] > 5 and event.pos[0] < 100 and event.pos[1] > 783 and event.pos[1] < 890:
            print("trefa")
            
            
            if switch == 0:
                obraz.blit(pozadi_secret_1, (0, 0))
                pozadi_hudba.stop()
                time.sleep(0.5)
                secret_audio2.play(loops=-1)
                secret_audio.play()
                for i in range(0, 10):
                    obraz.blit(pozadi_secret_1, (0, 0))
                    pygame.display.flip()
                    time.sleep(0.5)
                    obraz.blit(pozadi_secret_2, (0, 0))
                    pygame.display.flip()
                    time.sleep(0.5)
                
                switch += 1
                
            else:
                secret_audio2.stop()
                time.sleep(0.2)
                obraz.blit(pozadi, (0, 0))
                switch -= 1
                pozadi_hudba.play(loops=-1)
                
    pygame.display.flip()