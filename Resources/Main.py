#pygame.draw.rect(Game,Barva_kostky,(pozice_hrace_x,pozice_hrace_y,velikost_kostky,velikost_kostky))

import pygame
import sys

pygame.init()
pygame.font.init()

Plaing = True
info = pygame.display.Info()
screen = (info.current_w,info.current_h)
game = pygame.display.set_mode(screen,pygame.FULLSCREEN)
Backgorund = pygame.image.load("Images\CS2-Counter-strike-2-Italy-Mid.jpg")
Background_ = pygame.transform.scale(Backgorund,screen)
my_font = pygame.font.SysFont("Comic Sans MS", 60)
text_surface = my_font.render("PLAY", False , (0, 0, 0))
def Menu():
    game.blit(Background_,(0,0))
    play_ = pygame.draw.rect(game,(35,30,35),(info.current_w/10.5,info.current_h/10.5,info.current_w/8.2,info.current_h/11.2))
    play = pygame.draw.rect(game,(60,60,60),(info.current_w/10,info.current_h/10,info.current_w/9,info.current_h/13))
    game.blit(text_surface,(info.current_w/8.5,info.current_h/10.5))
while Plaing:
    game.fill((255,255,255))
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif udalost.type == pygame.KEYDOWN:
            if udalost.key == pygame.K_ESCAPE:
                print("Game Exited Correctly")
                pygame.quit()
                sys.exit()
    klavesy = pygame.key.get_pressed()
    if klavesy[pygame.MOUSEBUTTONUP] and 
    
    Menu()
    pygame.display.update()