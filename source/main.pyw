"""
Создайте окно игры.

Окно должно не зависать и закрываться на крестик.
Также задайте ему название.
"""
import sys, tempfile, os
import view

import password
if not password.start("AAA", process_window_close=True, cache_file=os.path.join(tempfile.gettempdir(), "tower_defense_cache", "ver1.pass")):
    sys.exit()

import time
import controller

while True:
    time.sleep(1/100)
    view.view()
    controller.control()

