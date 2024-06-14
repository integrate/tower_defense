import pygame

im_orig = pygame.image.load("../source/assets/images/Monsters/move/blue_down.png")

im_ready = pygame.Surface([220,317], pygame.SRCALPHA)
im_ready.blit(im_orig, [0,0],[20,16,220,317])
im_ready=pygame.transform.scale(im_ready, [24,24])

pygame.image.save(im_ready, "icon.png")

from PIL import Image
im = Image.open("icon.png")
im.save("icon.ico", "ico")