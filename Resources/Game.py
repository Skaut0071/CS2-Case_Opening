import pygame
import sys
import random

pygame.init()
pygame.font.init()

Plaing = True
game = pygame.display.set_mode((800,500))
Velikost_ctverce = 50
pozice_y = 220
pozice = [850,911.5,973,1034.5,1096,1157.5,1218.5,1280,1341.5,1403,1464.5,1526,1587.5,1649,1710.5]
barvy = [(169,0,0),(255,200,0),(0,100,140),(110,0,215)]
poz_barva = []
rychlost = random.random() + 0.2
RareSpecialItem = pygame.image.load("Images\RareSpecialItemIcon.png")
InRareSpecial = pygame.transform.scale(RareSpecialItem,(Velikost_ctverce,40))
hit_box_arrow = [400,410]
x1, y1, x2, y2 = 0, 0, 0, 0

def barva():
    vysledna_barva = None
    sance = random.random()
    if sance <= 0.025:
        vysledna_barva = barvy[1]
    if sance > 0.025 and sance <= 0.125:
        vysledna_barva = barvy[0]
    if sance > 0.125 and sance <= 0.25:
        vysledna_barva = barvy[3]
    if sance > 0.25:
        vysledna_barva = barvy[2]
    return vysledna_barva

def barvicka():    
    for _ in pozice:
        poz_barva.append(barva())
barvicka()

while Plaing:
    game.fill((170,200,255))
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            print("Game Exited Correctly")
            pygame.quit()
            sys.exit()
        elif udalost.type == pygame.KEYDOWN:
            if udalost.key == pygame.K_ESCAPE:
                print("Game Exited Correctly")
                pygame.quit()
                sys.exit()
    
    for i, x in enumerate(pozice):
        pozice[i] -= rychlost
        if pozice[i] < -75:
            pozice[i] = 850
            rychlost -= 0.01
            poz_barva[i] = barva()
            x1, y1, x2, y2 = pozice[i], pozice_y, pozice[i] + Velikost_ctverce, pozice_y + Velikost_ctverce
        if not (x2 < 400 or x1 > 400 + 10 or y2 < 250 or y1 > 250 + 50):
            pozice[i] -= 1
    if rychlost < 0.07:
        rychlost = 0 
    for i, _ in enumerate(pozice):
        pygame.draw.rect(game,poz_barva[i],(pozice[i],pozice_y,Velikost_ctverce,Velikost_ctverce))
        if poz_barva[i] == (255,200,0):
            game.blit(InRareSpecial,(pozice[i],pozice_y + 4))
    pygame.draw.rect(game,(0,0,0),(400,250,10,50))
    
    
    
    pygame.display.update()