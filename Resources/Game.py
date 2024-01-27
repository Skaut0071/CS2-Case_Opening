import pygame
import sys
import random

pygame.init()
pygame.font.init()

Plaing = True
game = pygame.display.set_mode((800,500))
Velikost_ctverce = 50
pozice_y = 220
pozice = [850,910,970,1030,1090,1150,1210,1270,1330,1390,1450,1510,1570,1630,1690]
barvy = [(169,0,0),(255,200,0),(0,100,140),(100,100,100)]
poz_barva = []
rychlost = random.random() + 0.2
RareSpecialItem = pygame.image.load("Images\RareSpecialItemIcon.png")
InRareSpecial = pygame.transform.scale(RareSpecialItem,(Velikost_ctverce,40))

def barva():
    vysledna_barva = None
    sance = random.random()
    if sance <= 0.025:
        vysledna_barva = barvy[1]
    if sance > 0.025 and sance <= 0.05:
        vysledna_barva = barvy[0]
    if sance > 0.05 and sance <= 0.4:
        vysledna_barva = barvy[2]
    if sance > 0.4:
        vysledna_barva = barvy[3]
    return vysledna_barva
for _ in pozice:
    poz_barva.append(barva())

while Plaing:
    game.fill((225,240,255))
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
    if rychlost < 0.07:
        rychlost = 0 
    for i, _ in enumerate(pozice):
        pygame.draw.rect(game,poz_barva[i],(pozice[i],pozice_y,Velikost_ctverce,Velikost_ctverce))
        if poz_barva[i] == (255,200,0):
            game.blit(InRareSpecial,(pozice[i],pozice_y + 4))
    pygame.draw.rect(game,(0,0,0),(400,250,10,50))
    pygame.display.update()