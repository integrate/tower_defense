"""
Создайте окно игры.

Окно должно не зависать и закрываться на крестик.
Также задайте ему название.
"""
import time
import model, view, controller

while True:
    time.sleep(1/100)
    view.view()
    controller.control()

