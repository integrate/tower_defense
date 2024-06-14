import pygame
import utils

screen = pygame.display.set_mode([800, 800])
pygame.display.set_caption("Tower Defense")

def view():
    screen.fill([0,0,0])
    pygame.display.flip()



# im = pygame.image.load(utils.resource_path("assets/images/Monsters/move/blue_down.png"))
# im2 = pygame.Surface([220,317], pygame.SRCALPHA)
# im2.blit(im, [0,0],[20,16,220,317])
# pygame.display.set_icon(im2)