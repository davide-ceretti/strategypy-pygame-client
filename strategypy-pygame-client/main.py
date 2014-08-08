import json
import sys
import os

import pygame

from core import Game
import settings

if __name__ == "__main__":
    output = sys.stdin.read()
    data = json.loads(output)
    screen_size = settings.get_screen_size(data['grid_size'])
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.display.set_mode(screen_size)
    game = Game(data)
    game.main_loop()
    pygame.quit()
    sys.exit()
