"""
Создайте окно игры.

Окно должно не зависать и закрываться на крестик.
Также задайте ему название.
"""
import sys
import time
import view

import password
if not password.start("AAA", process_window_close=True):
    sys.exit()

import controller

while True:
    time.sleep(1/100)
    view.view()
    controller.control()

