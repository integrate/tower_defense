
import time, pygame
from .password import *


def start(correct_pass, max_attempts = 5, process_window_close = False, cache_file = None):

    # view
    screen = pygame.display.get_surface()
    if screen is None:
        screen = pygame.display.set_mode([400, 300])
        pygame.display.set_caption("Пароль")

    result = None
    def ok_callback(status):
        nonlocal result
        result = True

    def cancel_callback(status):
        nonlocal result
        result = False

    password = Password(correct_pass, max_attempts, ok_callback, cancel_callback, cache_file)
    while result is None:
        time.sleep(1/100)

        password.draw()
        pygame.display.flip()

        password.controller(pygame.event.get(), process_window_close)

    return result