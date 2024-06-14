import sys,pygame
import model

def control():

    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            sys.exit(0)